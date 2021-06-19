# program to Count the number of Objects

class object:
    objectcount=0

    def __init__(self):
        object.objectcount+=1
    @staticmethod
    def displaycount():
        print(object.objectcount)

o1=object()
o2=object()
o3=object()

object.displaycount()