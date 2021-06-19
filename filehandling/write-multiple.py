f=open("filexp.txt","w")
print("enter text (please mark the end of string with ';' when done")
s=''
while s!=';':
    s= input()
    f.write(s)

f.close