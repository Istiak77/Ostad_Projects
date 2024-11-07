print("calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = input("Select an option: ")

if option == "1":
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    n3 = n1 + n2
    print("Result:", str(n3))

elif option == "2":
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    n3 = n1 - n2
    print("Result:", str(n3))

elif option == "3":
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    n3 = n1 * n2
    print("Result:", str(n3))

elif option == "4":
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        n3 = n1 / n2
        print("Result:", str(n3))

else:
    print("Invalid Input")
