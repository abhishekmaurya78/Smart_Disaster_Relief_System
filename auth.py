"""
auth.py - Admin Authentication System for Smart Disaster Relief System
"""

import hashlib
import json
import os
from utils import print_header, print_subheader, get_user_input

class AuthSystem:
    """Handles admin authentication"""
    
    def __init__(self):
        self.users_file = 'data/users.json'
        self.current_user = None
        self.load_users()
    
    def load_users(self):
        """Load users from JSON file"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as f:
                    self.users = json.load(f)
            except:
                self.users = {}
        else:
            # Default admin account
            self.users = {
                'admin': {
                    'password': hashlib.sha256('admin123'.encode()).hexdigest(),
                    'role': 'admin',
                    'name': 'Administrator'
                }
            }
            self.save_users()
    
    def save_users(self):
        """Save users to JSON file"""
        os.makedirs('data', exist_ok=True)
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=4)
    
    def hash_password(self, password):
        """Hash password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def login(self):
        """Admin login process"""
        print_header("ADMIN LOGIN")
        
        username = get_user_input("Enter username: ")
        password = get_user_input("Enter password: ")
        
        if username in self.users:
            if self.users[username]['password'] == self.hash_password(password):
                self.current_user = username
                print(f"\nWelcome, {self.users[username]['name']}!")
                return True
        
        print("\nInvalid username or password!")
        return False
    
    def change_password(self):
        """Change admin password"""
        if not self.current_user:
            print("Please login first!")
            return
        
        print_subheader("CHANGE PASSWORD")
        
        old_password = get_user_input("Enter old password: ")
        if self.users[self.current_user]['password'] != self.hash_password(old_password):
            print("Invalid old password!")
            return
        
        new_password = get_user_input("Enter new password: ")
        confirm_password = get_user_input("Confirm new password: ")
        
        if new_password != confirm_password:
            print("Passwords do not match!")
            return
        
        self.users[self.current_user]['password'] = self.hash_password(new_password)
        self.save_users()
        print("Password changed successfully!")
    
    def logout(self):
        """Logout current user"""
        self.current_user = None
        print("Logged out successfully!")
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return self.current_user is not None