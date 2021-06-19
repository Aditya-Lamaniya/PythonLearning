from threading import *

class bookbus:
    def __init__(self, avlseat):
        self.avlseat = avlseat
        self.l=Lock()

    def buy(self, seatreq):
        self.l.acquire
        print("total seat free = ", self.avlseat)
        if self.avlseat >= seatreq:
            print("confirming a seat")
            print("processing payment ")
            print("printing the ticket ")
            self.avlseat -= seatreq
        else:
            print("no seat avialable right now ")


obj = bookbus(10)
t = Thread(target=obj.buy, args=(3,))
t2 = Thread(target=obj.buy, args=(4,))
t3 = Thread(target=obj.buy, args=(2,))

t.start()
t2.start()
t3.start()
