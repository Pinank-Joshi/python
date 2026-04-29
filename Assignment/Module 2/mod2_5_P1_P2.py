tup1 = ("zero","one","two","three","four","five","six","seven","eight")

#printing values between index 1 to 5 exculding the index 1 and 5
print(tup1[2:5])

#printing values between index 1 to 5 including the index 1 and 5
print(tup1[1:6])

for i in range(0, len(tup1), 2):
    print(tup1[i])