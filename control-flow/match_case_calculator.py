num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operations=input("Choose the operations (+,-,*,/):")
match operations:
    case '+':
        result=num1+num2
        print(f"The result is {result}.")
    case '-':
        result=num1-num2
        print(f"The result is {result}.")
    case '*':
        result=num1*num2
        print(f"The result is {result}.")
    case '/':
        match num2:
            case 0:
                print(f"Cannot divide by 0")
            case _:
                result=num1/num2
                print(f"The result is {result}.")
