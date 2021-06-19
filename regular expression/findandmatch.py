import re

try:
    str = input("enter any string ")
    result = re.search(r'o\w', str)
    print(result.group())

    result = re.findall(r'o\w', str) #find
    print(result)

    result=re.findall(r'o\w\w',str)
    print(result)

    result=re.match(r'a\w\w',str) #match
    print(result.group())

except:
    print("no matching pair found")
