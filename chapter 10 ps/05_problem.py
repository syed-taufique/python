# Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
# fare information of train running under Indian Railways
from random import randint
class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def Book(self,frm,to,):
        print(f"Ticket is booked in train no: {self.trainNo}from {frm}to{to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getfare(self,frm,to,):
        print(f"Ticket fare is train no: {self.trainNo}from{frm}to{to}is{randint(222,555)}")

t = Train(124787)
t.Book("Siwan","Lucknow")
t.getstatus()
t.getfare("Siwan","Lucknow")