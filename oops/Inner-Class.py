#Inner Class
class car:
    def __init__(self,year,manufacturer):
        self.manufac=manufacturer
        self.year=year
    class engine :
        def __init__(self,enginenum):
            self.engnum=enginenum
        def start(self):
            print("engine start success")
c=car(2017,'suzuki')
en=c.engine(532241)
en.start()