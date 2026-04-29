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


calc()