class Empolyee:
    company = "ITC"
    def show(self):
        print(f"The name of empolyee is {self.name} and the salary is {self.salary}")

# class programmer:
#     def show(self):
#             print(f"The name of empolyee is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#          print(f"The name is a {self.name} and he is a good with{self.language} language")
         

class Programmer(Empolyee):
    company = "ITC Infotec"
    def showlanguage(self):
        print(f"The name is a {self.name} and he is a good with{self.language} language")

a = Empolyee
b = Programmer
print(a.company,b.company)