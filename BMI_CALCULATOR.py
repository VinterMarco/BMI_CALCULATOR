# BMI calculator

print("Let's calculate your Body Mass Index")
print("Please answer to my next questions")
print("")
weight = float(input("1. Enter your weight in Kilograms: "))
height = float(input("2. Enter your height in centimeters: "))
height_in_cm = height / 100
bmi = weight / (height_in_cm ** 2)


if bmi > 40:
    print(f"You're BMI is {bmi}\nThis means that you have class III Obesity")
elif 35 < bmi < 39.9:
    print(f"You're BMI is {bmi}\nThis means that you have class II Obesity")
elif 30 < bmi < 34.9:
    print(f"You're BMI is {bmi}\nThis means that you have class I Obesity")
elif 25 < bmi < 29.9:
    print(f"You're BMI is {bmi}\nThis means that you are overweight")
elif 18.5 < bmi < 24.9:
    print(f"You're BMI is {bmi}\nThis means that you have a normal weight")
elif bmi < 18.5:
    print(f"You're BMI is {bmi}\nThis means that you are underweight")

