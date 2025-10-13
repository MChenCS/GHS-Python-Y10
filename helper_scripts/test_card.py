import card_checker as cc
from datetime import datetime

def test_get_card_type():
    tests = [
        ('340000100669947', 'Amex'),
        ('371449635398431', 'Amex'),
        ('4111111111111111', 'Visa'),
        ('4012888888881881', 'Visa'),
        ('4222222222222', 'Visa'),
        ('5555555555554444', 'Mastercard'),
        ('5105105105105100', 'Mastercard'),
        ('2221000000000009', 'Mastercard'),
        ('2720992711111111', 'Mastercard'),
        ('1234567890123456', 'Unknown'),
        ('abcd4111111111111', 'Unknown'),
        ('', 'Unknown'),
    ]
    print("Testing get_card_type...")
    for number, expected in tests:
        result = cc.get_card_type(number)
        print(f"  get_card_type('{number}') == '{result}' (expected: '{expected}')", "PASS" if result == expected else "FAIL")

def test_is_valid_card():
    tests = [
        ('378282246310005', 'Amex'),
        ('371449635398431', 'Amex'),
        ('4111111111111111', 'Visa'),
        ('4012888888881881', 'Visa'),
        ('4222222222222', 'Visa'),
        ('5555555555554444', 'Mastercard'),
        ('5105105105105100', 'Mastercard'),
        ('2221000000000009', 'Mastercard'),
        ('2720992711111111', 'Mastercard'),
        ('1234567890123456', 'Unknown'),
        ('abcd4111111111111', 'Unknown'),
        ('', 'Unknown'),
    ]
    print("Testing is_valid_card...")
    for number, expected in tests:
        result = cc.is_valid_card(number)
        print(f"  is_valid_card('{number}') == '{result}' (expected: '{expected}')", "PASS" if result == expected else "FAIL")

def test_is_valid_expiry():
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    tests = [
        (current_month, current_year, True),
        ((current_month % 12) + 1, current_year + (1 if current_month == 12 else 0), True),
        (current_month - 1 if current_month > 1 else 12, current_year if current_month > 1 else current_year - 1, False),
        (0, current_year, False),
        (13, current_year, False),
        (current_month, current_year - 1, False),
    ]
    print("Testing is_valid_expiry...")
    for month, year, expected in tests:
        result = cc.is_valid_expiry(month, year)
        print(f"  is_valid_expiry({month}, {year}) == {result} (expected: {expected})", "PASS" if result == expected else "FAIL")

def test_is_valid_cvc():
    tests = [
        ('1234', 'Amex', True),
        ('123', 'Amex', False),
        ('123', 'Visa', True),
        ('12a', 'Visa', False),
        ('123', 'Mastercard', True),
        ('1234', 'Mastercard', False),
        ('123', 'Unknown', False),
    ]
    print("Testing is_valid_cvc...")
    for cvc, card_type, expected in tests:
        result = cc.is_valid_cvc(cvc, card_type)
        print(f"  is_valid_cvc('{cvc}', '{card_type}') == {result} (expected: {expected})", "PASS" if result == expected else "FAIL")

if __name__ == "__main__":
    test_get_card_type()
    print()
    test_is_valid_card()
    print()
    test_is_valid_expiry()
    print()
    test_is_valid_cvc()