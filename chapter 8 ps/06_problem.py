#Write a python function which converts inches to cms
def inch_to_cms(inches):
    return inches * 2.54
n = int(input("Enter the length in inches: "))
cms = inch_to_cms(n)
print(f"The corresponding value in cms is: {round(cms, 2)}")