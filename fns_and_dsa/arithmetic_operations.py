def perform_operations(num1, num2, operator):
    match operator:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 != 0:
                return num1 / num2
            else:
                print("Cannot divide by zero")
                return None
        case _:
            print("invalid operation")
            return None
