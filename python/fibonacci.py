print("Welcome to the Fibonacci Generator!")
print("1. Generate Fibonacci series by number of terms")
print("2. Generate Fibonacci series by maximum value")

option = input("Enter your option (1 or 2): ")

if option == "1":
    terms = int(input("How many terms do you want? "))
    if terms <= 0:
        print("Please enter a positive number.")
    else:
        series = [0, 1]
        if terms == 1:
            print("Fibonacci series with 1 term: [0]")
        else:
            while len(series) < terms:
                next_number = series[-1] + series[-2]
                series.append(next_number)
            print("Fibonacci series with", terms, "terms:", series)


elif option == "2":
    max_value = int(input("Enter the maximum value: "))
    if max_value < 0:
        print("Please enter a non-negative number.")
    else:
        series = [0, 1] 
        if max_value == 0:
            print("Fibonacci series up to 0: [0]")
        else:
            while True:
                next_number = series[-1] + series[-2]
                if next_number > max_value:
                    break
                series.append(next_number)
            print("Fibonacci series up to", max_value, ":", series)

else:
    print("Invalid option. Please enter 1 or 2.")
