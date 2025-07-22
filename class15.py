"""Outline:
Write a program to create a function name well wishes that will give output hello, how are you!
def well_whishes():
    print("Hello, how are you.")

well_whishes()


Weather condition
Outline:
Write a program to display the weather in autumn and spring :


def weather_check():
    weather=input("What is the season right now: ")
    if weather=="autumn":
        print("The weather right now is cool")
    elif weather=="spring":
        print("The weather is warm right now")
    else:
        print("Invalid answer")

weather_check()

Calculator
Outline:
Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide.
 Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform 
 And call that function accordingly"""


number1=int(input("what is the first number: "))
number2=int(input("What is the second number: "))
print("Please select the operation(a,b,c,d)")
print("a.addition\nb.subpraction\nc.multiplication\nd.division")
operation=input("Please enter your choice (a,b,c,d): ")
def add(p,q):
    return p+q
def supraction(p,q):
    return p-q
def multipliction(p,q):
    return p*q
def division(p,q):
    return p/q
if operation=="a":
    print(add(number1,number2))
elif operation=="b":
    print(supraction(number1,number2))
elif operation=="c":
    print(multipliction(number1,number2))
elif operation=="d":
    print(division(number1,number2))
else:
    print("Invalid answer")
    