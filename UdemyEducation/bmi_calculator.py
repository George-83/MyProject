if __name__ == '__main__':
    # BMI Calculator
    height = input("What is your height in metres (example: 1.87)? ")
    weight = input("What is your weight? ")
    weight_as_int = int(weight)
    height_as_float = float(height)
    bmi = weight_as_int / height_as_float ** 2
    bmi = weight_as_int / (height_as_float * height_as_float)
    bmi_as_int = int(bmi)
    print(f"Your BMI is {bmi_as_int}")
