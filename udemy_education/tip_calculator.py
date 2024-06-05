if __name__ == '__main__':
    # Tip calculator
    print("Welcome to the tip calculator.")
    total_bill = input("What was the total bill? $")
    tip_in_percents = input("What percentage tip would you like to give? 10, 12, or 15? ")
    people_quantity = input("How many people to split the bill? ")
    short_percentage = float("1." + tip_in_percents)
    result = float(total_bill) * short_percentage / float(people_quantity)
    rounded_result = round(result, 2)
    two_decimals_format_result = "{:.2f}".format(rounded_result)
    print(f"Each person should pay: ${two_decimals_format_result}")
