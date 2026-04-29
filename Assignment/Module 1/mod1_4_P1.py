#find gratest and lowest of 3 number
def more_less():
    
    val1 = input("Enter 1st Value: ")
    val2 = input("Enter 2nd Value: ")

    is_equal = False

    def more(val1,val2):

        if val1 > val2:
            print(f"Greatest is: {val1}")
        
        elif val2 > val1:
            print(f"Greatest is: {val2}")

        else:
            is_equal = True
    
    def less(val1,val2):

        if val1 < val2:
            print(f"Least is: {val1}")
        
        elif val2 < val1:
            print(f"Least is: {val2}")

        else:
            is_equal = True
    
    more(val1,val2)
    less(val1,val2)

    if is_equal == True:
        print("They are Equal")

    is_equal = False

def  prime():
    
    user_input = int(input("Enter Number you want to Check: "))

    if user_input <= 1:
        print("Not Prime")
    
    else:

        is_prime : bool
        
        for i in range(2,user_input):
            
            if user_input % i == 0:
                is_prime = False
                break

            else:
                is_prime = True

            i = i + 1

    if is_prime == True:
        print("Prime")

    else:
        print("Not Prime")

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


def bcheck():
    user_bt = input("We only need A+ type blood what is your blood type?: ")
    if user_bt.lower() == "a+":
        btat = input("Do you have Tattoo on your body: ")
        if btat.lower() == "no" or "n":
            illcheck = input("Are you currently suffering from any illness?: ")
            if  illcheck.lower() == "no" or "n":
                print("You are ready to Donate Blood!!")
            else:
                print("sorry you cannot donate Blood")
        else:
            print("sorry you cannot donate Blood")
    else:
        print("sorry you cannot donate Blood")

user_choice = ""

#this will ask user which program to run infinitely
while user_choice == 1 or 2 or 3 or 4 or 5:
    
    #take input from user what he want to do
    user_choice = int(input("What program you want to see ?\n1. Grater or Less \n2. Check Prime \n3. Grade calculator \n4. Check Blood Donate Eligibility \n5. Exit \nEnter choice: "))
    
    #if choice  is 1 do moreless
    if  user_choice == 1:
        more_less()

    #if choice is 2 do prime ,notprime
    elif user_choice == 2:
        prime()

    #if choice is 3 do grade calculator
    elif user_choice == 3:
        grade()

    #if choice is 4 do check blood donate eligibility
    elif user_choice == 4:
        bcheck()

    #end the program
    elif user_choice == 5:
        break

    #end the program
    else:
        break