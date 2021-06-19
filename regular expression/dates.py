import re

str=input("enter the date in dd/mm/yyyy format    :")
result=re.findall(r'\d{1,2}/\d{1,2}/\d{4}',str)
print(result)