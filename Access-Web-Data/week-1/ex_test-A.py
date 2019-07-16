# sum all the numbers in the text

import re
# open file
handle = open('test-1.txt')
num_list = []
for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)   # find all the numbers in the text
    num=map(int,stuff)                  # transform str into int
    num_list.extend(num)                # add all the int to the list
print(sum(num_list))                    # print the sum of the numbers in the list
