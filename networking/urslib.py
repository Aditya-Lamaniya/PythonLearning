import urllib.request

try:
    url=urllib.request.urlopen("https://www.python.org/")
    content = url.read()

except urllib.error.HTTPError:
    print("the webpage not found ")
    exit()

f = open('python.html', 'wb')
f.write(content)
f.close()
