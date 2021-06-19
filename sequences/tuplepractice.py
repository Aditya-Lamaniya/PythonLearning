#tuple :_ cannot be modified , immutable ,read only 

t=(1,5,2.3,'whatever',22/7)                          #basic tuple,
print(t)
t1=(9,)                                              #single element tuple 
print(t[2])                                          #indexing in tuple
print(t*2)                                           #repeating tuple
print(t.count(5))                                    #count repeating occurance of given element 
print(t.index('whatever'))                           #return index of searched element 

l=[1,2,3,4]
t2=tuple(l)                                           #convert list into tuple
print(t2)
print(type(t2))
l2=list(t2)                                           #convert tuple into list
print(l2)
print(type(l2))                                              