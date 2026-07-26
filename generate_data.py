"""
generate_data.py - Complete Dataset Generation for Smart Disaster Relief System
"""

import csv
import random
from datetime import datetime, timedelta
import os

# DATA GENERATION FUNCTIONS

def generate_disasters():
    """Generate 50 disaster records"""
    
    disaster_types = ['Flood', 'Earthquake', 'Cyclone', 'Tsunami', 'Landslide', 
                      'Drought', 'Heatwave', 'Cold Wave', 'Forest Fire', 'Epidemic']
    
    states = ['Maharashtra', 'Gujarat', 'Rajasthan', 'Uttar Pradesh', 'Bihar', 
              'West Bengal', 'Tamil Nadu', 'Kerala', 'Karnataka', 'Odisha',
              'Assam', 'Punjab', 'Haryana', 'Jammu and Kashmir', 'Himachal Pradesh']
    
    districts = {
        'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Nashik', 'Aurangabad'],
        'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar'],
        'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota', 'Bikaner'],
        'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Varanasi', 'Agra', 'Prayagraj'],
        'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Darbhanga'],
        'West Bengal': ['Kolkata', 'Howrah', 'Siliguri', 'Darjeeling', 'Asansol'],
        'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem'],
        'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Thrissur', 'Alappuzha'],
        'Karnataka': ['Bengaluru', 'Mysuru', 'Hubballi', 'Mangaluru', 'Belagavi'],
        'Odisha': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Puri', 'Sambalpur'],
        'Assam': ['Guwahati', 'Silchar', 'Dibrugarh', 'Jorhat', 'Tezpur'],
        'Punjab': ['Chandigarh', 'Amritsar', 'Ludhiana', 'Patiala', 'Jalandhar'],
        'Haryana': ['Gurugram', 'Faridabad', 'Panipat', 'Ambala', 'Karnal'],
        'Jammu and Kashmir': ['Srinagar', 'Jammu', 'Anantnag', 'Baramulla', 'Udhampur'],
        'Himachal Pradesh': ['Shimla', 'Dharamshala', 'Manali', 'Kullu', 'Mandi']
    }
    
    severity_levels = ['Low', 'Medium', 'High', 'Critical']
    statuses = ['Active', 'Resolved', 'Recovery Phase', 'Under Control']
    
    disasters = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(1, 51):
        state = random.choice(states)
        district = random.choice(districts.get(state, ['Unknown']))
        disaster_type = random.choice(disaster_types)
        
        days_offset = random.randint(0, 800)
        start = start_date + timedelta(days=days_offset)
        duration = random.randint(1, 60)
        end = start + timedelta(days=duration)
        
        severity = random.choices(severity_levels, weights=[0.15, 0.30, 0.35, 0.20])[0]
        affected = random.randint(100, 50000)
        status = random.choices(statuses, weights=[0.30, 0.25, 0.25, 0.20])[0]
        
        disasters.append({
            'Disaster_ID': f'DIS{i:03d}',
            'Disaster_Type': disaster_type,
            'State': state,
            'District': district,
            'Start_Date': start.strftime('%Y-%m-%d'),
            'End_Date': end.strftime('%Y-%m-%d'),
            'Severity': severity,
            'Affected_People': affected,
            'Status': status
        })
    
    return disasters


def generate_victims():
    """Generate 1000 victim records"""
    
    first_names = ['Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Sai', 'Pranav', 'Dhruv',
                   'Krishna', 'Shaurya', 'Aryan', 'Ayaan', 'Ananya', 'Diya', 'Anika', 'Aanya',
                   'Myra', 'Ishita', 'Ishika', 'Riya', 'Sara', 'Sana', 'Isha', 'Anvi',
                   'Sneha', 'Rohan', 'Amit', 'Pooja', 'Raj', 'Priya', 'Sanjay', 'Sunita']
    
    last_names = ['Sharma', 'Verma', 'Patel', 'Singh', 'Yadav', 'Kumar', 'Gupta', 'Joshi',
                  'Mehta', 'Shah', 'Desai', 'Pandey', 'Rao', 'Reddy', 'Nair', 'Menon']
    
    genders = ['Male', 'Female']
    medical_statuses = ['Healthy', 'Minor Injuries', 'Serious Injuries', 'Critical', 'Under Treatment']
    states = ['Maharashtra', 'Gujarat', 'Rajasthan', 'Uttar Pradesh', 'Bihar', 
              'West Bengal', 'Tamil Nadu', 'Kerala', 'Karnataka', 'Odisha']
    
    victims = []
    for i in range(1, 1001):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(1, 85)
        gender = random.choice(genders)
        state = random.choice(states)
        district = random.choice(['District_A', 'District_B', 'District_C', 'District_D'])
        phone = f"9{random.randint(100000000, 999999999)}"
        disaster_id = f"DIS{random.randint(1, 50):03d}"
        camp_id = f"CAMP{random.randint(1, 100):03d}"
        medical_status = random.choices(medical_statuses, weights=[0.30, 0.25, 0.20, 0.10, 0.15])[0]
        
        victims.append({
            'Victim_ID': f'VIC{i:04d}',
            'Name': name,
            'Age': age,
            'Gender': gender,
            'State': state,
            'District': district,
            'Phone': phone,
            'Disaster_ID': disaster_id,
            'Camp_ID': camp_id,
            'Medical_Status': medical_status
        })
    
    return victims


def generate_volunteers():
    """Generate 200 volunteer records"""
    
    first_names = ['Dr.', 'Prof.', 'Mr.', 'Ms.', 'Mrs.'] + ['Amit', 'Rahul', 'Vikram', 'Suresh',
                   'Rakesh', 'Manish', 'Rajesh', 'Prakash', 'Deepak', 'Sunil', 'Anita', 'Kavita',
                   'Sangeeta', 'Meena', 'Rekha', 'Neha', 'Priyanka', 'Sakshi', 'Ruchi']
    
    last_names = ['Sharma', 'Verma', 'Patel', 'Singh', 'Yadav', 'Kumar', 'Gupta', 'Joshi',
                  'Mehta', 'Shah', 'Desai', 'Pandey', 'Rao', 'Reddy']
    
    departments = ['Medical', 'Rescue', 'Logistics', 'Food Supply', 'Shelter Management',
                   'Communication', 'First Aid', 'Search and Rescue', 'Transport', 'Administration']
    
    volunteers = []
    for i in range(1, 201):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(18, 65)
        gender = random.choice(['Male', 'Female'])
        phone = f"9{random.randint(100000000, 999999999)}"
        department = random.choice(departments)
        camp_id = f"CAMP{random.randint(1, 100):03d}"
        
        volunteers.append({
            'Volunteer_ID': f'VOL{i:03d}',
            'Name': name,
            'Age': age,
            'Gender': gender,
            'Phone': phone,
            'Department': department,
            'Assigned_Camp': camp_id
        })
    
    return volunteers


def generate_relief_camps():
    """Generate 100 relief camp records"""
    
    camp_names = ['Red Cross Camp', 'Holy Family School', 'Community Hall', 'Stadium Camp',
                  'Temple Ground', 'Church Hall', 'Municipal School', 'Community Center',
                  'Relief Shelter', 'Emergency Camp', 'Volunteer Camp', 'Medical Camp',
                  'Food Distribution Center', 'Shelter Home', 'Relief Point', 'Evacuation Camp',
                  'Emergency Shelter', 'Community Kitchen', 'Aid Camp', 'Support Center']
    
    states = ['Maharashtra', 'Gujarat', 'Rajasthan', 'Uttar Pradesh', 'Bihar', 
              'West Bengal', 'Tamil Nadu', 'Kerala', 'Karnataka', 'Odisha']
    
    camps = []
    for i in range(1, 101):
        name = random.choice(camp_names) + f" {i}"
        state = random.choice(states)
        district = random.choice(['District_A', 'District_B', 'District_C', 'District_D'])
        capacity = random.randint(50, 1000)
        current = random.randint(0, capacity)
        food_stock = random.randint(100, 5000)
        medicine_stock = random.randint(50, 2000)
        
        camps.append({
            'Camp_ID': f'CAMP{i:03d}',
            'Camp_Name': name,
            'State': state,
            'District': district,
            'Capacity': capacity,
            'Current_People': current,
            'Food_Stock': food_stock,
            'Medicine_Stock': medicine_stock
        })
    
    return camps


def generate_food_inventory():
    """Generate 500 food inventory records"""
    
    food_items = ['Rice (25kg)', 'Wheat Flour (10kg)', 'Cooking Oil (5L)', 'Sugar (5kg)',
                  'Salt (1kg)', 'Dal (2kg)', 'Canned Food', 'Milk Powder (500g)',
                  'Biscuits', 'Noodles', 'Pasta', 'Cereal', 'Bread', 'Eggs',
                  'Vegetable Oil (5L)', 'Tea Powder', 'Coffee', 'Spices Pack',
                  'Ready-to-Eat Meals', 'Protein Bars', 'Water Bottles', 'Juice Packets']
    
    units = ['kg', 'L', 'packets', 'bottles', 'boxes', 'cartons']
    
    food_items_list = []
    for i in range(1, 501):
        food_name = random.choice(food_items)
        quantity = random.randint(10, 500)
        unit = random.choice(units)
        expiry = datetime.now() + timedelta(days=random.randint(30, 365))
        camp_id = f"CAMP{random.randint(1, 100):03d}"
        
        food_items_list.append({
            'Food_ID': f'FOOD{i:04d}',
            'Food_Name': food_name,
            'Quantity': quantity,
            'Unit': unit,
            'Expiry_Date': expiry.strftime('%Y-%m-%d'),
            'Camp_ID': camp_id
        })
    
    return food_items_list


def generate_medicine_inventory():
    """Generate 500 medicine inventory records"""
    
    medicines = ['Paracetamol (500mg)', 'Ibuprofen (400mg)', 'Antibiotic (Ciprofloxacin)',
                 'Antibiotic (Amoxicillin)', 'Antacid', 'ORS Packets', 'Antihistamine',
                 'Insulin', 'Aspirin (100mg)', 'Cough Syrup', 'Bandages (Roll)',
                 'Cotton Roll', 'Antiseptic Cream', 'Pain Relief Spray', 'Calamine Lotion',
                 'Vitamin C Tablets', 'Iron Supplements', 'Calcium Tablets', 'Antifungal Cream',
                 'Eye Drops', 'Ear Drops', 'Nasal Spray', 'First Aid Kit', 'Band-Aids']
    
    medicines_list = []
    for i in range(1, 501):
        medicine_name = random.choice(medicines)
        quantity = random.randint(50, 2000)
        expiry = datetime.now() + timedelta(days=random.randint(30, 730))
        camp_id = f"CAMP{random.randint(1, 100):03d}"
        
        medicines_list.append({
            'Medicine_ID': f'MED{i:04d}',
            'Medicine_Name': medicine_name,
            'Quantity': quantity,
            'Expiry_Date': expiry.strftime('%Y-%m-%d'),
            'Camp_ID': camp_id
        })
    
    return medicines_list


def save_to_csv(data, filename):
    """Save data to CSV file"""
    
    os.makedirs('data', exist_ok=True)
    filepath = f'data/{filename}'
    
    if not data:
        print(f"   Warning: No data to save for {filename}")
        return
    
    fieldnames = list(data[0].keys())
    
    with open(filepath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"   Saved {len(data)} records to {filepath}")


# MAIN EXECUTION

def main():
    """Generate all datasets"""
    
    print("\n" + "=" * 70)
    print(" SMART DISASTER RELIEF SYSTEM - DATA GENERATION")
    print("=" * 70)
    
    print("\nGenerating all datasets...\n")
    
    # 1. Disasters
    disasters = generate_disasters()
    save_to_csv(disasters, 'disasters.csv')
    
    # 2. Victims
    victims = generate_victims()
    save_to_csv(victims, 'victims.csv')
    
    # 3. Volunteers
    volunteers = generate_volunteers()
    save_to_csv(volunteers, 'volunteers.csv')
    
    # 4. Relief Camps
    camps = generate_relief_camps()
    save_to_csv(camps, 'relief_camps.csv')
    
    # 5. Food Inventory
    food = generate_food_inventory()
    save_to_csv(food, 'food_inventory.csv')
    
    # 6. Medicine Inventory
    medicine = generate_medicine_inventory()
    save_to_csv(medicine, 'medicine_inventory.csv')
    
    print("\n" + "=" * 70)
    print(" DATA GENERATION COMPLETE!")
    print("=" * 70)
    print("\nFiles created in 'data/' folder:")
    print("   1. disasters.csv       (50 records)")
    print("   2. victims.csv         (1,000 records)")
    print("   3. volunteers.csv      (200 records)")
    print("   4. relief_camps.csv    (100 records)")
    print("   5. food_inventory.csv  (500 records)")
    print("   6. medicine_inventory.csv (500 records)")
    print("\nNext: Run the main application!")
    print("=" * 70)


if __name__ == "__main__":
    main()