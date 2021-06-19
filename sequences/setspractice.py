#sets: sets do not allow duplicates 


s={}                               #null set 
s={3,-1,4.6,'whatever',0b1010}
print(s)

#insertion:  set doesnt keep order ,doesnt allow redudancy/repeating occurance  ,and also donot support slicing

s.update([55,88])
print(s)

#deletion 

s.remove(55)
print(s)

#frozen sets: doesnt allow update or removal 

f=frozenset(s)              #convert set into frozen set 
