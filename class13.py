"""Right angle triangle
Outline:
Write a program to demonstrate a right angle triangle pattern?



row=int(input("Enter the numbeer of rows: "))
for i in range(row):
    for j in range(i+1):
        print("*",end=" ")
    print()


    
Floyd's triangle
Outline:
Write a program to demonstrate a Floyd triangle pattern?


row=int(input("Enter the numbeer of rows: "))
number=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(number,end=" ")
        number=number+1
    print()



Diamond Pattern
Outline:
Write a program to demonstrate the numbers in a diamond pattern?

(without numbers)

row=int(input("Enter the numbers of rows: "))
for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(row):
    for j in range(i):
        print(" ",end="")
    for k in range(row-i):
        print("*",end=" ")
    print()


(with numbers)


row=int(input("Enter the numbers of rows: "))
number=1
for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for k in range(i+1):
        print(number,end=" ")
    number=number+1
    print()
for i in range(row):
    for j in range(i):
        print(" ",end="")
    for k in range(row-i):
        print(number,end=" ")
    number=number-1
    print()

row=int(input("Enter the numbers of rows: "))
for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    number=1
    for k in range(i+1):
        print(number,end=" ")
        number=number+1
    print()
for i in range(row):
    for j in range(i):
        print(" ",end="")
    number=1
    for k in range(row-i):
        print(number,end=" ")
        number=number+1
    print()"""