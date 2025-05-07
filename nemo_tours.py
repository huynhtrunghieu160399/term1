# TODO -- create header comments

ENTER_BOOKING = 1
DISPLAY_BOOKINGS = 2
DISPLAY_STATISTICS = 3
SEARCH_BOOKINGS = 4
SAVE_BOOKINGS = 5
READ_BOOKINGS = 6
EXIT = 7

# TODO -- declare any further constants

# TODO -- declare two lists one for the booking names and another for the number of passengers
# TODO -- declare variable for the number of bookings entered (integer)


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


def enter_booking():
    # TODO -- read in the booking name (as a string)
	# TODO -- create validation loop (do this after getting the other functionality working)

	# TODO -- read in the number of passengers
	# TODO -- create validation loop (do this after getting the other functionality working)

	# TODO -- add the booking name and the number of passengers to the parallel lists
    
	# TODO -- display the booking name, number of passengers and the charge as a receipt as per the specification

    # TODO -- increment the number of bookings variable

    pass

def display_bookings():
    print_heading()

    # TODO -- check if there has been an booking entered (do this after getting the other functionality working)

	# TODO -- display all of the entries entered so far as per the specification

    pass

def display_statistics():    
    # TODO -- check if there has been an booking entered (do this after getting the other functionality working)

    # TODO -- loop though the current entries in the lists and calculate and display the statistics
    
    pass

def search_bookings():
    # TODO -- check if there has been an booking entered (do this after getting the other functionality working)

    # TODO -- read the search key

    # TODO -- loop though the current entries in the booking names list to search for the search key

    # TODO -- display the found item or report it has not been found

    pass

def save_bookings():
    # TODO -- save the entries as a csv (comma seperated file) in the current folder called bookings.csv
    pass

def read_bookings():
    # TODO -- check if the file exists

    # TODO -- read the entries and add them to the parallel lists

    pass    

print("Welcome to the Nemo Reef Tours Management System")
process_menu_item() 
