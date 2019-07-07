alessia = input("Enter a number > 0: ")
try:
    ival = int (alessia)
except:
    ival = -1

if ival > 0 :
    print ("nice work")
else:
    print ("not a number > 0")