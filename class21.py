"""Lists
Outline:
Write a program to perform the following operations on a List:
1. Create an empty list 2. A list with elements 3. Use * operator 4. Reverse a list
my_list=[]
my_list2=[1,2,3,4,5,6,7,8,9,0]
print(my_list2)
my_list3=[1,2,3]*3
print(my_list3)
my_list4=[100,200,300]
print(my_list4[::-1])"""


"""Word Matching
Outline:
Write a Python program to count the number of strings where the string length is two or more,
and the first and last characters are the same from a given list of strings.
def check_string(words):
    char=0
    my_list=[]
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            char=char+1
            my_list.append(i)
    print("list of the words with the same fist and last chartcer is",my_list)
    return char
new_list=check_string(["abc","ded","101","111","12","aba"])"""

"""Play with Lists
Outline:
Write a Python program to find the sum and average of the list. 
The average of the list is defined as the sum of the elements divided by the number of the elements.
Also, find the largest and the smallest number in the list.
my_list=[4,50,6,7,107,46,8]
my_sum=0
for i in my_list:
    my_sum=my_sum+i
print("Sum=",my_sum)
my_avarge=my_sum/len(my_list)
print("Average=",my_avarge)
my_list.sort()
print(my_list[0],my_list[-1])"""