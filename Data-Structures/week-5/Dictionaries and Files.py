# create an empty dictionary
counts={}
print('Enter a line of text: ')
line = input('')
#create the list
words = line.split(' ')



# add the element of the list to the empty dictionary and count them
for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts',counts)
for k,v in counts.items():
    print (k,v)