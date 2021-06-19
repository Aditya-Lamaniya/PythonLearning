# search using RE: re.search

import re

str = input("enter any string ")
result = re.search(r'o\w', str)
print(result.group())
result = re.findall(r'o\w', str)
print(result)
count=0
for i in range(len(str)):
 if str[i].islower():
    count+=1
 elif str[i].isupper():
    count+=1
 elif str[i].isnumeric():
    count+=1

print(count)
