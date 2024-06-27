import random

if __name__ == '__main__':
    names = input("Type several names here: ")
    names_string = names.__str__()
    names = names_string.split(", ")
    names_length = len(names)
    random_name_index = random.randint(0, (names_length - 1))
    print(names[random_name_index] + " is going to buy the meal today!")

