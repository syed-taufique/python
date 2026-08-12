a = 31.2
t = type (a) #class <int>
print(t)

a = "ali"
t = type (a) #class <str>
print(t)

a = "31.2"
t = type (a) #class <str>
print(t)

a = "31.2"
b = float (a) # a but the type should be float
t = type (b) #class <float>
print(t)