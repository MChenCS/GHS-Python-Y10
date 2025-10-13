
from datetime import date

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

def add_addons(base_price, number_of_guests, length_of_stay):
    """
    Captures and adds optional addons to the base price.
    """
    total_addon_price = 0
    # For each addon option, ask user if they want it, and calculate price accordingly
    for addon in ROOM_ADDONS:
        print(f"You can add {addon} for {pretty_print_currency(ROOM_ADDONS[addon]['price'])} {'per person' if ROOM_ADDONS[addon]['per_person'] else ''} {'per night' if ROOM_ADDONS[addon]['per_night'] else ''}")
        choice = input(f"Would you like to add {addon}? (yes/no): ").strip().lower()
        if choice == 'yes':
            addon_price = ROOM_ADDONS[addon]['price']
            if ROOM_ADDONS[addon]['per_person']:
                addon_price *= number_of_guests
            if ROOM_ADDONS[addon]['per_night']:
                addon_price *= length_of_stay
            total_addon_price += addon_price
    return base_price + total_addon_price

if __name__ == "__main__":
    # Capture check-in, check-out dates as strings
    check_in_date_str = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date_str = input("Enter check-out date (YYYY-MM-DD): ")
    number_of_guests = input("Enter number of guests: ")
    # Capture and check number of guests
    while not number_of_guests.isdigit() or int(number_of_guests) <= 0:
        print("Please enter a valid positive integer for number of guests.")
        number_of_guests = input("Enter number of guests: ")
    number_of_guests = int(number_of_guests)
    # Use calculate_dates function to calculate length of stay, also check-in, check-out strings to date objects
    check_in_date, check_out_date, length_of_stay = calculate_dates(check_in_date_str, check_out_date_str)
    # Check if exist, meaning dates were valid
    if check_in_date and check_out_date:
        print(f"Check-in Date: {check_in_date}")
        print(f"Check-out Date: {check_out_date}")
        print(f"Length of Stay: {length_of_stay} days")
        # Capture room type and calculate total price, validation is done in calculate_price function
        room_type = input(f"Enter room type ({', '.join(ROOM_DATA.keys())}): ").strip().lower()
        total_price = calculate_price(room_type, length_of_stay)
        # Add addons to total price
        if total_price is not None:
            total_price = add_addons(total_price, number_of_guests, length_of_stay)
        # Display results
        if total_price is not None:
            print(f"Total Price for {length_of_stay} days in a {room_type} room: {pretty_print_currency(total_price, CURRENCY)}")
        else:
            print("Could not calculate total price due to invalid input.")