class Employee:

    def __init__(self,name,age,standard):
        self.name=name
        self.age=age
        self.standard=standard

    def display(self):                 # Instance Method
        print("Name:",self.name)
        print("Age:",self.age)
        print("class:",self.standard)

    def greeting(self):
        print("Welcome to OOPS")

    def printing():                    # static method
        print("This is a static method")


    @classmethod
    def class_method(cls):              # class method is used for mostly modifying the class variables
        print("This is a class method")


obj1=Employee("sidhesh",20,11)
obj1.display()# All types of variables easily accessed inside function
print(obj1.name)#Easily accessed
print(obj1.age)