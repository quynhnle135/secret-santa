from faker import Faker

faker = Faker()

print(faker.name())
print(type(faker.name()))
print(faker.first_name())
names = []
for i in range(10):
    names.append(faker.first_name())
print(names)