# create an empty dictionary
counts={}
print('Enter a line of text: ')
line = open(input(''))
#create the list
for lines in line:
    words = lines.split()

# add the element of the list to the empty dictionary and count them
    for word in words:
        counts[word]=counts.get(word,0)+1
print('Counts',counts)      # print the dictionary
for k,v in counts.items():
    print (k,v)             # print the element of the dictionary
