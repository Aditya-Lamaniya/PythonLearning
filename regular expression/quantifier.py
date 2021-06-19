import re

str=input("enter any string  :")
result=re.findall(r'h\w*',str)

print(result)

#?=check for only one character
#{n} = check for number of occurence
#n+  = one or more
#n*= zero or more
