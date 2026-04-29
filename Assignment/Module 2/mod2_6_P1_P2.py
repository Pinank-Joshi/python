#not 6 you can enter howmany you want
n = int(input("Enter how any user detail you want to enter: "))

users = []

for i in range(n):
    user_id = int(input("Enter User Reg No.: "))
    user_name= input("Enter User Name: ")

    user ={
        "user_id" : user_id,
        "user_name" : user_name
    }

    users.append(user)

print(users)

for i in range(n):
    print(users[i]["user_name"])
