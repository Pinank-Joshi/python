list1 = []
n = int(input("How many element you want to enter: "))

for i in range(n):
    user_input = input("Value: ")
    list1.append(user_input)

print("orignal list")

for i in list1:
    print(i)

list1.sort()
print(" ")
print("orignal list sorted")
for i in list1:
    print(i)


#Sorted not working