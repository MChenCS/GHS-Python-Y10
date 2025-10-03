def is_palindrome(s):
    s = s.strip().lower()
    return s == s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("Palindrome")
    else:
        print("Not a palindrome")