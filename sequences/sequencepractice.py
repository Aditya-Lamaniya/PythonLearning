#1string commands  .......

s="   whatever   "                              #singlew line string
print(s)     
s1="""well   
well
well"""                                         #multiple line string 
print(s1)
print(s[4])                                     #index in string
print(s*3)                                      #repeatation*n times 
print(len(s))                                   #pass lenth of string 

#2slicing string commands......

print(s[0:6])                               #print from s[0]-s[5] (s[a:n]..s[a]....s[n-1])
print(s[0:])                                #will print from s[a:] to end lenght 
print(s[:5])                                #will print from starting to s[:n]
print(s[-5:-1])                             # negative represent from backward ..note=*for s[-a:-s],a>s,-a<-s
print(s[0:7:2])                             #step jump value,,will print element of given indices, print(s[starting index:ending index:difference])
print(s[8::-1])                             # will reverse the above operation from back index of string 
print(s[::-1])                              #will reverse string same as above 

#3strip the space 

print(s.strip())                            #strip space from beginning and end 
print(s.lstrip())                           # strip space from left/beginning
print(s.rstrip())                           #strip space from right/end 

#4finding sub string 
print(s.find("ever"))                       # for s.find(sub) will find sub string 'sub', return -1 if fail to find 
print(s.find("ever",0,len(s)))              #("string",starting search index,ending search index 
print(s.count("e"))                         #return the number of occurance for given "sub string"
print(s.replace("a","i"))                   # replace sub string , stringname.replace("old substring","new sub string")
print(s.upper())                            #convert string to upper case 
print(s.lower())                            #convert string to lower case 
print(s1.title())                           #first word after white space becomes upper case,while all other becomes lower case 



