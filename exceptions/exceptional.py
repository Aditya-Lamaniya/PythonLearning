try:
    a,b=[int(x) for x in input("enter two numbers ").split(" ")]
    c=a/b
    print(c)
except ZeroDivisionError:
    print("please enter non zero value ")

