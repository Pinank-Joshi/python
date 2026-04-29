#Calculator function
def calc():
    #ask user for input
    user_input = input("You can do 1. Addition 2. Subtraction 3. Multiplication 4. Division \n(For Example: 12 + 13, 100 / 10 (There is a space on the both side of opration)) \nEnter Expression you want to do: ")

    #process userinput 
    user_input = user_input.strip().split()
    user_input[0] = int(user_input[0])
    user_input[2] = int(user_input[2])
    
    #do operation as requested
    if user_input[1] == "+":
        print(f"Ans: {user_input[0] + user_input[2]}")
    
    elif user_input[1] == "-":
        print(f"Ans: {user_input[0] - user_input[2]}")
    
    elif user_input[1] == "*":
        print(f"Ans: {user_input[0] * user_input[2]}")

    elif user_input[1] == "/":
        print(f"Ans: {user_input[0] / user_input[2]}")

    else:
        print("Please Enter input as Given formate (For Example: 12 + 13, 100 / 10)")

#Grade Finder
def grade():

    #get user input
    user_input = input("(Consider You cannot get 100%)\nEnter your Percentage to findout Your Grade: ")

    #process user input
    user_input = user_input.strip()
    user_input = int(user_input[0] + user_input[1])

    #calculate Grades
    if user_input > 90 and user_input <= 100:
        print("Your garde is A+")

    elif user_input > 80 and user_input <= 90:
        print("Your garde is A")

    elif user_input > 70 and user_input <= 80:
        print("Your garde is B+")

    elif user_input > 60 and user_input <= 70:
        print("Your garde is B")

    elif user_input > 50 and user_input <= 60:
        print("Your garde is C")

    elif user_input > 40 and user_input <= 50:
        print("Your garde is D")

    elif user_input > 0 and user_input <= 40:
        print("Sorry You Failed")


#-------------------------------------------------------------------------------------------------------------------------#
# make a program to do both calculator as well as grade calculator
# first create calculator that works when selecting it in choice

#this will keep trak of which program to run
user_choice = ""

#this will ask user which program to run infinitely
while user_choice == 1 or 2:
    
    #take input from user what he want to do
    user_choice = int(input("What program you want to see ?\n1. Calculator \n2. Grade calculator \n3. Exit \nEnter choice: "))
    
    #if choice  is 1 do calculator
    if  user_choice == 1:
        calc()

    #if choice is 2 do greade finder
    elif user_choice == 2:
        grade()

    #end the program
    elif user_choice == 3:
        break

    #end the program
    else:
        break
