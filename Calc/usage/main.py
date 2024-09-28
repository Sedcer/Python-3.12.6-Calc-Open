# main.py
from calc import Calculator

def main():
    calc = Calculator()
    
    print("Welcome to the Basic Calculator!")
    print("Available operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter the first number (or type 'exit' to quit): "))
            num2 = float(input("Enter the second number: "))
            operation = input("Type the operation (+, -, *, /): ")

            result = calc.calculate(num1, num2, operation)

            if result is not None:
                print(f"The result of {num1} {operation} {num2} is: {result}")
        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
