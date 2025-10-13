from datetime import date

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

if __name__ == "__main__":
    check_in_date_str = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date_str = input("Enter check-out date (YYYY-MM-DD): ")
    check_in_date, check_out_date, length_of_stay = calculate_dates(check_in_date_str, check_out_date_str)
    if check_in_date and check_out_date:
        print(f"Check-in Date: {check_in_date}")
        print(f"Check-out Date: {check_out_date}")
        print(f"Length of Stay: {length_of_stay} days")