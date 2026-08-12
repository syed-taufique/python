#Write a program which finds out whether a given name is present in a list or not.
l = ("Harry", "Rohan", "Sima", "Sumaiya")

name = input("Enter the name: ")

if (name in l):
    print("You name in the list")

else:
    print("You name is not in the list")