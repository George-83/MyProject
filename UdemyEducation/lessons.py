import pytest
import requests
import json

if __name__ == '__main__':
    # Band Name Generator
    # print("\nWelcome to the Band Name Generator.")
    # city_name = input("What's name of the city you grew up in?" + "\n")
    # pet_name = input("What's your pet's name?" + "\n")
    # print("Your band name could be " + city_name + " " + pet_name)
    # print("Hello"[4])

    # Age left calculator
    # age = input()
    # all_years = 90
    # years_left = all_years - int(age)
    # weeks_left = 52 * years_left
    # print(f"You have {weeks_left} weeks left.")

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
