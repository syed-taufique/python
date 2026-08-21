class Employee:
    language = "Python"  
    salary = 1200000

    def getInfo(self):
        print(f"This language is {self.language}. This salary is {self.salary}")

harry = Employee()
# harry.language = "java"
harry.getInfo()
# Employee.getInfo(harry)

