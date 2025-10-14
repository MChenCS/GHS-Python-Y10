import card_checker
from datetime import date
import random

# Fixed constants
ROOM_DATA = {
    "studio": {"price":1100, "max_occupancy":2, "room_number_range":[(101,130), (201,230)]},
    "family": {"price":1800, "max_occupancy":5, "room_number_range":[(131,140), (231,240)]},
    "premium": {"price":1800, "max_occupancy":3, "room_number_range":[(301,320)]},
    "rooftop": {"price":2400, "max_occupancy":4, "room_number_range":[(401,410)]}
}
ROOM_ADDONS = {
    "breakfast": {"price": 400, "per_person": True, "per_night": True},
    "parking": {"price": 800, "per_person": False, "per_night": True},
    "pet_access": {"price": 1000, "per_person": False, "per_night": False}
}
CURRENCY = "SEK"

def calculate_dates(check_in_date_string=None, check_out_date_string=None):
    """
    Captures check-in and check-out dates from user input in YYYY-MM-DD format.
    Returns a tuple of two date objects (check_in_date, check_out_date).
    """
    today = date.today()
    # Test if date strings are valid dates in correct format
    try:
        check_in_date = date.fromisoformat(check_in_date_string)
        check_out_date = date.fromisoformat(check_out_date_string)
        length_of_stay = (check_out_date - check_in_date).days
    # If not, return None three times
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None, None, None
    # Test if check-in date is today or later, and check-out date is after check-in date
    if check_in_date < today or check_out_date <= check_in_date:
        print("Check-in date must be today or later, and check-out date must be after check-in date.")
        return None, None, None
    # If all tests passed, return the valid dates and length of stay
    return check_in_date, check_out_date, length_of_stay

def calculate_price(room_type, length_of_stay):
    """
    Calculates the total price for a given room type and length of stay.
    """
    # Case where room type is not found
    if room_type not in ROOM_DATA:
        print(f"Invalid room type. Available types: {', '.join(ROOM_DATA.keys())}")
        return None
    # Case where length of stay is not a positive integer
    if length_of_stay <= 0:
        print("Length of stay must be a positive integer.")
        return None
    # Otherwise, retrieve room price and calculate total
    price_per_night = ROOM_DATA[room_type]["price"]
    total_price = price_per_night * length_of_stay
    return total_price

def pretty_print_currency(amount, currency=CURRENCY):
    """
    Formats the amount as a currency string.
    """
    return f"{currency} {amount:,.2f}"

def add_addons(number_of_guests, length_of_stay):
    """
    Captures and adds optional addons to the base price.
    """
    total_addon_price = 0
    # For each addon option, ask user if they want it, and calculate price accordingly
    for addon in ROOM_ADDONS:
        print(f"You can add {addon} for {pretty_print_currency(ROOM_ADDONS[addon]['price'])} {'per person' if ROOM_ADDONS[addon]['per_person'] else ''} {'per night' if ROOM_ADDONS[addon]['per_night'] else ''} {'per stay' if not ROOM_ADDONS[addon]['per_night'] and not ROOM_ADDONS[addon]['per_person'] else ''}")
        choice = input(f"Would you like to add {addon}? (yes/no): ").strip().lower()
        while choice != "yes" and choice != "no":
            print("Please answer 'yes' or 'no'.")
            choice = input(f"Would you like to add {addon}? (yes/no): ").strip().lower()
        if choice == 'yes':
            addon_price = ROOM_ADDONS[addon]['price']
            if ROOM_ADDONS[addon]['per_person']:
                addon_price *= number_of_guests
            if ROOM_ADDONS[addon]['per_night']:
                addon_price *= length_of_stay
            total_addon_price += addon_price
    return total_addon_price

def find_available_rooms(number_of_guests):
    """
    Displays available room types based on the number of guests.
    """
    available_rooms = [room for room, data in ROOM_DATA.items() if data["max_occupancy"] >= number_of_guests]
    if available_rooms:
        print(f"Available room types for {number_of_guests} guests:")
        for room in available_rooms:
            print(f"- {room.capitalize()} ({pretty_print_currency(ROOM_DATA[room]['price'])} per night)")
    else:
        print("No rooms available for the specified number of guests.")
    return available_rooms

def generate_room_number(room_type):
    """
    Generates a random room number based on the room type.
    """
    if room_type not in ROOM_DATA:
        print(f"Invalid room type. Available types: {', '.join(ROOM_DATA.keys())}")
        return None
    room_ranges = ROOM_DATA[room_type]["room_number_range"]
    selected_range = random.choice(room_ranges)
    return random.randint(selected_range[0], selected_range[1])

if __name__ == "__main__":
    # Capture check-in, check-out dates as strings, convert to date objects and calculate length of stay
    check_in_date_str = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date_str = input("Enter check-out date (YYYY-MM-DD): ")
    check_in_date, check_out_date, length_of_stay = calculate_dates(check_in_date_str, check_out_date_str)

    while not check_in_date or not check_out_date:
        check_in_date_str = input("Enter check-in date (YYYY-MM-DD): ")
        check_out_date_str = input("Enter check-out date (YYYY-MM-DD): ")
        check_in_date, check_out_date, length_of_stay = calculate_dates(check_in_date_str, check_out_date_str)
    
    # Capture and check number of guests
    number_of_guests = input("Enter number of guests: ")
    while not number_of_guests.isdigit() or int(number_of_guests) <= 0:
        print("Please enter a valid positive integer for number of guests.")
        number_of_guests = input("Enter number of guests: ")
    number_of_guests = int(number_of_guests)

    # Find available rooms based on number of guests
    available_rooms = find_available_rooms(number_of_guests)
    while not available_rooms:
        number_of_guests = input("Enter a different number of guests: ")
        while not number_of_guests.isdigit() or int(number_of_guests) <= 0:
            print("Please enter a valid positive integer for number of guests.")
            number_of_guests = input("Enter number of guests: ")
        number_of_guests = int(number_of_guests)
        available_rooms = find_available_rooms(number_of_guests)

    # Capture room type and check if selected room type is available
    room_type = input(f"Enter room type: ").strip().lower()
    while room_type not in available_rooms:
        print(f"Selected room type '{room_type}' is not available for {number_of_guests} guests.")
        room_type = input(f"Enter room type ({', '.join(available_rooms)}): ").strip().lower()
    
    # Calculate base price, assuming room types & length of stay checks out
    total_price = calculate_price(room_type, length_of_stay)

    # Add addons to price
    total_price = total_price + add_addons(number_of_guests, length_of_stay)
        
    # Display results
    if total_price is not None:
        print(f"Total Price for your {length_of_stay} night stay is {pretty_print_currency(total_price, CURRENCY)}")
    else:
        print("Could not calculate total price due to invalid input.")

    # Check if card number is valid and obtain card type
    card_number = input("Enter your card number (no spaces): ").strip()
    card_type = card_checker.get_card_type(card_number)
    while card_checker.is_valid_card(card_number) == "Unknown":
        print("Invalid card number. Please try again.")
        card_number = input("Enter your card number (no spaces): ").strip()
        card_type = card_checker.get_card_type(card_number)
    
    # Check if expiry date is valid (input only)
    card_expiry_month = input("Enter card expiry month (MM): ").strip()
    card_expiry_year = input("Enter card expiry year (YYYY): ").strip()
    while not card_expiry_month.isdigit() or not card_expiry_year.isdigit() or not card_checker.is_valid_expiry(int(card_expiry_month), int(card_expiry_year)):
        print("Invalid expiry date. Please try again.")
        card_expiry_month = input("Enter card expiry month (MM): ").strip()
        card_expiry_year = input("Enter card expiry year (YYYY): ").strip()
    card_expiry_month = int(card_expiry_month)
    card_expiry_year = int(card_expiry_year)

    # Check if expiry date is valid (function)
    while not card_checker.is_valid_expiry(card_expiry_month, card_expiry_year):
        print("Invalid expiry date. Please try again.")
        card_expiry_month = input("Enter card expiry month (MM): ").strip()
        card_expiry_year = input("Enter card expiry year (YYYY): ").strip()
        while not card_expiry_month.isdigit() or not card_expiry_year.isdigit():
            print("Please enter numeric values for month and year.")
            card_expiry_month = input("Enter card expiry month (MM): ").strip()
            card_expiry_year = input("Enter card expiry year (YYYY): ").strip()
        card_expiry_month = int(card_expiry_month)
        card_expiry_year = int(card_expiry_year)

    # Check if CVC is valid
    card_cvc = input("Enter card CVC: ").strip()
    while not card_checker.is_valid_cvc(card_cvc, card_type):
        print("Invalid CVC. Please try again.")
        card_cvc = input("Enter card CVC: ").strip()
    
    print(f"Payment successful with {card_type} card ending in {card_number[-4:]}. Thank you for your booking!")

    # Generate and display room number
    room_number = generate_room_number(room_type)
    if room_number:
        print(f"Your room number is {room_number}. Enjoy your stay!")