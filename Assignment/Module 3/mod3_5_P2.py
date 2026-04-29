try:
    file = open("new1.txt",'r')
except:
    print("Error File not found")
finally:
    print("This is finally block and will execute all he time")
