if __name__ == '__main__':
    # Age left calculator
    age = input("What is your age?")
    all_years = 90
    years_left = all_years - int(age)
    weeks_left = 52 * years_left
    print(f"You have {weeks_left} weeks left.")
