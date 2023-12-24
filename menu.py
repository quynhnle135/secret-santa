def menu():
    print("*** Welcome to Secret Santa Generator ***")
    nums = int(input("How many people will join this Secret Santa? "))
    names = []
    for i in range(nums):
        name = input(f"{i + 1}. Enter participant's name: ")
        names.append(name)

    return names
