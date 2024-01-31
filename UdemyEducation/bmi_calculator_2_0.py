if __name__ == '__main__':
    # BMI Calculator
    height = float(input("What is your height in meters (example: 1.87)? "))
    weight = int(input("What is your weight in kilograms? "))
    bmi = weight / height ** 2
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif 25 <= bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif 30 <= bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")
