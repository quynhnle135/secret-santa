import random
from faker import Faker
from person import Person

faker = Faker()
names = set()
for i in range(10):
    names.add(faker.first_name())

names = list(names)
print(f"Names before being shuffled: {names}")
random.shuffle(names)
print(f"Names after being shuffled: {names}")

people = []
for i in range(len(names)):
    people.append(Person(name=names[i]))

start = 0
end = len(names) - 1
mid = (end - start) // 2
while start < end:
    people[start].receiver = people[end].name
    people[end].receiver = people[start + 1].name
    start += 1
    end -= 1

people[start].receiver = people[0].name

# Display santa
for person in people:
    print(f"{person.name} will give gitf to {person.receiver}")

