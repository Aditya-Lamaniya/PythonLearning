class student:
    major = 'cse'

    def __init__(self,enroll,name):
        self.enroll=enroll
        self.name=name

s1=student(1,"s1")
s2=student(2,"s2")

print(s1.major)
print(s1.enroll)
print(s1.name)

print(student.major)  #GLOBAL VARIABBLES CAN BE ACCESSED THROUGH CLASS NAME 

print(s2.major)
print(s2.enroll)
print(s2.name)