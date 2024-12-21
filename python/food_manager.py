food_list = []

while True:
    print("\nFood Manager")
    print("Press q to quit")
    print("1.Add foods")
    print("2.Remove foods")
    print("3.View all foods")

    choice = input("Choose an option: ")

    if choice.lower() == "q":
        print("Thanks for using Food Manager")
        break

    elif choice == "1":
        while True:
            food = input("Enter a food name: ")
            food_list.append(food)
            print(f"{food} has been added.")
            add_more = input("Do you want to add another food? (y/n): ")
            if add_more.lower() != 'y':
                break

    elif choice == "2":
        food_list.remove(food)
        print('Food has been removed.')

    elif choice == "3":
        print("\nYour Food List:")
        if food_list:
            for index, food in enumerate(food_list, start=1):
                print(f"{index}. {food}")
        else:
            print("No food was added.")

        input("\nPress Enter to return to the main menu.")
    
    else:
        print("Invalid choice")