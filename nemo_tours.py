#*********************************************************************************************************************
# Name: Trung Hieu HUYNH
# ID: 12281833
# Project name: Nemo Reef Tours Program
# 
#*********************************************************************************************************************
# Question:
# 1. Cac bien nen duoc khai bao theo dinh dang nao: camel hay ...
# 2. func 4:
#           #ERR: sẽ ra sau nếu người dùng nhập dư khoảng trắng trước/sau tên
# 3. 
#*********************************************************************************************************************

import csv # For function 5: save_bookings()
import os # For function 6: read_bookings()

#-----------------------------------------------------------------------------
# Constants Declaration
#-----------------------------------------------------------------------------
ENTER_BOOKING = 1
DISPLAY_BOOKINGS = 2
DISPLAY_STATISTICS = 3
SEARCH_BOOKINGS = 4
SAVE_BOOKINGS = 5
READ_BOOKINGS = 6
EXIT = 7

# Declare any further constants
PASSENGER_CHARGE = 95.50

TEN_PERCENT_DISCOUNT = 0.1         #10% discount for a booking with three to five passengers
FIFTEEN_PERCENT_DISCOUNT = 0.15    #15% discount for a booking of more than six to ten passengers
TWENTY_PERCENT_DISCOUNT = 0.2      #20% discount for more than ten passengers on the total charge

#-----------------------------------------------------------------------------
# Declare two lists, one for the booking names and another for the number of passengers
booking_names = []
booking_passengers = []

# Declare variable for the number of bookings entered (integer)
number_of_bookings = 0

#-----------------------------------------------------------------------------
# Function Definition
#-----------------------------------------------------------------------------
def print_heading():
    print("{:30s}{:11s}{:6s}".format("Booking name","Passengers", "Charge"))

def get_menu_item():
    print("\nPlease select from the following")
    print(str(ENTER_BOOKING) + ". Enter booking name and number of passengers")
    print(str(DISPLAY_BOOKINGS) + ". Display all booking names, number of passengers and charges")
    print(str(DISPLAY_STATISTICS) + ". Display Statistics")
    print(str(SEARCH_BOOKINGS) + ". Search for booking")
    print(str(SAVE_BOOKINGS) + ". Save bookings to file")
    print(str(READ_BOOKINGS) + ". Read bookings from file")
    print(str(EXIT) + ". Exit the application")
    print("Enter choice==> ", end = " ")
    choice = input()
    while  not choice.isdigit():
        print("Error - Menu selection name cannot be blank and must be numeric")
        print("Enter choice==> ", end = " ")
        choice = input()

    return int(choice)

def process_menu_item():
    choice = get_menu_item()
    while choice != EXIT:
        if choice == ENTER_BOOKING:
            enter_booking()
        elif choice == DISPLAY_BOOKINGS:
            display_bookings()
        elif choice == DISPLAY_STATISTICS:
            display_statistics()
        elif choice == SEARCH_BOOKINGS:
            search_bookings()
        elif choice == SAVE_BOOKINGS:
            save_bookings()
        elif choice == READ_BOOKINGS:
            read_bookings()
        choice = get_menu_item()

#--------------------------------------
# Sub_function 1:
#--------------------------------------
def get_booking_name():
    booking_name = input("Please enter the booking name ==> ")
    while booking_name == "":
        print("ERROR: booking name cannot be blank.")
        booking_name = input("Please enter the booking name ==> ")
    return booking_name


#--------------------------------------
# Sub_function 2:
#--------------------------------------
def get_number_of_passenger(booking_name):
    while True:
        num_str = input("Enter the number of passengers for "" + booking_name + "" ==> ")
        if num_str != "":
            is_valid = True
            for ch in num_str:
                if ch < "0" or ch > "9":
                    is_valid = False
                    break
                
            if is_valid:
                num = int(num_str)
                if num >= 1:
                    return num
        print("ERROR: must be numeric and number of passengers must be greater than or equal to one")


#--------------------------------------
#Sub_function 3:
#--------------------------------------
def calculate_charge(passengers):
    charge = passengers * PASSENGER_CHARGE
    if passengers >= 11:
        charge = charge*(1 - TWENTY_PERCENT_DISCOUNT)
    elif passengers >= 6:
        charge = charge*(1 - FIFTEEN_PERCENT_DISCOUNT)
    elif passengers >= 3:
        charge = charge*(1 - TEN_PERCENT_DISCOUNT)
    return charge


#--------------------------------------
#Sub_function 4: Print receipt
#--------------------------------------
def print_receipt(name, passengers, charge):
    print("\n---Nemo Tours Receipt---")
    print("Booking name: ",name)
    print("Number of passenger: ",passengers)
    print("Total charge: " + "$" + format(charge, ".2f"))

#----------------------------------------------------------
# Function 1:
#----------------------------------------------------------
def enter_booking():
    global number_of_bookings # ERR???? re-define????

    # Calling "Sub_function 1" - get_booking_name: to read in the booking name (as a string)
    booking_name = get_booking_name()
    
    # Calling "Sub_function 2" - get_number_of_passenger: to read in the number of passengers
    passengers = get_number_of_passenger(booking_name)

    # Calling "Sub_function 3" - calculate_charge: to calculate the charge
    charge = calculate_charge(passengers)

    # Add the booking name and the number of passengers to the parallel lists
    booking_names.append(booking_name)
    booking_passengers.append(passengers)

    # Increment the number of bookings variable
    number_of_bookings += 1

    # Calling "Sub_function 4" -  print_receipt: to print the receipt
    print_receipt(booking_name, passengers, charge)

#----------------------------------------------------------
# Function 2:
#----------------------------------------------------------
def display_bookings():
    # Check if there has been an booking entered (do this after getting the other functionality working)
    if number_of_bookings == 0:
        print("ERROR: Please enter at least one booking")
        return
    else: 
        print_heading()
        # Display all of the entries entered so far as per the specification
        # Loop all the booking names and passengers
        for i in range(number_of_bookings):
            # Calculate the charge for each booking using the calculate_charge function
            charge = calculate_charge(booking_passengers[i])

            # Display each booking's details in the specified format
            print("{:30s}{:<11d}${:4.2f}".format(booking_names[i], booking_passengers[i], charge))

#----------------------------------------------------------
# Function 3
#----------------------------------------------------------
def display_statistics():    
    # Check if there has been an booking entered (do this after getting the other functionality working)
    if number_of_bookings == 0:
        print("ERROR: Please enter at least one booking")
        return
    else:
        # Initialize variables for tracking statistics
        min_passenger = booking_passengers[0]
        max_passenger = booking_passengers[0]
        min_booking_name = booking_names[0]
        max_booking_name = booking_names[0]
        
        total_passengers = 0
        total_charge = 0.0
        
        # Loop though the current entries in the lists and calculate and display the statistics
        for i in range(number_of_bookings):
            passengers = booking_passengers[i]
            charge = calculate_charge(passengers)
            
            # Update total passengers and charges
            total_passengers += passengers
            total_charge += charge
            
            # Update min and max passenger count and corresponding booking names
            if passengers < min_passenger:
                min_passenger = passengers
                min_booking_name = booking_names[i]
            if passengers > max_passenger:
                max_passenger = passengers
                max_booking_name = booking_names[i]
                
            # Calculate average number of passengers
            # Ensure floating-point division
            average_passengers = total_passengers / number_of_bookings
            
            # Display the statistics info
            print("\nStatistics for Nemo Tours  ")
            print(f"{max_booking_name} has the maximum number of {max_passenger} passengers")
            print(f"{min_booking_name} has the minimum number of {min_passenger} passengers")
            print(f"Average number of passengers per booking is {average_passengers:.2f}")
            print(f"The total charges are: ${total_charge:.2f}")
            

#----------------------------------------------------------
# Function 4
#----------------------------------------------------------
def search_bookings():
    # Check if there has been an booking entered (do this after getting the other functionality working)
    if number_of_bookings == 0:
        print("ERROR: Please enter at least one booking")
        return
    else:
        # Read the search key
        search_name = input("Please enter the booking name ==> ")
        
        # Perform a case-insensitive search in the booking names list
        found = False  # Flag to check if the booking is found
        
        # Loop though the current entries in the booking names list to search for the search key
        for i in range(number_of_bookings):
            # Compare the lowercase versions of the booking name
            if search_name.lower() == booking_names[i].lower():
                # Calculate the charge for each booking using the calculate_charge function
                charge = calculate_charge(booking_passengers[i])
                
                # Display the found item or report it has not been found
                print_heading()
                print("{:30s}{:<11d}${:4.2f}".format(booking_names[i], booking_passengers[i], charge))
                found = True
                break
        if not found:
            print(f"{search_name} not found")
#----------------------------------------------------------
# Function 5
#----------------------------------------------------------
def save_bookings():
    if number_of_bookings == 0:
        print("ERROR: Please enter at least one booking")
        return
    else:
        # Save the entries as a csv (comma seperated file) in the current folder called bookings.csv
        # Open the bookings.csv file with write mode ("w"), will overwrite if the file already exists
        with open("bookings.csv", "w", newline="") as file:
            writer = csv.writer(file)

            # Write title (optional)
            writer.writerow(["Booking Name", "Passengers"])

            # Write each booking data line (passenger name and number)    
            for i in range(number_of_bookings):
                writer.writerow([booking_names[i], booking_passengers[i]])

    print("Data successfully saved to file")

#----------------------------------------------------------
# Function 6
#----------------------------------------------------------
def read_bookings():
    # Check if the file exists
    # Read the entries and add them to the parallel lists
    # Check Check if the file exists (bookings.csv file)
    if not os.path.exists("./bookings.csv"):
        print("ERROR - file does not exist")
        return
    
    # Open the bookings.csv file and read the data from it
    with open("bookings.csv", "r") as file:
        # Skip the header line if present
        next(file)

        # Iterate through each line in the file and split the values
        for line in file:
            # Split the booking name and passenger number from each line
            booking_name, passengers = line.strip().split(",")
            booking_names.append(booking_name)
            booking_passengers.append(int(passengers)) # Convert the passenger number to int
    
    # Update the number of bookings
    global number_of_bookings
    number_of_bookings = len(booking_names)

    print("Data successfully read from the file")
    print(f"Loaded {number_of_bookings} bookings.")  # Check have many bookings have been read


#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
print("Welcome to the Nemo Reef Tours Management System")
process_menu_item() 

#-----------------------------------------------------------------------------
# End
#-----------------------------------------------------------------------------
