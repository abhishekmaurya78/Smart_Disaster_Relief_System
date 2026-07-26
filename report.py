"""
report.py - Report Generation System for Smart Disaster Relief System
"""

import os
import csv
from datetime import datetime
from utils import print_header, get_user_input, load_csv

class ReportGenerator:
    """Generates reports from data"""
    
    def __init__(self):
        self.report_dir = 'reports'
        os.makedirs(self.report_dir, exist_ok=True)
    
    def generate_disaster_report(self):
        """Generate disaster summary report"""
        print_header("GENERATE DISASTER REPORT")
        
        disasters = load_csv('data/disasters.csv')
        if not disasters:
            print("No disaster data found!")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = os.path.join(self.report_dir, f"disaster_report_{timestamp}.txt")
        
        with open(report_file, 'w') as f:
            f.write("=" * 70 + "\n")
            f.write(" DISASTER RELIEF SYSTEM - DISASTER REPORT\n")
            f.write("=" * 70 + "\n")
            f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Disasters: {len(disasters)}\n")
            f.write("=" * 70 + "\n\n")
            
            # Summary by severity
            f.write("SEVERITY SUMMARY\n")
            f.write("-" * 50 + "\n")
            severity_count = {}
            for d in disasters:
                severity = d.get('Severity', 'Unknown')
                severity_count[severity] = severity_count.get(severity, 0) + 1
            for sev, count in severity_count.items():
                f.write(f"  {sev}: {count}\n")
            
            # Summary by status
            f.write("\nSTATUS SUMMARY\n")
            f.write("-" * 50 + "\n")
            status_count = {}
            for d in disasters:
                status = d.get('Status', 'Unknown')
                status_count[status] = status_count.get(status, 0) + 1
            for st, count in status_count.items():
                f.write(f"  {st}: {count}\n")
            
            # Summary by type
            f.write("\nDISASTER TYPE SUMMARY\n")
            f.write("-" * 50 + "\n")
            type_count = {}
            for d in disasters:
                dtype = d.get('Disaster_Type', 'Unknown')
                type_count[dtype] = type_count.get(dtype, 0) + 1
            for dtype, count in sorted(type_count.items(), key=lambda x: x[1], reverse=True):
                f.write(f"  {dtype}: {count}\n")
            
            f.write("\n" + "=" * 70 + "\n")
            f.write(" DETAILED DISASTER LIST\n")
            f.write("=" * 70 + "\n\n")
            f.write(f"{'ID':<10} {'Type':<15} {'State':<15} {'Severity':<10} {'Affected':<12} {'Status':<15}\n")
            f.write("-" * 70 + "\n")
            for d in disasters:
                f.write(f"{d.get('Disaster_ID', 'N/A'):<10} {d.get('Disaster_Type', 'N/A'):<15} {d.get('State', 'N/A'):<15} {d.get('Severity', 'N/A'):<10} {d.get('Affected_People', 'N/A'):<12} {d.get('Status', 'N/A'):<15}\n")
        
        print(f"\nReport saved to: {report_file}")
        return report_file
    
    def menu(self):
        """Report menu"""
        while True:
            print_header("REPORT GENERATOR")
            print("[1] Generate Disaster Report")
            print("[0] Back to Main Menu")
            print("-" * 50)
            
            choice = get_user_input("Enter your choice: ", ['0', '1'])
            
            if choice == '0':
                break
            elif choice == '1':
                self.generate_disaster_report()
            
            input("\nPress Enter to continue...")