# calculate pay
# focus on not valid input


hrs = input("Enter Hours: ")
pay = input("Enter Pay: ")
try:
    p = float(pay)
    h = float(hrs)
except:
    print("ERROR: Please, enter a valid number")

if h <= 40:
    print(p * h)
else:
    print(40 * p + (h - 40) * p * 1.5)

# program run also using str:
# ValueError: could not convert string to float: 'fgs'
# program runs also using negative numbers
