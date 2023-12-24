import random
from faker import Faker
from person import Person


def match_secret_santa_using_faker():
    print("\n*** Welcome to Secret Generator with Faker ***\n")

    # Create a Faker object to generate fake first names.
    faker = Faker()

    # Initialize an empty set to hold unique names.
    names = set()
    # Generate 10 unique first names using Faker and add them to the set
    for i in range(10):
        names.add(faker.first_name())

    # Convert the set to a list and print the names before shuffling.
    names = list(names)

    # Initialize an empty list to hold Person objects.
    people = []
    # Create a Person object for each name and add it to the list.
    for i in range(len(names)):
        people.append(Person(name=names[i]))

    # Initialize pointers for the start, end, and middle of the list.
    start = 0
    end = len(names) - 1

    # Loop through the list to assign each person someone to give a gift to.
    while start < end:
        people[start].receiver = people[end].name  # Assign the person at the start to give to the person at the end.
        people[end].receiver = people[
            start + 1].name  # Assign the person at the end to give to the next person in the list
        start += 1  # Move the start pointer up.
        end -= 1  # Move the end pointer down.

    # Assign the last person in the middle to give to the first person
    people[start].receiver = people[0].name

    # Print the final Secret Santa pairings
    print("--- Secret Santa Pairings ---")
    for person in people:
        print(f"{person.name} will give their gift to {person.receiver}")