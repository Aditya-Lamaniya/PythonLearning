class profile:
    def setname(self, name):
        self.name = name

    def getname(self):
        return (self.name)

    def setqual(self, qual):
        self.qual = qual

    def getqual(self):
        return (self.qual)

    def setsal(self, sal):
        self.sal = sal

    def getsal(self):
        return (self.sal)

p1=profile()
p1.setname('adi')
p1.setsal(10000)
p1.setqual(["python","c++","data structure"])

print(p1.getname())
print(p1.getsal())
print(p1.getqual())





