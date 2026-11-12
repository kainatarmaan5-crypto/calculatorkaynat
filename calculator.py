"""
Simple Interactive Calculator in Python
Supports addition, subtraction, multiplication, division, exponentiation, and modulo.
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        raise ZeroDivisionError("Error: Modulo by zero is not allowed.")
    return x % y

def get_number(prompt):
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("=" * 40)
    print("           SIMPLE CALCULATOR            ")
    print("=" * 40)
    print("Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Exponentiation (^)")
    print("  6. Modulo (%)")
    print("  Q. Quit")
    print("-" * 40)

    operations = {
        '1': ('+', add),
        '+': ('+', add),
        '2': ('-', subtract),
        '-': ('-', subtract),
        '3': ('*', multiply),
        '*': ('*', multiply),
        '4': ('/', divide),
        '/': ('/', divide),
        '5': ('^', power),
        '^': ('^', power),
        '6': ('%', modulo),
        '%': ('%', modulo),
    }

    while True:
        choice = input("\nSelect operation (1-6 or +, -, *, /, ^, % | Q to quit): ").strip().lower()
        if choice in ['q', 'quit', 'exit']:
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid selection. Please choose an operation from the list.")
            continue

        symbol, func = operations[choice]

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = func(num1, num2)
            # Format integer outputs without trailing .0
            if result.is_integer():
                result = int(result)
            if num1.is_integer():
                num1 = int(num1)
            if num2.is_integer():
                num2 = int(num2)
            print(f"\nResult: {num1} {symbol} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"\n{e}")

if __name__ == "__main__":
    main()
