# calc.py
# Basic math calculator

class Calculator:
    def __init__(self):
        pass  # No attributes are necessary for this class

    def calculate(self, num1, num2, operation):
        """Perform a mathematical operation on two numbers."""
        try:
            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                raise ValueError("Both num1 and num2 must be numbers.")
            
            if operation == "+":
                return self.add(num1, num2)
            elif operation == "-":
                return self.subtract(num1, num2)
            elif operation == "*":
                return self.multiply(num1, num2)
            elif operation == "/":
                return self.divide(num1, num2)
            else:
                raise ValueError("Error: Invalid operation!")
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")
            return None
        except KeyboardInterrupt:
            print("Warning: Got interrupted")
            return None

    def add(self, num1, num2):
        """Add two numbers."""
        return num1 + num2

    def subtract(self, num1, num2):
        """Subtract the second number from the first."""
        return num1 - num2

    def multiply(self, num1, num2):
        """Multiply two numbers."""
        return num1 * num2

    def divide(self, num1, num2):
        """Divide the first number by the second."""
        try:
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return num1 / num2
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return None


# Main function
def main():
    calc = Calculator()
    # Placeholder for interaction logic
    # You can implement user input and interaction here in the future

if __name__ == "__main__":
    main()
