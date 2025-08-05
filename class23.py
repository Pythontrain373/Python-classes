"""Get rid of the duplicates
Outline:
First, create a dictionary that consists of - id, name, class and subject integration of students.
 Then, write a program to retrieve unique entries and eliminate the rest.


my_dict={'id1':{'name':'Zara','class':'6C','subject':['Math','English','Science']},
         'id2':{'name':'Tim','class':'6C','subject':['Math','English','Science']},
         'id3':{'name':'John','class':'6C','subject':['Math','English','Science']},
         'id4':{'name':'Ronny','class':'6C','subject':['Math','English','Science']}}
print(my_dict)"""

"""Check the frequency
Outline:
Write a program to check the frequency of a value in a dictionary - {'Codingal' :
 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.

my_dict={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
k=3
result=0
for i in my_dict:
    if my_dict[i]==k:
        result=result+1
print("Frequency of k =",result)"""


"""Get the country code
Outline:
Write a program to return the country code for various countries. Here is a dictionary of different country codes 
 {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.

my_dict={'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
print("Contry code of india",my_dict.get("India","Not found"))
print("Contry code of Australia",my_dict.get("Australia","Not found"))
print("Contry code of Napal",my_dict.get("Nepal","Not found"))"""