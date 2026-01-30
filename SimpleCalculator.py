def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b


def do_calculation():
    operator = input("Which operation do you want (+ - * /)? ").strip()

    if operator not in ['+', '-', '*', '/']:
        print("that operator doesn’t look right.")
        return

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operator == '+':
        result = add(first_number, second_number)
    elif operator == '-':
        result = subtract(first_number, second_number)
    elif operator == '*':
        result = multiply(first_number, second_number)
    else:  # division
        result = divide(first_number, second_number)
        if result is None:
            print("You can’t divide by zero.")
            return

    print(f"Result: {result}")


while True:
    print("\n--- Simple Calculator ---")
    print("1. Do a calculation")
    print("2. Exit")

    choice = input("What do you want to do? ").strip()

    if choice == '1':
        do_calculation()
    elif choice == '2':
        print("Okay, see you later")
        break
    else:
        print("That’s not a valid option. Try again.")
