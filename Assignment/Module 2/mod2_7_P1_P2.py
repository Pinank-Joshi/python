keys = []
values = []
dict1 =  {
    "id" : 101,
    "name" : "Pinank",
    "city" : "Rajkot",
    "email" : "Pinank.joshi@gmail.com"
}

print(dict1)

dict1["id"] = 202


print(f"after the Update using key\n",dict1)


print("Keys are = ")
keys.append(dict1.keys())  

print(keys)

print("values are = ")
values.append(dict1.values())  
print(values)