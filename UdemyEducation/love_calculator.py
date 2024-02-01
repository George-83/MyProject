if __name__ == '__main__':
    # Love Calculator
    print("The Love Calculator is calculating your score...")
    name1 = input("What is your name?").lower()
    name2 = input("What is their name?").lower()
    t1 = name1.count("t")
    r1 = name1.count("r")
    u1 = name1.count("u")
    e1 = name1.count("e")
    t2 = name2.count("t")
    r2 = name2.count("r")
    u2 = name2.count("u")
    e2 = name2.count("e")
    total_true = t1 + t2 + r1 + r2 + u1 + u2 + e1 + e2
    l1 = name1.count("l")
    o1 = name1.count("o")
    v1 = name1.count("v")
    e1 = name1.count("e")
    l2 = name2.count("l")
    o2 = name2.count("o")
    v2 = name2.count("v")
    e2 = name2.count("e")
    total_love = l1 + l2 + o1 + o2 + v1 + v2 + e1 + e2
    total_score = int(str(total_true) + str(total_love))
    if total_score < 10 or total_score > 90:
        print(f"Your score is {total_score}, you go together like coke and mentos.")
    elif 40 < total_score < 50:
        print(f"Your score is {total_score}, you are alright together.")
    else:
        print(f"Your score is {total_score}.")
