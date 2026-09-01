# A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams
p1 ="Make a lot of money"
p2 ="buy now"
p3 ="click this"
p4 ="subscribe this"
message = input("Enter the comment: ")

if(p1 in message or p2 in message or p3 in message):
    print("This comment is a spam")

else:
    print("This message is not spam")

