"""
disaster.py - Disaster Management Module
"""

import os
from datetime import datetime
from utils import (
    load_csv, save_csv, print_header, print_subheader, 
    get_user_input, get_date_input, generate_id
)

class DisasterManager:
    """Handles all disaster-related operations"""
    
    def __init__(self):
        self.data_file = 'data/disasters.csv'
        self.fieldnames = ['Disaster_ID', 'Disaster_Type', 'State', 'District', 
                           'Start_Date', 'End_Date', 'Severity', 'Affected_People', 'Status']
        self.disasters = []
        self.load_data()
    
    def load_data(self):
        """Load disasters from CSV"""
        self.disasters = load_csv(self.data_file)
    
    def save_data(self):
        """Save disasters to CSV"""
        save_csv(self.disasters, self.data_file, self.fieldnames)
    
    def get_all_ids(self):
        """Get all disaster IDs"""
        return [d['Disaster_ID'] for d in self.disasters]
    
    def add_disaster(self):
        """Add a new disaster"""
        print_header("ADD NEW DISASTER")
        
        disaster_types = ['Flood', 'Earthquake', 'Cyclone', 'Tsunami', 'Landslide', 
                          'Drought', 'Heatwave', 'Cold Wave', 'Forest Fire', 'Epidemic']
        
        severity_levels = ['Low', 'Medium', 'High', 'Critical']
        statuses = ['Active', 'Resolved', 'Recovery Phase', 'Under Control']
        
        disaster_id = generate_id('DIS', self.get_all_ids())
        
        print(f"Disaster ID: {disaster_id}")
        
        print("\nSelect Disaster Type:")
        for i, dt in enumerate(disaster_types, 1):
            print(f"  {i}. {dt}")
        type_choice = get_user_input("Enter choice: ", [str(i) for i in range(1, len(disaster_types)+1)])
        disaster_type = disaster_types[int(type_choice)-1]
        
        state = get_user_input("Enter State: ")
        district = get_user_input("Enter District: ")
        start_date = get_date_input("Enter Start Date (YYYY-MM-DD): ")
        end_date = get_date_input("Enter End Date (YYYY-MM-DD): ")
        
        print("\nSelect Severity:")
        for i, sev in enumerate(severity_levels, 1):
            print(f"  {i}. {sev}")
        sev_choice = get_user_input("Enter choice: ", [str(i) for i in range(1, len(severity_levels)+1)])
        severity = severity_levels[int(sev_choice)-1]
        
        affected = get_user_input("Enter Affected People Count: ")
        
        print("\nSelect Status:")
        for i, st in enumerate(statuses, 1):
            print(f"  {i}. {st}")
        status_choice = get_user_input("Enter choice: ", [str(i) for i in range(1, len(statuses)+1)])
        status = statuses[int(status_choice)-1]
        
        disaster = {
            'Disaster_ID': disaster_id,
            'Disaster_Type': disaster_type,
            'State': state,
            'District': district,
            'Start_Date': start_date,
            'End_Date': end_date,
            'Severity': severity,
            'Affected_People': affected,
            'Status': status
        }
        
        self.disasters.append(disaster)
        self.save_data()
        print(f"\nDisaster {disaster_id} added successfully!")
    
    def view_disasters(self):
        """View all disasters"""
        print_header("VIEW DISASTERS")
        
        if not self.disasters:
            print("No disasters found.")
            return
        
        print("\n" + "-" * 100)
        print(f"{'ID':<10} {'Type':<15} {'State':<15} {'District':<15} {'Severity':<10} {'Affected':<12} {'Status':<15}")
        print("-" * 100)
        
        for d in self.disasters:
            print(f"{d['Disaster_ID']:<10} {d['Disaster_Type']:<15} {d['State']:<15} {d['District']:<15} {d['Severity']:<10} {d['Affected_People']:<12} {d['Status']:<15}")
        
        print("-" * 100)
        print(f"Total: {len(self.disasters)} disasters")
    
    def search_disaster(self):
        """Search for a disaster"""
        print_header("SEARCH DISASTER")
        
        disaster_id = get_user_input("Enter Disaster ID to search: ")
        
        for d in self.disasters:
            if d['Disaster_ID'] == disaster_id:
                print("\n" + "-" * 50)
                print(f"ID: {d['Disaster_ID']}")
                print(f"Type: {d['Disaster_Type']}")
                print(f"State: {d['State']}")
                print(f"District: {d['District']}")
                print(f"Start Date: {d['Start_Date']}")
                print(f"End Date: {d['End_Date']}")
                print(f"Severity: {d['Severity']}")
                print(f"Affected People: {d['Affected_People']}")
                print(f"Status: {d['Status']}")
                print("-" * 50)
                return
        
        print("Disaster not found!")
    
    def update_disaster(self):
        """Update a disaster record"""
        print_header("UPDATE DISASTER")
        
        disaster_id = get_user_input("Enter Disaster ID to update: ")
        
        for i, d in enumerate(self.disasters):
            if d['Disaster_ID'] == disaster_id:
                print("\nLeave blank to keep current value")
                print(f"Current Type: {d['Disaster_Type']}")
                new_type = get_user_input("New Type (or press Enter): ")
                if new_type:
                    d['Disaster_Type'] = new_type
                
                print(f"Current State: {d['State']}")
                new_state = get_user_input("New State (or press Enter): ")
                if new_state:
                    d['State'] = new_state
                
                print(f"Current District: {d['District']}")
                new_district = get_user_input("New District (or press Enter): ")
                if new_district:
                    d['District'] = new_district
                
                print(f"Current Severity: {d['Severity']}")
                new_severity = get_user_input("New Severity (or press Enter): ")
                if new_severity:
                    d['Severity'] = new_severity
                
                print(f"Current Status: {d['Status']}")
                new_status = get_user_input("New Status (or press Enter): ")
                if new_status:
                    d['Status'] = new_status
                
                self.save_data()
                print(f"\nDisaster {disaster_id} updated successfully!")
                return
        
        print("Disaster not found!")
    
    def delete_disaster(self):
        """Delete a disaster record"""
        print_header("DELETE DISASTER")
        
        disaster_id = get_user_input("Enter Disaster ID to delete: ")
        
        for i, d in enumerate(self.disasters):
            if d['Disaster_ID'] == disaster_id:
                confirm = get_user_input(f"Are you sure you want to delete {disaster_id}? (y/n): ", ['y', 'n'])
                if confirm == 'y':
                    self.disasters.pop(i)
                    self.save_data()
                    print(f"\nDisaster {disaster_id} deleted successfully!")
                else:
                    print("Deletion cancelled.")
                return
        
        print("Disaster not found!")
    
    def menu(self):
        """Display disaster management menu"""
        while True:
            print_header("DISASTER MANAGEMENT")
            print("[1] Add Disaster")
            print("[2] View All Disasters")
            print("[3] Search Disaster")
            print("[4] Update Disaster")
            print("[5] Delete Disaster")
            print("[0] Back to Main Menu")
            print("-" * 50)
            
            choice = get_user_input("Enter your choice: ", 
                                   ['0', '1', '2', '3', '4', '5'])
            
            if choice == '0':
                break
            elif choice == '1':
                self.add_disaster()
            elif choice == '2':
                self.view_disasters()
            elif choice == '3':
                self.search_disaster()
            elif choice == '4':
                self.update_disaster()
            elif choice == '5':
                self.delete_disaster()
            
            input("\nPress Enter to continue...")