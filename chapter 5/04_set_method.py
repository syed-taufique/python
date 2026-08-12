s = {1,34,56,5,34,34,"harry"}
print(s,type(s))


s.add(344)#Adds one element
print(s)


s.update([10,20])#Adds multiple elements
print(s)


s.remove(5)#Removes an element; error if absent
print(s)


s.discard(10)#Removes an element; no error if absent
print(s)