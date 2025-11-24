"""
Authentication Callable Module
This module provides authentication functions that can be called to verify tokens and permissions.
"""

import jwt
import datetime
from functools import wraps
from flask import request, jsonify

# Secret key for JWT (in production, use environment variable)
SECRET_KEY = "your-secret-key-change-in-production"

class AuthModule:
    """Callable authentication module for testing"""
    
    def __init__(self, secret_key=None):
        self.secret_key = secret_key or SECRET_KEY
        self.valid_users = {
            "admin": "admin123",
            "user": "user123",
            "testuser": "test123"
        }
    
    def generate_token(self, username, expires_in_minutes=60):
        """
        Generate a JWT token for a user
        
        Args:
            username (str): The username to generate token for
            expires_in_minutes (int): Token expiration time in minutes
            
        Returns:
            str: JWT token
        """
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_in_minutes),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token
    
    def verify_token(self, token):
        """
        Verify a JWT token
        
        Args:
            token (str): The JWT token to verify
            
        Returns:
            dict: Decoded token payload if valid, None otherwise
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    def authenticate_user(self, username, password):
        """
        Authenticate a user with username and password
        
        Args:
            username (str): Username
            password (str): Password
            
        Returns:
            bool: True if authentication successful, False otherwise
        """
        return username in self.valid_users and self.valid_users[username] == password
    
    def require_auth(self, f):
        """
        Decorator to require authentication for a route
        Usage: @auth_module.require_auth
        """
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Get token from Authorization header
            auth_header = request.headers.get('Authorization')
            
            if not auth_header:
                return jsonify({
                    'success': False,
                    'message': 'Missing Authorization header',
                    'tip': 'Include "Authorization: Bearer <token>" in your request headers'
                }), 401
            
            # Check if it's a Bearer token
            parts = auth_header.split()
            if len(parts) != 2 or parts[0].lower() != 'bearer':
                return jsonify({
                    'success': False,
                    'message': 'Invalid Authorization header format',
                    'tip': 'Use format: "Authorization: Bearer <token>"'
                }), 401
            
            token = parts[1]
            
            # Verify the token
            payload = self.verify_token(token)
            if not payload:
                return jsonify({
                    'success': False,
                    'message': 'Invalid or expired token',
                    'tip': 'Get a new token from /api/login endpoint'
                }), 401
            
            # Add user info to request for use in the route
            request.user = payload
            
            return f(*args, **kwargs)
        
        return decorated_function
    
    def get_user_from_request(self):
        """
        Get the authenticated user from the current request
        
        Returns:
            dict: User payload from token
        """
        return getattr(request, 'user', None)


# Create a singleton instance for easy importing
auth_module = AuthModule()
