#ask for a file
#open the file
#looking for lines of the form: X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values
#compute the average of those values and produce an output

fname=input('Enter name file: ')
fhand=open(fname)
for line in fhand:
    line=line.rstrip()
    print(line)
