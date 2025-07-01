"""AND-OR operator
Outline:
Write a program to check whether the given values have boolean values or not.


a=int(input("What is the first number: "))
b=int(input("What is the second number: "))
c=int(input("What is the third number: "))
if a%2==0 and b%2==0 and c%2==0:
    print("All the numbers are divisible by two")
else:
    print("At least 1 number is not divisible by two")
    
x=int(input("What is the first number: "))
y=int(input("What is the second number: "))
z=int(input("What is the third number: "))
if x%2==0 or y%2==0 or z%2==0:
    print("At least 1 number is divisible by 2")
else:
    print("No number is divisible by two")


    NOT Equal Operator
Outline:
Write a program to check the application of not equal operator
a=int(input("What is your first number: "))
b=int(input("What is your second number: "))
print(a != b)


BMI Checker
Outline:
Write a program to calculate the BMI of a person?"""


weigh=int(input("Enter your weight in kg: "))
height=int(input("Enter your height in cm: "))
bmi=weigh/(height/100)**2
print("Your BMI is ",bmi)
if bmi <=18.5:
    print("You are underweight")
elif bmi <=25:
    print("You are healthy")
elif bmi <=30:
    print("You are overweight")
elif bmi <=35:
    print("You are obese")
else:
    print("You are severly obese")