marks = {
    "harry":98,
    "rohan":95,
    "sohan":45,
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":56})
print(marks)

print(marks.get("harry"))