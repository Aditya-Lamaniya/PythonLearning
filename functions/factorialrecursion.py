# program to print factorial using recursion
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


y = int(input("enter the number to find factorial"))
z = factorial(y)
print("result= :", z)
