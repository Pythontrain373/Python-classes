def check_age():
    try:
        age=int(input("What is your age: "))
        if age%2!=0:
            print("Your age is a odd number")
        elif age%2==0:
            print("Your age is a even number")
        else:
            raise ValueError
    except ValueError:
        print("Invalid age please try again")
        check_age()
while True:
    check_age()