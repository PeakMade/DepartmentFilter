# 🔐 Authentication Test App

A simple Flask application to test your authentication callable module. This app demonstrates JWT-based authentication with a protected endpoint that returns a list of names.

## 📋 Features

- **Authentication Module** (`auth_module.py`): A callable module with authentication functions
- **JWT Token Generation**: Secure token-based authentication
- **Protected Endpoints**: Endpoints that require valid authentication
- **Names API**: Returns a list of names when properly authenticated
- **Interactive UI**: Beautiful web interface to test authentication
- **Helpful Error Messages**: Clear feedback to help you understand what's working

## 🚀 Quick Start

### 1. Install Dependencies

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Run the Application

```powershell
python app.py
```

The app will start on `http://localhost:5000`

### 3. Test the Authentication

Open your browser and go to: **http://localhost:5000**

## 🔑 Test Credentials

Use any of these credentials to test:

- Username: `admin` / Password: `admin123`
- Username: `user` / Password: `user123`
- Username: `testuser` / Password: `test123`

## 📡 API Endpoints

### POST `/api/login`
Login to get a JWT token

**Request:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login successful! ✓",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "username": "admin"
}
```

### GET `/api/names` 🔒 (Protected)
Get list of names - requires authentication

**Headers:**
```
Authorization: Bearer <your-token>
```

**Response:**
```json
{
  "success": true,
  "message": "Authentication verified! ✓",
  "authenticated_as": "admin",
  "data": [
    {"id": 1, "name": "Alice Johnson", "department": "Engineering"},
    ...
  ],
  "count": 8
}
```

### GET `/api/me` 🔒 (Protected)
Get current authenticated user info

**Headers:**
```
Authorization: Bearer <your-token>
```

**Response:**
```json
{
  "success": true,
  "message": "You are authenticated! ✓",
  "user": {
    "username": "admin",
    "token_issued_at": 1732464000,
    "token_expires_at": 1732467600
  }
}
```

### GET `/api/health`
Health check endpoint (no auth required)

### GET `/api/test-scenarios`
Get list of test scenarios to try

## 🧪 Testing with cURL

### 1. Login to get a token:
```powershell
curl -X POST http://localhost:5000/api/login `
  -H "Content-Type: application/json" `
  -d '{"username":"admin","password":"admin123"}'
```

### 2. Use the token to access protected endpoint:
```powershell
curl http://localhost:5000/api/names `
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## 🧩 Using the Authentication Module

The `auth_module.py` is designed to be callable and reusable. Here's how to use it:

### Basic Usage:

```python
from auth_module import auth_module

# Authenticate a user
if auth_module.authenticate_user("admin", "admin123"):
    # Generate a token
    token = auth_module.generate_token("admin")
    print(f"Token: {token}")

# Verify a token
payload = auth_module.verify_token(token)
if payload:
    print(f"Token is valid for user: {payload['username']}")
```

### As a Decorator:

```python
from flask import Flask
from auth_module import auth_module

app = Flask(__name__)

@app.route('/protected')
@auth_module.require_auth  # Just add this decorator!
def protected_route():
    user = auth_module.get_user_from_request()
    return f"Hello, {user['username']}!"
```

## ✅ What You're Testing

This app helps you verify that your authentication module correctly:

1. ✅ **Generates JWT tokens** with proper expiration
2. ✅ **Validates credentials** against a user database
3. ✅ **Verifies tokens** on protected endpoints
4. ✅ **Handles missing tokens** with helpful error messages
5. ✅ **Handles invalid tokens** appropriately
6. ✅ **Extracts user info** from valid tokens
7. ✅ **Works as a decorator** for route protection

## 📁 Project Structure

```
DepartmentFilter/
│
├── app.py              # Main Flask application
├── auth_module.py      # Authentication callable module
├── index.html          # Interactive test UI
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🛠️ Customization

### Add More Users:
Edit the `valid_users` dictionary in `auth_module.py`:

```python
self.valid_users = {
    "admin": "admin123",
    "newuser": "newpassword"
}
```

### Add More Names:
Edit the `NAMES_DATABASE` list in `app.py`:

```python
NAMES_DATABASE = [
    {"id": 1, "name": "Your Name", "department": "Your Dept"},
    ...
]
```

### Change Token Expiration:
Modify the `expires_in_minutes` parameter when calling `generate_token()`.

## 🔍 Troubleshooting

**Problem:** "Missing Authorization header"
- **Solution:** Make sure you include `Authorization: Bearer <token>` in your request headers

**Problem:** "Invalid or expired token"
- **Solution:** Login again to get a fresh token (tokens expire after 60 minutes)

**Problem:** "Invalid credentials"
- **Solution:** Check that you're using the correct username/password combination

## 💡 Tips

- Tokens expire after 60 minutes by default
- The app provides helpful error messages to guide you
- Check the browser console for detailed error information
- Use the web UI for the easiest testing experience
- Try the `/api/test-scenarios` endpoint for testing ideas

## 📚 Learning Points

This app demonstrates:
- **Callable Module Pattern**: How to create reusable authentication functions
- **JWT Authentication**: Industry-standard token-based auth
- **Decorator Pattern**: Using decorators to protect routes
- **Error Handling**: Providing helpful feedback to API consumers
- **RESTful API Design**: Clean, predictable endpoint structure

---

**Happy Testing! 🎉**
