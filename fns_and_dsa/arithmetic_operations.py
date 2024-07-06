def perform_operation(num1, num2, operator):
    if operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    elif operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        if num2 == 0:
            print("Cannot divide by zero")
            return None
        else:
            result = num1 / num2
    else:
        print("Invalid input")
    return result

