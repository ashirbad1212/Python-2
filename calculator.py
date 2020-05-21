#Program to create simple calculator in Python which on input of 1,2,3,4 should add , subtract , multiply and divide respectivel

def add(x, y):  #for adding
    return x + y

def subtract(x, y): #function for subtracting
    return x - y

def multiply(x, y):  #for multiplication
    return x * y

def divide(x, y):   #function for division
    return x / y


print("Select ur desired operation for perfoming calculation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice from(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':    #elif for else if
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")