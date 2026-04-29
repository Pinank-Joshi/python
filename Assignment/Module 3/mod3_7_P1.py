class write:

    user_id : int
    user_name : str

    def get_data(self):
        self.user_id = int(input("Enter user ID:"))
        self.user_name = input("Enter user name:")

class read(write):

    def print_data(self):
        print(f"User ID is : {self.user_id} and user name is : {self.user_name}")

o1 = read()
o1.get_data()
o1.print_data()