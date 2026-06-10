class Employee:
    def __init__(self,name,age,standard):
        self.__name=name #private var
        self.age=age   #public var
        self._standard=standard #protected var

    def display(self):
        print("Name:",self.__name)
        print("Age:",self.age)
        print("class:",self._standard)

    def greeting(self):
        print("Welcome to OOPS")


obj1=Employee("sidhesh",20,11)
obj1.display()# All types of variables easily accessed inside function 

print(obj1.age)#Easily accessed
print(obj1.__name)#Error
print(obj1._standard)#Warning 


