#ask for a file
#open the file
#print the contents of the file in upper case

fname = input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    line=line.rstrip()
    line=line.upper()
    print (line)
