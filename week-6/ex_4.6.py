# calculate salary from hours and pay rate input
# run the function only if the input are float

hrs = input("Enter your hours: ")
pay = input("Enter pay rate: ")

def computepay():
    if float(hrs)< 40:
        print(float(hrs) * float(pay))
    else:
        print(40 * float(pay) + (float(hrs)-40) * float(pay)*1.5)


# hrs: valuate if the function creates an error.
# true if the parameters are ok - false is not.
try :
    float(hrs)
    hours_validity = True
except :
    hours_validity = False
    print("Insert a valid hours number")


# pay: valuate if the function creates an error.
# true if the parameters are ok - false is not.
try :
    float(pay)
    pay_validity = True
except :
    pay_validity = False
    print("Insert a valid pay rate number")


# valuate if the function can run
if hours_validity == True and pay_validity == True:
    if float(hrs) > 0 and float(pay) > 0:
        computepay()
else:
    print ("Error")