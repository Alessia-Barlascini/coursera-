counts={}                                       #create an empty dictionary
handle=open('il-piccolo-principe.txt')

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1     # add keys to the dictionary

bigcount=None                                   # create the base to count the values
bigword=None                                    # create the base to associate the keys

for word,count in counts.items():
    if bigcount is None or count > bigcount:    # find the biggest values
        bigword=word
        bigcount=count
print(bigword,bigcount)