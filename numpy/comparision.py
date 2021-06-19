from numpy import *

a1=array([10,20,50,70,90])
a2=array([20,40,60,80,100])

print(a1>a2)
print(a2<a1)

print(any(a1>=a2))
print(all(a2>a1))