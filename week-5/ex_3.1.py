# calculate pay
# no matter problem of input

hrs = input("enter working hours: ")
h = float(hrs)
pay = input("enter pay rate: ")
p = float(pay)

if h <= 40:
    print(p*h)
else :
    print(40*p+(h-40)*p*1.5)