



class Employee:

    def __init__(self,name,age):   #constructor is a special method which is automatically called when   
        self.name=name             #an object of the class is created
        self.age=age
    
    def display(self):      #self denotes the current object and in class function is called method 
        print("Hello World")
        print("Name:",self.name)
        print("Age:",self.age)

    def greeting(self):
        print("Welcome to OOPS")


obj1=Employee("sahu",45)
obj1.display()