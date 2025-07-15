number=int(input("What is the number: "))
Number=number
digits=0
while number > 0:
    number //= 10
    digits += 1
print("The number of digits in",Number,"is",digits)