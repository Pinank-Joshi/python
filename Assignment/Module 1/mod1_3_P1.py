# Create variable with diffrent data type

#only variable declared with their data type
my_name : str
my_number : int
is_auth : bool

#variable with their value inicialized
city = "Rajkot"
id_no = 101

# Inicialize the declared variables
my_name = input("Enter your name: ")
my_number = input("Enter your number: ")


passworld = input("Enter the password: ")

#inicialize boolian variable
if passworld == "Admin":
    is_auth = True

if is_auth == True:
    print(f"Name: {my_name} \nNumber: {my_number} \nCity: {city} and its type is {type(city)} \nID: {id_no} and its type is {type(id_no)}")