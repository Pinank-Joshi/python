class user_data:

    user_id = 000
    user_name = "Default"

    def get_data(self):
        user_id = int(input("Enter user ID: "))
        user_name = input("Enter your name: ")
        print(f"User ID is : {user_id}\nUser name is: {user_name}")


u1=user_data()
u1.get_data()
#here we are print user id and name in function since they are in scope they are printing local value
#and down below we are printing same but from class variable giving default value
print(f"Default user ID is : {user_data.user_id} and user name is : {user_data.user_name}")