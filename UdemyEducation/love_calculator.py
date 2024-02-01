if __name__ == '__main__':
    # Love Calculator
    print("The Love Calculator is calculating your score...")
    name1 = input("What is your name?").lower()
    name2 = input("What is their name?").lower()
    combined_names = name1 + name2
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    total_true = t + r + u + e
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    total_love = l + o + v + e
    total_score = int(str(total_true) + str(total_love))
    if total_score < 10 or total_score > 90:
        print(f"Your score is {total_score}, you go together like coke and mentos.")
    elif 40 <= total_score <= 50:
        print(f"Your score is {total_score}, you are alright together.")
    else:
        print(f"Your score is {total_score}.")
