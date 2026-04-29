#list withassigned values
list1 = ["Apple","Banana","Mango"]

#Ask user what they want to find
user_input = input("What fruit you want to find in the list: ")


found = False
#find is there mango in given list with for loop
for i in list1:
    if i.lower() == user_input.lower():
        found = True
        break
    else:
        found = False

if found == True:
    print("Found")
else:
    print("Not Found")