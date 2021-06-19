# no slicing or repeatition on bytes, bytesarray allow indexing 

l=[22,11,4,7,2,4]
b=bytes(l)          #converting into 
print(type(b))

b1=bytearray(l)      #converting into bytesarray
b1[3]=5              #indexing in bytearray
print(b1)
