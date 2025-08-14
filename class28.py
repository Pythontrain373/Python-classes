"""String Upper Case
Outline:
Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1.
Next up create a method that gets a string as input from the user.
Create another method that will print the string in the upper case.
Next up create an object and call methods to get everything implemented.
class IOString:
    def __init__(self):
        self.str1=""
    def get_str(self):
        self.str1=input("What is the word: ")
    def print_str(self):
        print("The reuslt is:",self.str1.upper()) 
str1=IOString()
str1.get_str()
str1.print_str()"""



"""Employee in and Out
Outline:
Write a program to create a class with the named employee and create a constructor and destructor. 
Then, write a function to create an object for that class and delete the object. 
Make sure you call the function to get everything implemented

class Emplooy:
    def __init__(self):
        print("Employe created")
    def __del__(self):
        print("Destorcter called")
def create_obj():
    print("Macking object")
    obj=Emplooy()
    print('Function end')
    return obj
print('calling Creat_obj()  function')
obj=create_obj()
print("Program end")"""










"""Pair of Elements
Outline:
Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return 
the position of elements. The value of the sum can be taken as input from the user. 
Tuple - (10,20,30,40,50,60,70)"""
class pair:
    def two_sum(self,numbs,target):
        lookup={}
        for i,num in enumerate(numbs):
            if target-num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i
value=int(input("Enter the sum you want to search: "))
print("index1=%d,index2=%d" %pair().two_sum((10,20,30,40,50,60,70,80,90),value))