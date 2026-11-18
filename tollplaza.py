        ```python
import json
import os
from datetime import datetime

# ==========================================
# SMART HIGHWAY TOLL PLAZA SYSTEM
# ==========================================

DATA_FILE = "toll_data.json"

# Toll rates
TOLL_RATES = {
    "Car": 100,
    "Bike": 30,
    "Bus": 200,
    "Truck": 250,
    "Heavy Truck": 400,
    "Van": 120
}

# Global variables
total_vehicles_processed = 0
total_revenue_collected = 0.0
emergency_exemption_count = 0
vehicle_history = []


# ==========================================
# LOAD PREVIOUS DATA
# ==========================================

def load_data():

    global total_vehicles_processed
    global total_revenue_collected
    global emergency_exemption_count
    global vehicle_history

    if os.path.exists(DATA_FILE):

        try:
            with open(DATA_FILE, "r") as file:

                data = json.load(file)

                total_vehicles_processed = data.get(
                    "total_vehicles_processed", 0
                )

                total_revenue_collected = data.get(
                    "total_revenue_collected", 0.0
                )

                emergency_exemption_count = data.get(
                    "emergency_exemption_count", 0
                )

                vehicle_history = data.get(
                    "vehicle_history", []
                )

        except (json.JSONDecodeError, OSError):
            print("Previous data could not be loaded.")


# ==========================================
# SAVE DATA
# ==========================================

def save_data():

    data = {
        "total_vehicles_processed": total_vehicles_processed,
        "total_revenue_collected": total_revenue_collected,
        "emergency_exemption_count": emergency_exemption_count,
        "vehicle_history": vehicle_history
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ==========================================
# DISPLAY VEHICLE TYPES
# ==========================================

def display_vehicle_types():

    print("\n========== VEHICLE TYPES ==========")

    for vehicle, rate in TOLL_RATES.items():

        print(f"{vehicle:<15} Rs. {rate}")


# ==========================================
# PROCESS TOLL
# ==========================================

def process_toll():

    global total_vehicles_processed
    global total_revenue_collected
    global emergency_exemption_count

    print("\n========== PROCESS TOLL ==========")

    vehicle_number = input("Enter Vehicle Number: ").upper()

    if not vehicle_number.strip():
        print("Invalid vehicle number.")
        return

    print("\n1. Car")
    print("2. Bike")
    print("3. Bus")
    print("4. Truck")
    print("5. Heavy Truck")
    print("6. Van")

    choice = input("\nSelect Vehicle Type: ")

    vehicle_types = {
        "1": "Car",
        "2": "Bike",
        "3": "Bus",
        "4": "Truck",
        "5": "Heavy Truck",
        "6": "Van"
    }

    if choice not in vehicle_types:
        print("Invalid vehicle type.")
        return

    vehicle_type = vehicle_types[choice]

    print("\nIs this an emergency vehicle?")
    print("1. Yes")
    print("2. No")

    emergency = input("Enter choice: ")

    if emergency == "1":

        toll_amount = 0
        emergency_exemption_count += 1
        payment_method = "Exempted"

    elif emergency == "2":

        toll_amount = TOLL_RATES[vehicle_type]

        print("\nPayment Method")
        print("1. Cash")
        print("2. FASTag")

        payment_choice = input("Select Payment: ")

        if payment_choice == "1":
            payment_method = "Cash"

        elif payment_choice == "2":
            payment_method = "FASTag"

            # FASTag discount
            toll_amount *= 0.90

        else:
            print("Invalid payment method.")
            return

    else:
        print("Invalid choice.")
        return

    total_vehicles_processed += 1
    total_revenue_collected += toll_amount

    transaction = {

        "vehicle_number": vehicle_number,
        "vehicle_type": vehicle_type,
        "toll_amount": toll_amount,
        "payment_method": payment_method,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "time": datetime.now().strftime("%H:%M:%S")

    }

    vehicle_history.append(transaction)

    save_data()

    print("\n========== TOLL RECEIPT ==========")

    print("Vehicle Number :", vehicle_number)
    print("Vehicle Type   :", vehicle_type)
    print("Payment Method :", payment_method)
    print("Toll Amount    : Rs.", round(toll_amount, 2))

    print("Date           :", transaction["date"])
    print("Time           :", transaction["time"])

    print("==================================")


# ==========================================
# REVENUE REPORT
# ==========================================

def revenue_report():

    print("\n========== REVENUE REPORT ==========")

    print("Total Vehicles Processed :", total_vehicles_processed)

    print("Total Revenue Collected  : Rs.",
          round(total_revenue_collected, 2))

    print("Emergency Exemptions     :", emergency_exemption_count)

    print("\nAverage Revenue Per Vehicle:")

    if total_vehicles_processed > 0:

        average = total_revenue_collected / total_vehicles_processed

        print("Rs.", round(average, 2))

    else:
        print("No vehicles processed yet.")


# ==========================================
# VEHICLE HISTORY
# ==========================================

def show_vehicle_history():

    print("\n========== VEHICLE HISTORY ==========")

    if len(vehicle_history) == 0:

        print("No vehicle records found.")
        return

    for index, vehicle in enumerate(vehicle_history, start=1):

        print(f"\nTransaction {index}")

        print("Vehicle Number :", vehicle["vehicle_number"])
        print("Vehicle Type   :", vehicle["vehicle_type"])
        print("Toll Amount    :", vehicle["toll_amount"])
        print("Payment Method :", vehicle["payment_method"])
        print("Date           :", vehicle["date"])
        print("Time           :", vehicle["time"])


# ==========================================
# SEARCH VEHICLE
# ==========================================

def search_vehicle():

    print("\n========== SEARCH VEHICLE ==========")

    number = input("Enter Vehicle Number: ").upper()

    found = False

    for vehicle in vehicle_history:

        if vehicle["vehicle_number"] == number:

            print("\nVehicle Found!")

            print("Vehicle Number :", vehicle["vehicle_number"])
            print("Vehicle Type   :", vehicle["vehicle_type"])
            print("Toll Amount    :", vehicle["toll_amount"])
            print("Payment Method :", vehicle["payment_method"])
            print("Date           :", vehicle["date"])

            found = True

    if not found:
        print("Vehicle record not found.")


# ==========================================
# RESET SHIFT
# ==========================================

def reset_shift():

    global total_vehicles_processed
    global total_revenue_collected
    global emergency_exemption_count
    global vehicle_history

    print("\n========== RESET SHIFT ==========")

    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":

        total_vehicles_processed = 0
        total_revenue_collected = 0.0
        emergency_exemption_count = 0
        vehicle_history = []

        save_data()

        print("Shift successfully reset!")

    else:
        print("Reset cancelled.")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    load_data()

    while True:

        print("\n")
        print("=" * 45)
        print("       SMART HIGHWAY TOLL PLAZA")
        print("          TRAFFIC BILLING SYSTEM")
        print("=" * 45)

        print("\n1. Process Toll")
        print("2. Display Toll Rates")
        print("3. Revenue Report")
        print("4. Vehicle History")
        print("5. Search Vehicle")
        print("6. Reset Shift")
        print("7. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":

            process_toll()

        elif choice == "2":

            display_vehicle_types()

        elif choice == "3":

            revenue_report()

        elif choice == "4":

            show_vehicle_history()

        elif choice == "5":

            search_vehicle()

        elif choice == "6":

            reset_shift()

        elif choice == "7":

            save_data()

            print("\nThank you for using Smart Highway Toll Plaza!")
            print("System shutting down...")

            break

        else:

            print("Invalid choice! Please try again.")


# ==========================================
# PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":

    main()
```