def get_card_type(number):
    """
    Determine the credit card type: Amex, Visa, or Mastercard.

    Args:
        number (str): The credit card number as a string.

    Returns:
        str: 'Amex', 'Visa', 'Mastercard', or 'Unknown'
    """
    # Remove spaces and hyphens from the input number
    number = number.replace(' ', '').replace('-', '')
    # Check if the cleaned number contains only digits
    if not number.isdigit():
        return 'Unknown'

    # Check for American Express (Amex): length 15, starts with 34 or 37
    if len(number) == 15 and (number.startswith('34') or number.startswith('37')):
        return 'Amex'
    # Check for Visa: length 13, 16, or 19, starts with 4
    elif len(number) in [13, 16, 19] and number.startswith('4'):
        return 'Visa'
    # Check for Mastercard: length 16, starts with 51-55 or 2221-2720
    elif len(number) == 16 and (
        51 <= int(number[:2]) <= 55 or
        2221 <= int(number[:4]) <= 2720
    ):
        return 'Mastercard'
    # If none match, return 'Unknown'
    else:
        return 'Unknown'

def is_valid_card(number):
    """
    Check if the given number is a valid credit card number using the Luhn algorithm.

    Args:
        number (str): The credit card number as a string.

    Returns:
        str: 'Amex', 'Visa', 'Mastercard', or 'Unknown'
    """
    # Remove spaces and hyphens from the input number
    number = number.replace(' ', '').replace('-', '')
    # Check if the cleaned number contains only digits
    if not number.isdigit():
        return "Unknown"

    # Get the card type using the get_card_type function
    card_type = get_card_type(number)
    # If card type is unknown, return 'Unknown'
    if card_type == 'Unknown':
        return "Unknown"

    # Implement the Luhn algorithm to validate the card number
    total = 0
    # Reverse the digits for processing
    reverse_digits = number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        # Double every second digit (i.e., digits at odd indices)
        if i % 2 == 1:
            n *= 2
            # If doubling results in a number > 9, subtract 9
            if n > 9:
                n -= 9
        # Add the processed digit to the total
        total += n
        # If the running total is divisible by 10, the card is valid
        if total % 10 == 0:
            return card_type
    # If not valid, return 'Unknown'
    return "Unknown"

def is_valid_expiry(month, year):
    """
    Check if the given expiry date is valid (not in the past).

    Args:
        month (int): The expiry month (1-12).
        year (int): The expiry year (four digits).

    Returns:
        bool: True if the expiry date is valid, False otherwise.
    """
    from datetime import datetime

    # Get the current date
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # Check if the year is in the past
    if year < current_year:
        return False
    # If the year is the current year, check the month
    elif year == current_year and month < current_month:
        return False
    # If the month is not between 1 and 12, it's invalid
    elif month < 1 or month > 12:
        return False
    # Otherwise, the expiry date is valid
    return True

def is_valid_cvc(cvc, card_type):
    """
    Check if the given CVC is valid based on the card type.

    Args:
        cvc (str): The CVC code as a string.
        card_type (str): The type of the card ('Amex', 'Visa', 'Mastercard').

    Returns:
        bool: True if the CVC is valid, False otherwise.
    """
    # CVC must be all digits
    if not cvc.isdigit():
        return False
    # American Express cards have a 4-digit CVC
    if card_type == 'Amex':
        return len(cvc) == 4
    # Visa and Mastercard have a 3-digit CVC
    elif card_type in ['Visa', 'Mastercard']:
        return len(cvc) == 3
    # Other card types are not supported
    else:
        return False