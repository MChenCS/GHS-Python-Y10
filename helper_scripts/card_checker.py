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

def is_valid_credit_card(number):
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