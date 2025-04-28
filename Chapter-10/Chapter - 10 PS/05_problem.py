from random import randint as rd

class train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Ticket is booked from {fro} to {to}")

    def getstatus(self):
        print(f"Train Number {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"The fare for train running from {fro} to {to} is {rd(1,5555)}")


t = train(12456)
t.book("Hyderabad","Delhi")
t.getFare("Hyderabad","Delhi")
t.getstatus()