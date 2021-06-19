# Private Fields and Name Mangling
class student:
    def __init__(self):
        self.__name = 'adi'
        self.__id = 2341234

    def display(self):
        print(self.__id)
        print(self.__name)


c = student()
c.display()
print(c._student__id);   # Name Mangling
print(c._student__name);