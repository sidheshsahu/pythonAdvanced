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


dog1 = Dog("Tommy")
dog1.speak()
dog1.bark()