# check if the input is larger than a group of num. if true transform the input in the largest number


largest = int(input())
print('before', largest)
for the_num in [9, 40, 7, 78, 21]:
    if the_num > largest:
        largest = the_num
    print(largest, the_num)
print('after', largest)



