tup1 = ()
list1 = []

n = int(input("How many element you want in tuple: "))

for i in range(n):
    user_input = input("Value: ")
    list1.append(user_input)

tup1 = tuple(list1)

print("------------------------------------")
print("Inicial tuple")
for i in tup1:
    print(i)


tup2 = (102,205,603,904)

tup3 = tup1 + tup2
print("------------------------------------")
print("Tuple no 3 with str + Int data")
for i in tup3:
    print(i)

print("Accessing 1st element using index")
print(tup3[0])