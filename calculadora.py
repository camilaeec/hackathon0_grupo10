import re

def calculate(expression):
    expression = expression.strip()

    if not expression:
        raise ValueError("Empty input is not allowed")

    # Check for invalid characters
    if not re.match(r'^[\d\s\+\-\*/\(\)\.]+$', expression):
        raise ValueError("Invalid character found in the expression")

    try:
        # Evaluate the expression
        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")
    except SyntaxError:
        raise SyntaxError("Invalid syntax in the expression")
    except Exception as e:
        raise ValueError(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    print(calculate("4 / 2"))  # Should return 14

    