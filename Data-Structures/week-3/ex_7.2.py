#ask for a file
#open the file
#looking for lines of the form: X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values
#compute the average of those values and produce an output

from statistics import mean
memo=[]
fname=input('Enter name file: ')
fhand=open(fname)
for line in fhand:
    line=line.rstrip()
    # print(line) - check if the file is right
    if line.startswith('X-DSPAM-Confidence:'):      #find line stanting with ....
        line=line[line.find('0'):]                  #extract numerical part
        line=float(line)                            #tranform into float
        line= memo.append(line)                     #tranform line into a list
#print (memo)
#print(len(memo))
#print (line)
average=mean(memo)
print('Average spam confidence:',average)



