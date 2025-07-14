"""Sum of Natural Numbers
Outline:
Write a program to find the sum of natural numbers.


number=int(input("Please enter the value: "))
sum=0
i=0
while i<=number:
    sum=sum+i
    i=i+1
print(sum)



Infinity
Outline:
Write a program to check the infinite loop?


while True:
    number=int(input("What is the first number: "))
    n2=int(input("What is the second number: "))
    add=number+n2
    print(add)

i=0
while i<=0:
    print("I will run forever")



    Armstrong number
Outline:
Write a program to check if the number entered by the user is an Armstrong number or not?


number=int(input("What is the number you want to check: "))
sum=0
i=number
while i>0:
    new=i%10
    sum += new**3
    i//=10
if number==sum:
    print("It is an armstrong number.")
else:
    print("It is not an armstrong number.")"""