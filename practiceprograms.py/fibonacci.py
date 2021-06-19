# a program to print fibonacci series up to nth term

x = int(input("enter the nth term for fibonacci series :  \n\t"))
first = 0
second = 1
print(first, "\n", second)
for i in range(x):
    third = first + second
    first = second
    second = third
    print(third)
