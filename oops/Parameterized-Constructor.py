#Using Parameterized Constructor

class lessons:
    def __init__(self,name,ratings):
        self.name=name
        self.rating=ratings

c1=lessons('corejava',[1,2,3,4,5])
print(c1.name)
print(c1.rating)
c2=lessons('python',[5,3,4,4,5])
print(c2.name)
print(c2.rating)