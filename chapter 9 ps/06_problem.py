# Write a program to find out the line number where python is present from ques 6.
with open("log.txt") as f:
    lines = f.readlines()

linesno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. line no {linesno}" )
        break
    linesno += 1

else:
    print("no python is not presnt")
