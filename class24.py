"""Operations on Sets
Outline:
Write a program to create a set and perform the following operations on that set-
1. Create a set with integer elements 2. Create a set with mixed data type elements
3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements 
- [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
my_set={1,2,3,4}
print(my_set)
my_set2={1,2,"hi",3.5,True,False,(5,6,7)}
print(my_set2)
my_set3={1, 2, 3, 4, 3, 2,4}
print(my_set3)
my_list=[1,2,3,2]
print(my_list)
my_set4=set(my_list)
print(my_set4)
my_set5={0,1,3,4,5}
my_set5.pop()
print(my_set5)

Set Intersection
Outline:
Write a program to find the intersection of two sets. Set1 = {green, blue} Set2 = {blue, yellow}
Set1={"green", "blue"}
Set2={"blue", "yellow"}
print(Set1,Set2)
Set3=Set1.intersection(Set2)
print(Set3)
set4=Set1.union(Set2)
print(set4)
set5=Set1.difference(Set2)
print(set5)
set6=Set2.difference(Set1)
print(set6)


Arrays
Outline:
Write a program to create an array with the following elements
- [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array.
Also, print the reversed array."""
import array as arr
"""arr=[1,3,5,3,7,9,3]
count_3=arr.count(3)
print(arr)
print(count_3)
rev=arr[::-1]
print(rev)"""
new_arr=arr.array("i",[1, 3, 5, 3, 7, 9, 3])
new_arr.reverse()
print(str(new_arr))