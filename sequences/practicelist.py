# list :python support multiple data type string 

l=[1,3.0,-20,"whatever"]
print(l)

print(l[3])                                                                 #indexing 
print(l[1:3])                                                               #indexing range 
print(l*2)                                                                  #repeatation
print(len(l))                                                               #print lenght of list

#insert methods 

l.append(70)                                                             #add new element at the end of the list 
l.insert(2, 22/7)                                                        #list name.insert(index, object)
print(l)

#deletion methods 
l.remove("whatever")                                                    #remove the selected object from the list 
del(l[2])                                                               #delete element at given index 
print(l)

#finding specific element in list 

print(max(l))                                            #return maximum/highest value element 
print(min(l))                                            #return minimum/lowest value element 
l.sort()                                                 #will sort the list,ascending order 
print(l)
l.sort(reverse=True)                                     #will sort the list,descending order 
print(l)

# clearing whole list 
l.clear()  #clear all element from list 
print(l)

