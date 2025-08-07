def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def square(a):
    return a*a


def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Square (x^2)")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice not in ["1", "2", "3", "4","5"]:
        print("Invalid input.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered.")
        return

    if choice == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == "4":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == "5":
        print(f"{num1} squared = {square(num1)}")

if __name__ == "__main__":
    calculator()
