# check if the input is larger than a group of num. if true transform the input in the largest number

largest_so_far = int(input())
print('before', largest_so_far)
for the_num in [9, 40, 7, 78, 21]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('after', largest_so_far)



