class api_fetch:
    def fetch(self):
        print("Fetching data from API")


class database_fetch:
    def fetch(self):
        print("Fetching data from Database")

class adls_fetch:
    def fetch(self):
        print("Fetching data from ADLS")      


obj=api_fetch()
obj.fetch() # As all methods in the classes are same, we can call the same method name from different classes. This is called polymorphism.