"""
utils.py - Utility functions for Smart Disaster Relief System
"""

import os
import csv
import logging
from datetime import datetime

def setup_logging():
    """Setup logging configuration"""
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = f'logs/disaster_system_{datetime.now().strftime("%Y%m%d")}.log'
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    
    print(f"Logging started: {log_file}")

def create_directories(dirs):
    """Create multiple directories"""
    for dir_path in dirs:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {dir_path}")

def load_csv(file_path):
    """Load CSV file and return list of dictionaries"""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        data = []
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        
        print(f"Loaded {len(data)} records from {os.path.basename(file_path)}")
        return data
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return []

def save_csv(data, file_path, fieldnames):
    """Save data to CSV file"""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Saved {len(data)} records to {file_path}")
        return True
    except Exception as e:
        print(f"Error saving {file_path}: {e}")
        return False

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def print_subheader(title):
    """Print a formatted subheader"""
    print("\n" + "-" * 50)
    print(f" {title}")
    print("-" * 50)

def get_user_input(prompt, valid_options=None):
    """Get user input with validation"""
    while True:
        user_input = input(prompt).strip()
        if valid_options and user_input not in valid_options:
            print(f"Invalid input. Please choose from: {valid_options}")
            continue
        return user_input

def get_date_input(prompt):
    """Get date input in YYYY-MM-DD format"""
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

def generate_id(prefix, existing_ids):
    """Generate a new ID with given prefix"""
    if not existing_ids:
        return f"{prefix}001"
    
    numbers = []
    for id_str in existing_ids:
        try:
            num = int(id_str.replace(prefix, ''))
            numbers.append(num)
        except:
            continue
    
    if not numbers:
        return f"{prefix}001"
    
    next_num = max(numbers) + 1
    return f"{prefix}{next_num:03d}"