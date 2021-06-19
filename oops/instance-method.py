class lessons:
    def __init__(self, name, ratings):
        self.name = name
        self.rating = ratings

    def average(self):
        numrat = len(self.rating)
        avrg = sum(self.rating) / numrat
        print("average rating of ",self.name," is ",avrg)

c1 = lessons('corejava', [1, 2, 3, 4, 5])
print(c1.name)
print(c1.rating)
c1.average()
c2 = lessons('python', [5, 3, 4, 4, 5])
print(c2.name)
print(c2.rating)
c2.average()
