fhand=open('romeo.txt')
memo=[]                     #create an empty list
for line in fhand:
    line=line.strip()
    list = line.split()
    for some in list:       #add elements to one unique list eliminating double
        if some not in memo:
            memo.append(some)
memo.sort()                 #organize the list
print (memo)