def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item = input("enter the item to add: ")
            shopping_list.append(add_item)
            print(f"{add_item} added succesfulyy")
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Enter the item you want to remove")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} has been removed")
            else:
                print(f"{remove_item} is not in the list")
        elif choice == '3':
            # Display the shopping list
            # for item in shopping_list:
                print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
