import math
print("Choose one")
print("a.Sin\nb.Cos\nc.Tan")
ans=input("Choose one of the above(a,b,c): ")
angle=int(input("What is the angle(no need to add degree sign): "))
if ans=="a":
    print(math.sin(angle))
elif ans=="b":
    print(math.cos(angle))
elif ans=="c":
    print(math.tan(angle))
else:
    print("Invalid answer")