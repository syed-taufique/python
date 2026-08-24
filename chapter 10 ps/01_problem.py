#Create a class “Programmer” for storing information of few programmers working at
# Microsoft.
class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("Harry",120000,841227)
print(p.name,p.salary,p.pin,p.company)
