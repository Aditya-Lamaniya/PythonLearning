import re

str=input("enter the string ")

result=re.split(r'\d+',str)
print("result = ",result)