#Implementing Encapsulation

class student:
    def stid(self,id):
        self.id=id
    def gtid(self):
        return self.id
    def stnm(self,nm):
        self.nm=nm
    def gtnm(self):
        return self.nm

s=student()
s.stid(123123)
s.stnm('adi')
print(s.gtid())
print(s.gtnm())