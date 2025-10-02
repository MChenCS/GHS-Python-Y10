def is_valid_email(email):
    # Check for spaces
    if ' ' in email:
        return False

    # Check for exactly one '@'
    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    # Local part must not be empty and should be at least 1 character
    if len(local) < 1:
        return False

    # Domain part must contain at least one dot
    if '.' not in domain:
        return False

    # Dot must not be at the start or end of the domain
    if domain.startswith('.') or domain.endswith('.'):
        return False

    # Each part of the domain (split by dot) must not be empty
    domain_parts = domain.split('.')
    if any(len(part) == 0 for part in domain_parts):
        return False

    return True

if __name__ == "__main__":
    email = input("Enter an email address: ").strip()
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")