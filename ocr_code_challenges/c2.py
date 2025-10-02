def main():
    numbers = []
    while True:
        print("\nOptions:")
        print("1. Enter a number")
        print("2. Output average")
        print("3. Quit")
        choice = input("Choose an option (1/2/3): ").strip()
        if choice == '1':
            try:
                num = float(input("Enter a number: "))
                numbers.append(num)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            if numbers:
                avg = sum(numbers) / len(numbers)
                print(f"Average: {avg}")
            else:
                print("No numbers entered yet.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()