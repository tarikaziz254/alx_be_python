num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
operator=input("Enter either of the operators")

match operator:
    case '+':
        result=num1 + num2
        print(f"The result is: {result}")
    case '-':
        result=num1 - num2
        print(f"The result is: {result}")
    case '*':
        result=num1 * num2
        print(f"The result is: {result}")
    case '/':
        match num2:
            case 0:
                print("Error enter a different number")
            case _:
                result=num1/num2
                print(f"The result is {result}")
    case _:
        print("YOu have enter incorrect operation")
