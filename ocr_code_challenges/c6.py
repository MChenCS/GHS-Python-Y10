numbers = []

while True:
    user_input = input("Enter a number (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    try:
        num = float(user_input)
        numbers.append(num)
        print(f"Current list: {numbers}")
        print(f"Maximum: {max(numbers)}")
        print(f"Minimum: {min(numbers)}\n")
    except ValueError:
        print("Please enter a valid number or 'quit' to exit.\n")