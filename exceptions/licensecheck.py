class tooyoung(Exception):
    def __init__(self):
        print("too young to drive")


class tooOld(Exception):
    def __init__(self):
        print("too old to drive ")


age = int(input("enter your age   :"))
if age < 18:
    raise tooyoung
elif age > 80:
    raise tooOld
else:
    print("you are eligible to drive ")
