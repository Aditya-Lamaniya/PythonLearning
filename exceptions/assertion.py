try:
    num=int(input("enter an even  number :"))
    assert num%2==0,"you have input non even number"

except AssertionError as obj:
    print(obj)

print("the program ends ")