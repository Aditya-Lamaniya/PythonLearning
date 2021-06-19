d={1:"hello",2:"there",3:"whatever"}                        #basic dictionary
print(d)
print(d.items())                                            #will return the items in dictionary
k=d.keys()                                                  #will return all key index in dictionary
for i in k: print(i)
v=d.values()                                                #will return the value in dictionary
for i in v: print(i)

# indexing 

print(d[2])                                                 #will print the value for given key 

del d[2]                                                    #will delete value of of particular given key 
print(d)