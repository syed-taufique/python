#Write a python function to print multiplication table of a given number.
def multply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

multply(5)