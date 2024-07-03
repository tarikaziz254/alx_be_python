def perform_operation():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
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
                return "cannot divide by zero"
        case _:
            return "invalid input"
result = perform_operation()
print(f"Result: {result}")


