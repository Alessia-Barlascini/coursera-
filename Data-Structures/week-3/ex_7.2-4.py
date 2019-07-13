fname=input('Enter name file: ')
fhand=open(fname)
somma=0
conteggio=0
for line in fhand:
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        number=line[line.find('0'):]
        somma += float(number)
        conteggio += 1

print ('Avarage is:',somma/conteggio)

