from typing import List
import random
from person import Person


def match_secret_santa_using_circular(names: List[str]) -> None:
    print("\n*** Welcome to the Secret Santa Matcher using Circular Assignment ***\n")
    random.shuffle(names)
    # Create person object for each name
    people = []
    for name in names:
        people.append(Person(name=name))

    # Assign each person a receiver using a circular assignment
    for i in range(len(people)):
        receiver_index = (i + 1) % len(people)  # Ensuring the last person gives a gift to the first person
        people[i].receiver = people[receiver_index].name

    # Print the Secret Santa pairs
    print("--- Final Secret Santa Pairings ---")
    for p in people:
        print(f"{p.name} will give their gift to {p.receiver}")