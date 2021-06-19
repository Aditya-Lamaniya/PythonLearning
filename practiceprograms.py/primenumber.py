# program to check if any given number is prime number or not

x = int(input("enter the number to check if its prime or not :"))
if x == 0:
    print("the entered number is zero and its not prime")
elif x == 1:
    print("the given number is not prime ")
elif x==2 or x==3 or x==5 or x==7:
    print("the number is  prime")
elif x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
    print(" the given number is prime")
else:print("the given is not prime ")
