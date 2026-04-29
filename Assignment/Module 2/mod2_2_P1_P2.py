list1 = []

name = "Pinank"
city = "Rajkot"
mobile = "8200325761"

#first adding all the eliment in list using append
list1.append(name)
list1.append(city)
list1.append(mobile)

for i in list1:
    print(i)
print("Inicial data")
print(f"\n")

#adding element at specific index
list1.insert(2,"Insert")

for i in list1:
    print(i)

print("inserted data")
print(f"\n")


#removing index's element from the list using pop
list1.pop(3)

for i in list1:
    print(i)

print("after pop data")
print(f"\n")


#removing the element using its value
list1.remove("Rajkot")

for i in list1:
    print(i)

print("last data after remove")
print(f"\n")
