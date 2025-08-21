"""Abstract Class
Outline:
Write a program to create a base class that consists of two functions - 
one to display a value, and another function is an abstract method. 
Next, create a subclass that consists of a method similar to the abstract method. 
Finally, showcase how Abstraction is being implemented in this example.

from abc import ABC,abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value:",x)
    @abstractmethod
    def task(self):
        print("We are inside absclass task")
class teastclass(Absclass):
    def task(self):
        print("We are inside teastclass task")

test_obj=teastclass()
test_obj.task()
test_obj.print(100)"""



'''Class Animal
Outline:
Write a program to implement abstraction on animal class (base class).
The abstract method will be move will display what subclasses can do. 
Subclasses can be something like - Human, Dog.

from abc import ABC,abstractmethod
class Animal(ABC):
    def ani(self):
        pass
class human(Animal):
    def move(self):
        print('I can walk on both legs')
class dog(Animal):
    def move(self):
        print('I can bark')
hi=Animal()
h=human()
h.move()
d=dog()
d.move()'''


"""All about Countries
Outline:
Write a program to create two classes for two different countries that consist of three methods to display 
the following information of respective country - capital, language and type of country. 
Then, use Polymorphism to create a common interface for both classes.

class ind():
    def cap(self):
        print("New delhi is the capital of India")
    def lan(self):
        print("Hindi is the most popular language in India")
    def type(self):
        print('India is a developing country')
class china():
    def cap(self):
        print("Bejing is the capital of China")
    def lan(self):
        print("Chinese is the most popular language in China")
    def type(self):
        print('China is a developed country')
obj_ind=ind()
obj_chi=china()
for i in (obj_ind,obj_chi):
    i.cap()
    i.lan()
    i.type()"""



