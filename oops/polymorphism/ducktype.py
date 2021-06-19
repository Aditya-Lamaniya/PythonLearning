class birds:
    def talk(self):
        print("it cannot talk ")
class human:
    def talk(self):
        print("it can talk")

def calltalk(obj):
    obj.talk()

d=birds()
calltalk(d)

h=human()
calltalk(h)