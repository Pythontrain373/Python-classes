"""Character occurrence
Outline:
Write a program to check how many times a character is repeated in a word?


word=input("Enter your word(no caps): ")
charter=input("Enter your chartecter you want to check(no caps): ")
i=0
count=0
while i<len(word):
    if word [i]==charter:
        count=count+1
    i=i+1
print(count)


Is this a Prime Number
Outline:
Write a program to print all the prime numbers which come in the range entered by the user?


lower=int(input("What is the start of the range: "))
high=int(input("What is the highest number in the range: "))
for i in range(lower,high+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)


Mid product
Outline:
Write a program to calculate the product of the middle digits of a number?"""


number=int(input("What is the number: "))
t=number
number_len=0
while t>0:
    number_len=number_len+1
    t=int(t/10)#used to covert float into integer
if number_len>=4:
    number_len=int(number_len/2)
    check=0
    while number>0:
        remainder=number%10
        if check==number_len:
            mid1=remainder
        elif check==(number_len-1):
            mid2=remainder
        number=int(number/10)
        check=check+1
    product=mid1*mid2
    print("Product of mid digits= ",product)
else:
    print("It is not 4 digit or more digit number")