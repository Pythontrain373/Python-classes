"""Tip, the waiter
Outline:
Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant.
Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), 
this function calculates the total amount you should pay.
def total_calc(bill,tip):
    total=bill*(1+0.01*tip)
    total=round(total,2)
    print("Please pay ",total)
total_calc(1000,150)


Cube of the cube
Outline:
Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube(number):
    return number**3
def div_by_three(number):
    if number%3==0:
        return cube(number)
        #print("The number is divisiblle by three")
    else:
        return False
        #print("The number is not divisible by three")
print(div_by_three(5))


Factorial
Outline:
Write a program to find the factorial using recursive function

def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
n=int(input("What is the number: "))
if n<=0:
    print("Factorial dosent exist in negetive numbers: ")
else:
    print(f"factorial of {n} is {factorial(n)}")"""