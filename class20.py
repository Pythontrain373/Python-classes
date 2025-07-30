"""Current date and time
Outline:
Write a program to check the current date and time?

from datetime import date,time,datetime
today=date.today()
print(today)
print(today.month)
print(today.day)
print(today.year)
now=datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)

Random date and time
Outline:
Write a program to generate a random date and time from the given start and end dates


import random
from datetime import datetime,time,date
import time
def gen_ran_date(start,end):
    print("printing random date between",start,"and",end)
    randome_gen=random.random()
    dateformat="%m/%d/%Y"
    start_time=time.mktime(time.strptime(start,dateformat))
    end_time=time.mktime(time.strptime(end,dateformat))
    ran_time=start_time+randome_gen*(end_time-start_time)
    ran_date=time.strftime(dateformat,time.localtime(ran_time))
    return ran_date
print("Random date=",gen_ran_date("1/1/2024","7/30/2025"))

Trip expenditure
Outline:
Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost 
Price of the vehicle rented during the trip"""
def hotle_cost(nigts):
    return 1000*nigts
def plane_cost(city):
    if city=="Hong Kong":
        return 5000
    elif city=="Jaipur":
        return 4700
    elif city=="Los Angles":
        return 9000
    elif city=="Leon":
        return 8000
def car_rent(days):
    if days>=7:
        return 400*days
    elif days>=3:
        return 300*days
    else:
        return 200*days
def total(city,days,spending_money):
    return car_rent(days)+hotle_cost(days)+plane_cost(city)+spending_money
print("Car rent:",car_rent(7))
print("Plane cost:",plane_cost("Leon"))
print("Hotel cost:",hotle_cost(7))
print("Total cost of the trip:",total("Leon",7,5000))