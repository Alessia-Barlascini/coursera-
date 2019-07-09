# repeat asking for a number until the word done is entered
# print done
# find largest
# find smallest
# try/except to put out an appropriate message and ignore not valid number/strings


while True:
    val=input('enter a number: ')
    if val == 'done':
        break
    try:
        fval=float(val)
    except:
        print('enter a VALID number')
        continue
    print (fval)
