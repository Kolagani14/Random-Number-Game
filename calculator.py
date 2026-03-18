def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# ✅ Added: history storage
history = []

while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit  6.View History  7.Clear History")
    choice = input("Enter choice: ")

    if choice == '5':
        print("Exiting...")
        break

    # ✅ Added: View History
    if choice == '6':
        if not history:
            print("No history yet.")
        else:
            print("\nHistory:")
            for item in history:
                print(item)
        continue

    # ✅ Added: Clear History
    if choice == '7':
        history.clear()
        print("History cleared.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        result = add(a, b)
        print("Result:", result)
        history.append(f"{a} + {b} = {result}")

    elif choice == '2':
        result = sub(a, b)
        print("Result:", result)
        history.append(f"{a} - {b} = {result}")

    elif choice == '3':
        result = mul(a, b)
        print("Result:", result)
        history.append(f"{a} * {b} = {result}")

    elif choice == '4':
        result = div(a, b)
        print("Result:", result)
        history.append(f"{a} / {b} = {result}")

    else:
        print("Invalid choice")