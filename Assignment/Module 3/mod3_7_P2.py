class id:

    id : int

    def get_id(self):
        self.id = int(input("Enter your ID: "))

class name:

    name : str

    def get_name(self):
        self.name = input("Enter your name: ")

class data(id,name):

    def show_data(self):
        print(f"User ID is : {self.id} and User name is : {self.name}")

d1 = data()
d1.get_id()
d1.get_name()
d1.show_data()