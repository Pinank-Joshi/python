student = []

name = input("Enter your name:  ")
student.append(name)

regno = int(input("Enter your Reg no. :  "))
student.append(regno)

cityname = input("Enter your city's name:  ")
student.append(cityname)

contectno = int(input("Enter your Contact no. :  "))
student.append(contectno)

for i in student:
    print(f"value {i} and it's type {type(i)}")

print(f"End length of list is {len(student)}")