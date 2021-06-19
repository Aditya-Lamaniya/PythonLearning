# illustration of class inheritance

class car:
    def __init__(self, make, model, year):
        self.make= make
        self.model = model
        self.year = year
    def start(self):
        print("engine start ")
    def stop(self):
        print("engine stop ")
class tata(car):
    def __init__(self, type , make, model, year):
        car.__init__(self,make,model,year)
        self.__type = type


vehicledata = tata('SUV', 'tata', 'harrier', '2020')
print(vehicledata.make)
print(vehicledata.model)
print(vehicledata.year)
print(vehicledata._tata__type);

vehicledata.start()
vehicledata.stop()
