# repeat asking for a number until the word done is entered
# print done
# find largest
# find smallest
# try/except to put out an appropriate message and ignore not valid number/strings

memo=[]

largest = None
smallest = None


while True:
    val=input()
    if val == 'done':
        break
    try:
        fval=int(val)
    except:
        print('Invalid input')
        continue
    memo.append(fval)

print ('Maximum is',max(memo))
print ('Minimum is',min(memo))