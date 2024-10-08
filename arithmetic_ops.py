import math

def calculate(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError("Invalid operator")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None

while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        op = input("Enter an operator (+, -, *, /): ")
        result = calculate(a, b, op)
        if result is not None:
            print("Result:", result)
        break
    except ValueError:
        print("Invalid input. Please enter numbers and a valid operator.")
