"""
main.py - Main entry point for Smart Disaster Relief System
"""

import sys
import os
from utils import print_header, print_subheader, get_user_input, setup_logging
from auth import AuthSystem
from disaster import DisasterManager
from backup import BackupSystem
from report import ReportGenerator

class DisasterReliefSystem:
    """Main application class"""
    
    def __init__(self):
        self.auth = AuthSystem()
        self.disaster_manager = DisasterManager()
        self.backup_system = BackupSystem()
        self.report_gen = ReportGenerator()
        self.running = True
    
    def display_main_menu(self):
        """Display main menu"""
        print_header("SMART DISASTER RELIEF SYSTEM")
        print("\n[1] Disaster Management")
        print("[2] Victim Management")
        print("[3] Volunteer Management")
        print("[4] Relief Camp Management")
        print("[5] Inventory Management")
        print("[6] Reports")
        print("[7] Backup")
        print("[8] Change Password")
        print("[9] Logout")
        print("[0] Exit")
        print("-" * 50)
    
    def run(self):
        """Main application loop"""
        print_header("SMART DISASTER RELIEF SYSTEM")
        print("Welcome to Smart Disaster Relief System!")
        
        while not self.auth.is_logged_in():
            self.auth.login()
        
        print(f"\nLogged in as: {self.auth.current_user}")
        
        while self.running:
            self.display_main_menu()
            choice = get_user_input("\nEnter your choice: ", 
                                   ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
            
            if choice == '0':
                self.running = False
                print("\nThank you for using Smart Disaster Relief System!")
                
            elif choice == '1':
                self.disaster_manager.menu()
                
            elif choice == '2':
                print("\nVictim Management - Coming Soon!")
                
            elif choice == '3':
                print("\nVolunteer Management - Coming Soon!")
                
            elif choice == '4':
                print("\nRelief Camp Management - Coming Soon!")
                
            elif choice == '5':
                print("\nInventory Management - Coming Soon!")
                
            elif choice == '6':
                self.report_gen.menu()
                
            elif choice == '7':
                self.backup_system.menu()
                
            elif choice == '8':
                self.auth.change_password()
                
            elif choice == '9':
                self.auth.logout()
                while not self.auth.is_logged_in():
                    self.auth.login()
                print(f"\nLogged in as: {self.auth.current_user}")
            
            input("\nPress Enter to continue...")

def main():
    """Main function"""
    setup_logging()
    try:
        system = DisasterReliefSystem()
        system.run()
    except KeyboardInterrupt:
        print("\n\nSystem interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()