class flight:
    def __init__(self,engine):
        self.engine=engine

    def startengine(self):
        self.engine.start();

class airbusengine:
    def start(self):
        print("engine start boing ")

class boingengine:
    def start(self):
        print("engine start : boing ")

ae= airbusengine()
f= flight(ae)
f.startengine()

boi=boingengine()
f1=flight(boi)
f.startengine()