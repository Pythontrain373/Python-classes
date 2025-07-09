"""Exam Eligibility Check
Outline:
Write a program to check whether the student can take an exam or not.
 Students will be allowed only in two conditions: If they have a medical cause 
 (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. 
 If No, then check attendance If attendance is above 75, then allowed; otherwise,
 not allowed.


med=input("Do you have any medical cause,Y for yes and N for no: ")
if med=="Y":   
    print("Ok You are 1 step ahead to check if you are allowed for exam or not")
    attendence=int(input("Please enter your attendence percentage: "))
    if attendence>=75:
        print("You are allowed for exam.")
    else:
        print("You are not allowed for exam.")
else:
    print("You are not allowed to join the exam.")


    Electricity bill
Outline:
Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. 
Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25.
 If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35
   If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45
     And above 200, the cost of the unit is 8.45, and the tax is 75.


units=int(input("How many units are you using per month: "))
if units<50:
    final=units*2.60+25
    print("Your electricity bill is",final," dollars")
elif units<100:
    final=units*3.25+35
    print("Your electricity bill is",final," dollars")
elif units<200:
    final=units*5.26+45
    print("Your electricity bill is",final," dollars")
else:
    final=units*8.45+75
    print("Your electricity bill is",final," dollars")



    Customise your ride
Outline:
Write a program to select a ride according to your preference.
 The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories.
To give the user better selection options.


print("Please select your ride")
print("1.Bike\n2.Car")
ride=int(input("Enter your choice(1 or 2): "))
if ride==1:
    print("What brand of bike do you want?")
    print("1.Tata motors\n2.Dugati")
    bike=int(input("Enter the company you want to choose(1 or 2): "))
    if bike==1:
        print("You selected a Tata moters bike ride")
    else:
        print("You selected a Dugati bike ride")
elif ride==2:
    print("What brand of car do you want?")
    print("1.Tata motors\n2.Porshe")
    car=int(input("Enter the company you want to choose(1 or 2): "))
    if car==1:
        print("You selected a Tata moters car ride")
    else:
        print("You selected a Porshe car ride")
else:
    print("Invalid option plese try again")"""