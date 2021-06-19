# program to remove duplicated element from list
l1 = []
l2 = []
x = int(input("enter the size of list "))
for i in range(x):
    print("enter element for index [", i, "]  :")
    l1.insert(i, input())
for i in l1:
    if i not in l2:
        l2.append(i)
print("list after removing duplicated element=", l2)
