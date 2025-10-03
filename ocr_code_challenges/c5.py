names = []

print("Enter names one by one. Type 'done' when finished.")
while True:
    name = input("Enter a name: ")
    if name.lower() == 'done':
        break
    names.append(name)

if not names:
    print("No names were entered.")
else:
    choice = input("Print names in (o)riginal order or (r)everse? ").strip().lower()
    if choice == 'r':
        print("Names in reverse order:")
        for n in reversed(names):
            print(n)
    else:
        print("Names in original order:")
        for n in names:
            print(n)