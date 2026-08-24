class Empolyee:
    company = "ITC"
    name ="Harry"
    salary = 1200000
    def show(self):
        print(f"The name of empolyee is {self.name} and the salary is {self.salary}")

class coder:
    language = "python"
    def flanguage(self):
        print(f"Out of all the language here is your language: {self.language}")


class Programmer(Empolyee,coder):
    company = "ITC Infotec"
    def showlanguage(self):
        print(f"The company name is a {self.company} and he is a good with {self.language} language")

a = Empolyee()
b = Programmer()

b.show()
b.flanguage()
b.showlanguage()
