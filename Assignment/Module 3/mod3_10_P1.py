import re

mystr="Hello This is My name Pinank!"

x=re.search("is",mystr)
print(x)

if x:
    print("Match done!")
else:
    print("Error!")