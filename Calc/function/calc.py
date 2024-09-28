# calc.py
# Basic math calculator
def calculate(num1, num2, operation):
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 != 0:
                return num1 / num2
            else:
                print("Error: Division by zero!")
                return None
        else:
            print("Error: Invalid operation!")
            return None
    except ValueError as e:
        print("Error: Bad Value")
        return None
    except NameError as e:
        print("Error: Undefined Var")
        return None
    except TypeError as e:
        print("Error: Operation is applied to an object of an inappropriate type.")
        return None
    except ZeroDivisionError as e:
        print("Error: Division by zero!")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None
    except KeyboardInterrupt as i:
        print("Warning: Got interrupted")
        return None
