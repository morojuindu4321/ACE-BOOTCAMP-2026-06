first=int(input("enter a number:"))
second=int(input("enter another number:"))
op=input("enter an operator ")
match op:
    case "+":
        print(first+second)
    case "-":
        print(first-second)
    case "*":
        print(first*second)
    case "/":
        print(first/second)
    case "//":
        print(first//second)
    case "**":
        print(first**second)
    case "%":
        print(first%second)
    case _:
        print("Invalid operator")