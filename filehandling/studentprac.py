class student:
    major = 'cse'

    def __init__(self,enroll,name):
        self.enroll=enroll
        self.name=name
    def display(self):
        print(self.name)
        print(self.enroll)
        print(self.major)