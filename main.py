height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#round the bmi value
bmi = round(weight / height ** 2) 
#if the bmi is less than 18.5
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
#if bmi is over than 18.5 and less than 25
elif 18.5 < bmi < 25: 
    print(f"Your BMI is {bmi}, you have a normal weight.")
#if bmi is over than 25 and less than 30
elif 25 < bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
#if the bmi is over than 30 and less than 35
elif 30 < bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")