import random
from typing import List
from person import Person


def match_secret_santa_using_bs(names: List[str]) -> None:
    print("\n*** Welcome to Secret Santa Matcher using Binary Search ***\n")
    # Shuffle the list of names to randomize the order.
    random.shuffle(names)

    # Initialize an empty list to hold Person objects.
    people = []
    # Create a Person object for each name and add it to the list.
    for i in range(len(names)):
        people.append(Person(name=names[i]))

    # Initialize pointers for the start and end of the list.
    start = 0
    end = len(names) - 1

    # Loop through the list to assign each person someone to give a gift to.
    while start < end:
        people[start].receiver = people[end].name  # Assign the person at the start to give to the person at the end.
        people[end].receiver = people[start + 1].name  # Assign the person at the end to give to the next person in the list
        start += 1  # Move the start pointer up.
        end -= 1  # Move the end pointer down.

    # Assign the last person in the middle to give to the first person
    people[start].receiver = people[0].name

    # Print the final Secret Santa pairings
    print("--- Final Secret Santa Pairings ---")
    for person in people:
        print(f"{person.name} will give their gift to {person.receiver}")
