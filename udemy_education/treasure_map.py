if __name__ == '__main__':
    line1 = ["⬜️", "⬜️", "⬜️"]
    line2 = ["⬜️", "⬜️", "⬜️"]
    line3 = ["⬜️️", "⬜️️", "⬜️️"]
    map = [line1, line2, line3]
    print("Hiding your treasure! X marks the spot.")
    position = input()  # Where do you want to put the treasure?
    position_index = position[0].lower()
    line = int(position[1]) - 1
    if position_index == 'a':
        index = 0
    elif position_index == 'b':
        index = 1
    elif position_index == 'c':
        index = 2
    map[line][index] = 'X'
    # Alternative variant:
    # letter = position[0].lower()
    # abc = ["a", "b", "c"]
    # letter_index = abc.index(letter)
    # number_index = int(position[1]) - 1
    # map[number_index][letter_index] = "X"
    print(f"{line1}\n{line2}\n{line3}")
