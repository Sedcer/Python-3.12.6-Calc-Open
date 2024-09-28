# main.py
from calc import calculate

def main():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operation = input("Type which operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            result = calculate(num1, num2, operation)

            if result is not None:
                print(f"The result is: {result}")

            # Ask if the user wants to perform another calculation
            another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if another_calculation != "yes":
                print("Exiting the calculator. Goodbye!")
                break

        except ValueError:
            print("Error: Please enter valid numerical values.")
        except KeyboardInterrupt:
            print("\nWarning: Got interrupted. Exiting program.")
            break

if __name__ == "__main__":
    main()
