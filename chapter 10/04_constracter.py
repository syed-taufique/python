class Employee:
    # name = "Harry"   # This is a class attribute
    language = "Python"
    salary = 1200000

    def __init__(self, name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

harry = Employee("Harry", 1300000 , "javascript")
# harry.language = "java"  # This is a instance(object) attribute
print(harry.name, harry.language)

# rohan = Employee()