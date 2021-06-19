class overthelimit(Exception):
    def __init__(self,msg):
        self.msg=msg

def withdrawl(amount):
    if(amount>10000):
        raise overthelimit("you cannot withdrawl more than 10000")

withdrawl(100)