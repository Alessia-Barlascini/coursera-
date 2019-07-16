import re

handle = open('ufficial-test.txt')
num_list=[]
for line in handle:
    line.rstrip()
    #print(line)
    numbers = re.findall('[0-9]+',line)
    #print (numbers)
    numbers_int = map(int,numbers)
    num_list.extend(numbers_int)
print(sum(num_list))

