"""vKeep It Private!
Outline:
Write a program to create a class with following variables and methods - 
1. Private variable named privateVar that contains an integer value 
2. Create a private function privMeth that prints a message 
3. Create a function hello that prints the value of privateVar 
4. Create an object for the class and call all the functions.

class MyClass:
    __private_var = 27
    def __priv_meth(self):
        print("I am inside class MyClass")
    def hello(self):
        print("Private variable value:", MyClass.__private_var)
        self.__priv_meth()
foo = MyClass()
foo.hello()"""





"""Computer Price
Outline:
Write a program to create a class Computer with a private attribute max_price and methods sell(to display) 
the selling price and setmaxprice(change the private attribute max_price). 
Now create an object for the class Computer. 
Try changing the value of max price and use the sell function to display the updated price. 
Use a setter function to update the value and again display the price.

class computor:
    def __init__(self):
        self.__maxprise=900
    def sell(self):
        print("Selling price: {}".format(self.__maxprise))
    def set_max_price(self,price):
        self.__maxprise=price
c=computor()
c.sell()
c.__maxprise=1000
c.sell()"""
        


"""Point Function
Outline:
Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. 
Also, it consists of a function that returns the coordinates in Point format. 
Create an object passing the coordinates and print the Point.

class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
p1=point(2,3)
print(p1)"""
        










