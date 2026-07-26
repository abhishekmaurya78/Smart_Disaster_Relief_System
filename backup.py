"""
backup.py - Backup System for Smart Disaster Relief System
"""

import os
import shutil
import datetime
from utils import print_header, get_user_input

class BackupSystem:
    """Handles data backup and restore"""
    
    def __init__(self):
        self.data_dir = 'data'
        self.backup_dir = 'backup'
        self.files = ['disasters.csv', 'victims.csv', 'volunteers.csv', 
                      'relief_camps.csv', 'food_inventory.csv', 'medicine_inventory.csv']
        os.makedirs(self.backup_dir, exist_ok=True)
    
    def create_backup(self):
        """Create a backup of all data files"""
        print_header("CREATE BACKUP")
        
        if not os.path.exists(self.data_dir):
            print("No data directory found!")
            return
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_folder = os.path.join(self.backup_dir, f"backup_{timestamp}")
        os.makedirs(backup_folder, exist_ok=True)
        
        count = 0
        for file in self.files:
            src = os.path.join(self.data_dir, file)
            if os.path.exists(src):
                dst = os.path.join(backup_folder, file)
                shutil.copy2(src, dst)
                print(f"   Copied: {file}")
                count += 1
        
        print(f"\nBackup completed! {count} files backed up to: {backup_folder}")
        return backup_folder
    
    def list_backups(self):
        """List all available backups"""
        print_header("LIST BACKUPS")
        
        if not os.path.exists(self.backup_dir):
            print("No backups found!")
            return []
        
        backups = [f for f in os.listdir(self.backup_dir) if f.startswith('backup_')]
        
        if not backups:
            print("No backups found!")
            return []
        
        print("\nAvailable Backups:")
        print("-" * 50)
        for i, backup in enumerate(sorted(backups, reverse=True), 1):
            backup_path = os.path.join(self.backup_dir, backup)
            size = sum(os.path.getsize(os.path.join(backup_path, f)) for f in os.listdir(backup_path) if os.path.isfile(os.path.join(backup_path, f)))
            print(f"{i}. {backup} ({size/1024:.1f} KB)")
        
        return sorted(backups, reverse=True)
    
    def restore_backup(self):
        """Restore data from a backup"""
        print_header("RESTORE BACKUP")
        
        backups = self.list_backups()
        if not backups:
            return
        
        choice = get_user_input("\nEnter backup number to restore (0 to cancel): ", 
                                [str(i) for i in range(len(backups)+1)])
        
        if choice == '0':
            print("Restore cancelled.")
            return
        
        backup_name = backups[int(choice)-1]
        backup_path = os.path.join(self.backup_dir, backup_name)
        
        confirm = get_user_input(f"Restore from {backup_name}? (y/n): ", ['y', 'n'])
        if confirm != 'y':
            print("Restore cancelled.")
            return
        
        count = 0
        for file in self.files:
            src = os.path.join(backup_path, file)
            if os.path.exists(src):
                dst = os.path.join(self.data_dir, file)
                shutil.copy2(src, dst)
                print(f"   Restored: {file}")
                count += 1
        
        print(f"\nRestore completed! {count} files restored from {backup_name}")
    
    def menu(self):
        """Backup menu"""
        while True:
            print_header("BACKUP SYSTEM")
            print("[1] Create Backup")
            print("[2] List Backups")
            print("[3] Restore Backup")
            print("[0] Back to Main Menu")
            print("-" * 50)
            
            choice = get_user_input("Enter your choice: ", ['0', '1', '2', '3'])
            
            if choice == '0':
                break
            elif choice == '1':
                self.create_backup()
            elif choice == '2':
                self.list_backups()
            elif choice == '3':
                self.restore_backup()
            
            input("\nPress Enter to continue...")