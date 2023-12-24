import random
from person import Person


names = ["quinn", "jonathan", "brian", "jessica", "susan", "khoa", "khanh", "paul", "phong"]
random.shuffle(names)
people = []

for i in range(len(names)):
    receiver = random.randint(0, len(names) - 1)
    people.append(Person(name=names[i], receiver=names[receiver]))


for p in people:
    print(f"{p.name} will give their gift to {p.receiver}")
