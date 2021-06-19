import os,sys

x=input("enter file name :")
if os.path.isfile(x):
    print("the file exist in system")
else:
    print("error:file not found")