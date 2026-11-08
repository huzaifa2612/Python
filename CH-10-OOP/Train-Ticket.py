from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo=trainNo
    def book(s, dep, dest):
        print(f"Your Train No.{s.trainNo} is Booked from {dep} to {dest}")

    def getstatus(s):
        print(f"The Train No.{s.trainNo} will be departured on Time")


    def getfare(s, dep, dest):
        print(f"The Ticked Fare in Train No.{s.trainNo} from {dep} to {dest} is {randint(2000, 2800)}")      

s=Train(5400)        
s.book("Lahore", "Fatehpur")
s.getstatus()
s.getfare("Lahore", "Fatehpur")