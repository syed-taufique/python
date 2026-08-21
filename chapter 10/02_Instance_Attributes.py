class Employee:
    name = "Harry"   # This is a class attribute
    language = "Python"

harry = Employee()
harry.language = "java"  # This is a instance(object) attribute
print(harry.name, harry.language)