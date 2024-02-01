if __name__ == '__main__':
    # Pizza Order Program
    size = input("What size pizza do you want? S, M, or L ").upper()
    if size != "S" and size != "M" and size != "L":
        print("Please enter correct size - S, M, or L")
        quit()
    add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
    extra_cheese = input("Do you want extra cheese? Y or N ").upper()
    check = 0
    if size == "S":
        check = 15
    elif size == "M":
        check = 20
    else:
        check = 25
    if add_pepperoni == "Y":
        if size == "S":
            check += 2
        else:
            check += 3
    if extra_cheese == "Y":
        check += 1
    print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${check}.")
