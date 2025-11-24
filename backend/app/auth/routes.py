from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt

from ..database import SessionLocal
from ..models import User
from ..schemas import UserCreate, UserLogin
from .utils import hash_password, verify_password, create_access_token
from ..config import SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/auth")

# OAuth2 - used for reading Bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# ------------------------
# Database Dependency
# ------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------
# Register
# ------------------------
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Validate input
        if not user.full_name or not user.full_name.strip():
            raise HTTPException(status_code=400, detail="Full name is required")
        
        if not user.email:
            raise HTTPException(status_code=400, detail="Email is required")
        
        # Normalize email: lowercase and strip whitespace
        normalized_email = str(user.email).lower().strip()
        
        if not normalized_email:
            raise HTTPException(status_code=400, detail="Email cannot be empty")
        
        if not user.password or len(user.password) < 6:
            raise HTTPException(status_code=400, detail="Password must be at least 6 characters long")
        
        # Check if user already exists (case-insensitive)
        # SQLite compatible: check all users and compare case-insensitively
        try:
            all_users = db.query(User).all()
            existing_user = None
            for u in all_users:
                if u.email and u.email.lower().strip() == normalized_email:
                    existing_user = u
                    break
        except Exception as db_error:
            print(f"Database query error: {db_error}")
            raise HTTPException(status_code=500, detail=f"Database error: {str(db_error)}")
        
        if existing_user:
            raise HTTPException(
                status_code=400, 
                detail=f"Email '{normalized_email}' is already registered. Please use a different email or try logging in."
            )

        # Hash password
        try:
            hashed_password = hash_password(user.password)
        except Exception as hash_error:
            print(f"Password hashing error: {hash_error}")
            raise HTTPException(status_code=500, detail="Error processing password")

        # Create new user
        try:
            new_user = User(
                full_name=user.full_name.strip(),
                email=normalized_email,
                password=hashed_password
            )

            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        except Exception as db_error:
            db.rollback()
            print(f"Database commit error: {db_error}")
            # Check if it's a unique constraint violation
            if "UNIQUE constraint" in str(db_error) or "unique constraint" in str(db_error).lower():
                raise HTTPException(
                    status_code=400,
                    detail=f"Email '{normalized_email}' is already registered."
                )
            raise HTTPException(
                status_code=500,
                detail=f"Database error: {str(db_error)}"
            )

        return {
            "message": "User registered successfully.",
            "user_id": new_user.id,
            "email": new_user.email
        }
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        db.rollback()
        # Log the actual error for debugging
        import traceback
        error_details = str(e)
        error_type = type(e).__name__
        print(f"Registration error [{error_type}]: {error_details}")
        print(traceback.format_exc())
        raise HTTPException(
            status_code=500,
            detail=f"Error registering user: {error_details}"
        )


# ------------------------
# Login
# ------------------------
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        # Normalize email: lowercase and strip whitespace
        normalized_email = user.email.lower().strip()
        
        if not normalized_email:
            raise HTTPException(status_code=400, detail="Email cannot be empty")
        
        if not user.password:
            raise HTTPException(status_code=400, detail="Password cannot be empty")
        
        # Find user (case-insensitive email search - SQLite compatible)
        all_users = db.query(User).all()
        db_user = None
        for u in all_users:
            if u.email.lower().strip() == normalized_email:
                db_user = u
                break

        if not db_user:
            raise HTTPException(
                status_code=401, 
                detail="Invalid email or password. Please check your credentials and try again."
            )

        # Verify password
        if not verify_password(user.password, db_user.password):
            raise HTTPException(
                status_code=401, 
                detail="Invalid email or password. Please check your credentials and try again."
            )

        # Create access token
        try:
            token = create_access_token({"user_id": db_user.id})
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error creating token: {str(e)}"
            )

        return {
            "message": "Login successful",
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "id": db_user.id,
                "email": db_user.email,
                "full_name": db_user.full_name
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        error_details = str(e)
        error_type = type(e).__name__
        print(f"Login error [{error_type}]: {error_details}")
        print(traceback.format_exc())
        raise HTTPException(
            status_code=500,
            detail=f"Error during login: {error_details}"
        )


# ------------------------
# Get Current User (JWT Protected)
# ------------------------
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


# ------------------------
# /auth/me (Protected)
# ------------------------
@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email
    }
