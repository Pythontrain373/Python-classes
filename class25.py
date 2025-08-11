"""Hands-on Map
Outline:
Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list.
Use the map() function here to get the desired result.
number_1=[1,2,3]
number_2=[4,5,6]
result=map(lambda x,y:x+y,number_1,number_2)
print(list(result))
number_3=[1,2,3,4,5]
def sq(n):
    return n*n
square=map(sq,number_3)
print(list(square))"""



"""Zip It!
Outline:
Write a program to return -
1. zipped list from two lists
2. elements of two lists zipped together,
but 2nd list in reverse order 3. elements of two lists zipped into a dictionary

my_set={1,2,34,5,6,7,8,9}
my_set_2=("hi","a","b","c","d",'f','e','t')
result=list(zip(my_set,my_set_2))
print(result)

my_set=[1,2,34,5,6,7,8,9]
my_set_2=["hi","a","b","c","d",'f','e','t']
for i,j in zip(my_set,my_set_2[::-1]):
    print(i,j)

my_dict={my_set:my_set_2 for my_set,my_set_2 in zip(my_set,my_set_2)}
print(my_dict)



That is the exit
Outline:
Write a program where the value of i begins from 1 and goes to 10.
 When the value of i becomes 5, force the interpreter to exit the program.


for i in range(1,10):
    print(i)
    if i==5:
        exit()"""