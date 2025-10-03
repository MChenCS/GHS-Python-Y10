def is_valid_password(password):
    if len(password) < 8:
        return False
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    return has_lower and has_upper

def main():
    print("Password Reset Program")
    while True:
        pwd1 = input("Enter new password: ")
        pwd2 = input("Re-enter new password: ")
        if pwd1 != pwd2:
            print("Passwords do not match. Try again.")
            continue
        if not is_valid_password(pwd1):
            print("Password must be at least 8 characters long and contain both upper and lower case letters.")
            continue
        print("Password reset successful.")
        break

if __name__ == "__main__":
    main()