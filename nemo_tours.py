#*********************************************************************************************************************
# Name: Trung Hieu HUYNH
# ID: 12281833
# Project name: Nemo Reef Tours Program
# 
#*********************************************************************************************************************
# Question:
# 1. Cac bien nen duoc khai bao theo dinh dang nao: camel hay ...
# 2.
# 3. 
#*********************************************************************************************************************

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
TEN_PERCENT_DISCOUNT = 10
FIFTEEN_PERCENT_DISCOUNT = 15
TWENTY_PERCENT_DISCOUNT = 20
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
        num_str = input("Enter the number of passengers for '" + booking_name + "' ==> ")
        if num_str != "":
            is_valid = True
            for ch in num_str:
                if ch < '0' or ch > '9':
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
        charge *= (1 - TWENTY_PERCENT_DISCOUNT / 100)
    elif passengers >= 6:
        charge *= (1 - FIFTEEN_PERCENT_DISCOUNT / 100)
    elif passengers >= 3:
        charge *= (1 - TEN_PERCENT_DISCOUNT / 100)
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
    global number_of_bookings

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
    print_heading()

    # TODO -- check if there has been an booking entered (do this after getting the other functionality working)

	# TODO -- display all of the entries entered so far as per the specification

    pass

#----------------------------------------------------------
# Function 3
#----------------------------------------------------------
def display_statistics():    
    # TODO -- check if there has been an booking entered (do this after getting the other functionality working)

    # TODO -- loop though the current entries in the lists and calculate and display the statistics
    
    pass

#----------------------------------------------------------
# Function 4
#----------------------------------------------------------
def search_bookings():
    # TODO -- check if there has been an booking entered (do this after getting the other functionality working)

    # TODO -- read the search key

    # TODO -- loop though the current entries in the booking names list to search for the search key

    # TODO -- display the found item or report it has not been found

    pass

#----------------------------------------------------------
# Function 5
#----------------------------------------------------------
def save_bookings():
    # TODO -- save the entries as a csv (comma seperated file) in the current folder called bookings.csv
    pass

#----------------------------------------------------------
# Function 6
#----------------------------------------------------------
def read_bookings():
    # TODO -- check if the file exists

    # TODO -- read the entries and add them to the parallel lists

    pass    


#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
print("Welcome to the Nemo Reef Tours Management System")
process_menu_item() 

#-----------------------------------------------------------------------------
# End
#-----------------------------------------------------------------------------
