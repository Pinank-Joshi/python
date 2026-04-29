file=open("new.txt","r")

print("Inicial:")
print(file.read())
file.close()

file_open=open("new.txt","a")
file_open.write("Hi this is multiple string insert\n")
file_open.write("Hi this is second string")
file_open.close()

file=open("new.txt","r")
print("Updated:")
print(file.read())
file.close