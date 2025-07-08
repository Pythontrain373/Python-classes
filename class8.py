"""Operator precedence
Outline:
Write a program to understand how the operator precedence works


a=5
b=7
c=9
d=12
e=15
result=(d+e)*c/b**a+c*e-d
print(result)


Divisible Number
Outline:
Write to check a numerator is divisible by denominator.


n=int(input("What is the numerator: "))
d=int(input("What is the denominator: "))
if n%d==0:
    print(n,"is divisible by",d)
else:
    print(n,"is not divisible by",d)


Mean Value
Outline:
The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.


answer=(40*38+(56-36))/40
print(answer)


Average speed
Outline:
Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the
 average speed?

one=int(input("What is the first cyclist speed: "))
two=int(input("What is the second cyclist speed: "))
three=int(input("What is the third cyclist speed: "))
average=(one+two+three)/3
print("The average speed is ",average)
if average>one:
    print("Cyclist 1 is slower than the average speed")
elif average>two:
    print("Cyclist 2 is slower than the average speed")
elif average>three:
    print("Cyclist 3 is slower than the average speed")
else:
    print("Invalid inputs please try again")"""