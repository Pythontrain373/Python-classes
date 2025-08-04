"""Tuple Operations
Outline:
Write a program to perform the following operations: 
1. Create a tuple with different datatypes 2. Create another tuple of integers
 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple
   5. Perform slicing on the tuple
my_tuple=(1,2,3,4,5,6,7,8,'r','h','f')
print(my_tuple)
my_tuple2=(1,2,4,5,6,7,8,0)
print(my_tuple2)
my_tuple3=my_tuple2+(9,)
print(my_tuple3)
my_tuple4=(1,1,2,2,3,3,4,4,5,5)
print(my_tuple4.count(3))
my_tuple5=(1,2,3,4,5,6,7,8,9,0)
print(my_tuple5[2:7])"""

"""Flip Flop
Outline:
Write a program to check whether the given tuple -
(1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
my_tuple=(1,2,3,3,2,1)
if my_tuple==my_tuple[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")"""


"""Weather Prediction
Outline:
Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). 
If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by
1. On the basis of the value of rainy and sunny, predict the weather."""
wether=(1,0,0,0,1,1,0)
rainy=0
sunny=0
for i in range(0,7):
    if wether[i]==1:
        rainy=rainy+1
    else:
        sunny=sunny+1
if sunny>rainy:
    print("It is going to be sunny")
else:
    print("IT is going to rain")