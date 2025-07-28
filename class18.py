"""Value Error
Outline:
Write a program to understand how the value error exception works?

number=int(input("Enter a number: "))
print(number)

Bye Bye
Outline:
Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.

while True:
    try:
        number=int(input("Enter the number: "))
        while number%2==0:
            print("Bye")
    except:
        while number%2!=0:
            print("Invald answer")

Multiple exceptions
Outline:
Write a program to check how the exceptions and finally statement works
try:
    number1,number2=eval(input("Enter two numbers seprated by a comma: "))
    result=number1/number2
    print(result)
except ZeroDivisionError:
    print("Divison by 0 is error")
except SyntaxError:
    print("comma is missing")
except:
    print("Wrong input")
finally:
    print("This will excute no matter what")"""
try:
    age=int(input("Enter your age: "))
    if (age<18):
        raise ValueError
    else:
        print("The age is valid")
except ValueError:
    print("The age is not valid")

