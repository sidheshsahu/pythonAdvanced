



class Employee:
    name="sahu"
    age=45

    def display(self):      #self denotes the current object and in class function is called method 
        print("Hello World")
        print("Name:",self.name)
        print("Age:",self.age)

    def greeting(self):
        print("Welcome to OOPS")


obj1=Employee()
obj1.display()