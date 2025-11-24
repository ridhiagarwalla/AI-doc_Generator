"""
Test registration endpoint directly
Run this to debug registration issues
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_registration():
    """Test registration with detailed error reporting"""
    print("🧪 Testing Registration Endpoint...")
    print("=" * 50)
    
    test_data = {
        "full_name": "Test User",
        "email": "testuser@example.com",
        "password": "test123456"
    }
    
    print(f"\n📤 Sending registration request...")
    print(f"URL: {BASE_URL}/auth/register")
    print(f"Data: {json.dumps(test_data, indent=2)}")
    
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"\n📥 Response Status: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        try:
            response_data = response.json()
            print(f"Response Data: {json.dumps(response_data, indent=2)}")
        except:
            print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            print("\n✅ Registration successful!")
            return True
        else:
            print(f"\n❌ Registration failed with status {response.status_code}")
            if response.status_code == 400:
                print("   This might mean:")
                print("   - Email already exists")
                print("   - Validation error")
            elif response.status_code == 500:
                print("   This might mean:")
                print("   - Database error")
                print("   - Server error")
            return False
            
    except requests.exceptions.ConnectionError:
        print("\n❌ Cannot connect to server!")
        print("   💡 Make sure backend is running on http://localhost:8000")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Make sure backend is running first!")
    print("Then run this script to test registration.\n")
    test_registration()

