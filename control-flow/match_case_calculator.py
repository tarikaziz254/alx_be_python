num1=int(input("Enter the first number:")
num2=int(input("Enter the second number:")
operations=input("Choose the operation (+, -, *, /):")

match operations:
    case '+':
        result=num1+num2
        print("The result is {result}".)
    case '-':
        result=num1-num2
        print("The result is {result}".)
    case '*':
        result=num1*num2
        print("The result is {result}".)
    case '/':
        match num2:
            case 0:
                print("Error enter a different number")
            case _:
                result=num1/num2
                print("The result is {result}.")

