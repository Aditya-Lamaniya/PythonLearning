#program to find average of given numbers by user

x = int(input("enter the number of count average  :"))
lst = []
total = 0
for i in range(x):
    print("enter element for index [", i, "]  :")
    lst.insert(i, float(input()))
    total += lst[i]

print("\n the average of all the numbers is = ", total / x)
