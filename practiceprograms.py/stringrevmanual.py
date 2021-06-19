#to reverse given string and check if its palindrome

def reverse(str):
    x=list(str)
    xr=[]
    for i in range(len(x)-1,-1,-1):
        xr.append(x[i])
    x=''.join(xr)
    return(x)

x=input("enter a string to check if its palindrome : ")
if x==reverse(x):print(" its  palindrom")
else: print("its not palaindrom")

# 2nd method

def rev(s):
    str=""
    for i in s:
        str=i+str
    return str

print(rev("hellow "))