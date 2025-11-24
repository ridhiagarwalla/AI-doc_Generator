"""
Quick API Test Script
Run this to test if the API is working correctly
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    """Test all API endpoints"""
    print("🧪 Testing API Endpoints...")
    print("=" * 50)
    
    # Test 1: Root endpoint
    print("\n1. Testing root endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("   ✅ Root endpoint works")
            print(f"   Response: {response.json()}")
        else:
            print(f"   ❌ Root endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
        print("   💡 Make sure backend is running on port 8000")
        return False
    
    # Test 2: Register
    print("\n2. Testing registration...")
    test_email = f"test_{hash('test')}@example.com"
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json={
                "full_name": "Test User",
                "email": test_email,
                "password": "test123456"
            }
        )
        if response.status_code == 200:
            print("   ✅ Registration works")
        elif response.status_code == 400:
            print("   ⚠️  User might already exist (this is OK)")
        else:
            print(f"   ❌ Registration failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Login
    print("\n3. Testing login...")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "email": test_email,
                "password": "test123456"
            }
        )
        if response.status_code == 200:
            data = response.json()
            token = data.get("access_token")
            if token:
                print("   ✅ Login works")
                print(f"   Token received: {token[:20]}...")
                return token
            else:
                print("   ❌ No token in response")
        else:
            print(f"   ❌ Login failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    return None

def test_with_token(token):
    """Test protected endpoints"""
    headers = {"Authorization": f"Bearer {token}"}
    
    # Test 4: Get current user
    print("\n4. Testing /auth/me...")
    try:
        response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
        if response.status_code == 200:
            print("   ✅ /auth/me works")
            print(f"   User: {response.json()}")
        else:
            print(f"   ❌ /auth/me failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: Get projects
    print("\n5. Testing /projects...")
    try:
        response = requests.get(f"{BASE_URL}/projects", headers=headers)
        if response.status_code == 200:
            projects = response.json()
            print(f"   ✅ /projects works")
            print(f"   Found {len(projects)} projects")
        else:
            print(f"   ❌ /projects failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    print("🚀 API Test Script")
    print("=" * 50)
    print("Make sure backend is running on http://localhost:8000")
    print()
    
    token = test_api()
    
    if token:
        test_with_token(token)
        print("\n" + "=" * 50)
        print("✅ Basic API tests completed!")
        print("💡 For full testing, use the frontend at http://localhost:5173")
    else:
        print("\n" + "=" * 50)
        print("⚠️  Some tests failed. Check backend is running correctly.")

