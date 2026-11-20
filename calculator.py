try:
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    print("select operation: ")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    choice = input("Enter choice(1/2/3/4): ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if choice == "1":
        print(add(num1,num2))
    elif choice == "2":
        print(subtract(num1,num2))
    elif choice == "3":
        print(multiply(num1,num2))
    else: 
        if choice == "4":
            print(divide(num1,num2))
except ZeroDivisionError:
    print("You cant divide with zero")
except ValueError:
    print("Enter a valid number")