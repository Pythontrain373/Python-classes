class Dog:
    breed="Canine"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Breed:",self.breed)
        print("Name:",self.name)
        print("Age:",self.age)
dog1=Dog("Bulldog",5)
dog2=Dog("Beagle",3)
dog1.display()
dog2.display()