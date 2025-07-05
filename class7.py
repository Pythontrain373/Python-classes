"""Identity operator
Outline:
Write a program to illustrate the use of 'is' identity operator


a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=[1,2,3]
d=a
print(a is b)
print(a is d)
print(b is c)
print(b is not c)


Bitwise operator
Outline:
Write a program to apply the right shift and left shift bitwise operator.


membership operator
a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a
print(a in b)
print(a not in b)
print(a in c)
print(c in a)



Grading system
Outline:
Write a program to show students' grades by entering five subject marks and calculating average marks and grades. 
For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?


a=int(input("What is your first mark: "))
b=int(input("What is your second mark: "))
c=int(input("What is your third mark: "))
d=int(input("What is your fourth mark: "))
e=int(input("What is your 5th mark: "))
average=(a+b+c+d+e)/5
if average>91:
    print("You got a A1")
elif average>81:
    print("You got a A2")
elif average>71:
    print("You got a B1")
elif average>61:
    print("You got a B2")
elif average>51:
    print("You got a C1")
elif average>41:
    print("You got a C2")
elif average>31:
    print("You got a D1")
elif average>21:
    print("You got a D2")
elif average>11:
    print("You got a E1")
else:
    print("You got a E2")"""