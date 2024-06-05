# BMI Calculator
#https://mercer-health.com/services/weight-management-center/bmi-calculator#:~:text=Body%20Mass%20Index%2C%20or%20BMI,inches%20x%20height%20in%20inches

name = input("Enter you name: ")

weight = int(input("Enter your weight in kg: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name +", you are underweight.")
    elif (BMI<=24.9):
        print(name +", you are normal weight.")
    elif (BMI<29.9):
        print(name +", you are overweight. You need to exercise more and stop sitting and writing so many python tutorials.")
    elif (BMI<34.9):
        print(name +", you are obese.")
    elif (BMI<39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input")