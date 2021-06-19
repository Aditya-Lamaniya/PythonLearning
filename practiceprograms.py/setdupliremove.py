# program to remove duplicate element using set conversion
#drawback= set doesnt keep order
lst = []
x = int(input("enter size of list  :"))
for i in range(x):
    print("enter element for index [", i, "]  :")
    lst.insert(i,input())
s = set(lst)
print("new set =", s)
