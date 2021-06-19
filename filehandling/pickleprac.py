import pickle,studentprac

f = open("student.dat", "wb")
s = studentprac.student("208", "adi")
pickleprac.dump(s, f)
f.close()


