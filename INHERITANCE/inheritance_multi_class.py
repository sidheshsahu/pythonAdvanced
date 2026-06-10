# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

dog1 = Dog("Tommy")
dog1.speak()
dog1.bark()
cat1=Cat("kitty")
cat1.speak()
cat1.meow()