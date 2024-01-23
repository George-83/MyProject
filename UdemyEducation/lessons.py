import pytest
import requests
import json

if __name__ == '__main__':
    # print("\nWelcome to the Band Name Generator.")
    # city_name = input("What's name of the city you grew up in?" + "\n")
    # pet_name = input("What's your pet's name?" + "\n")
    # print("Your band name could be " + city_name + " " + pet_name)

    # print("Hello"[4])

    age = input()
    all_years = 90
    years_left = all_years - int(age)
    weeks_left = 52 * years_left
    print(f"You have {weeks_left} weeks left.")
