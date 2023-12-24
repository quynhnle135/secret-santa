from secret_santa_using_faker_and_bs import match_secret_santa_using_faker
from secret_santa_using_binary_search import match_secret_santa_using_bs
from secret_santa_using_circular import match_secret_santa_using_circular
from menu import menu


def main():
    user_choice = input(
        "Welcome to the Secret Santa Matcher program!\n"
        "Choose a method to generate pairings:\n"
        "  (1) Faker: Generates fake names to demonstrate the program.\n"
        "  (2) Binary Search: Enter real participants' names. Uses a binary search method for matching.\n"
        "  (3) Circular: Enter real participants' names. Uses a circular assignment method for matching.\n"
        "Select an option (1, 2, or 3): "
    )

    if user_choice == "1":
        match_secret_santa_using_faker()
    elif user_choice == "2":
        names = menu()
        match_secret_santa_using_bs(names)
    elif user_choice == "3":
        names = menu()
        match_secret_santa_using_circular(names)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()