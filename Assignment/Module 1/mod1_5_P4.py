
#Ask user what hight pyramid user want
user_input = int(input("What hight pyramid you want: "))

#make pyramid
for raw in range(1,user_input+1):
    for colum in range(raw):
        print("*",end="")
    print("") 