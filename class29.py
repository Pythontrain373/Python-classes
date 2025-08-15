"""Is this a bus?
Outline:
Write a Python program to implement Inheritance by creating a Parent Class Vehicle with 
a constructor that has details like name, maximum speed, and mileage. 
Then, create a Child Class Bus that inherits Class Vehicle. 
Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.
class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
class bus(Vehicle):
    pass
school_bus=bus('School Volvo',180,12)
print('Vehicle name:',school_bus.name,' Max_speed:',school_bus.max_speed,' Milage:',school_bus.milage)"""
        




"""Employee Inheritance
Outline:
Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. 
Next, create a child class Employee (attributes - name, id number, salary, post). 
Access the attributes of parent class in child class. 
Then, create an object for child class and call the display method to display the name and id number.-
class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def despplay(self):
        print(self.name)
        print(self.idnumber)
class employee(Person):
    def __init__(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)
a=employee('rahul',886012,200000,'Intern')
a.despplay()"""
        



"""Super Penguin
Outline:
Write a program to create a base class Bird, with a constructor and two methods. 
Then, create a child class that inherits the constructor from Class Bird and has two functions. 
Finally, display how you can use Super to access the parent class constructor inside the child class."""
class Bird:
    def __init__(self):
        print('Bird is ready')
    def who_is_this(self):
        print('Bird')
    def swim(self):
        print('swim faster')
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print('Penguin is ready')
    def who_is_this(self):
        print('Penguin')
    def run(self):
        print('Run faster')
Peggy=Penguin()
Peggy.who_is_this()
Peggy.swim()
Peggy.run()
        