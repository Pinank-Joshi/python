keys = [101,202,303,404]
values = ["Pinank","Om","Rutvik","Dhruv"]

dict1 = {}

#here I am Assuming both list have same number elements
for i  in range(len(keys)):
    dict1[keys[i]] = values[i]

print(dict1)