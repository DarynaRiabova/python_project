my_list = [1, 2, 3, 4, 5]
length = len(my_list)
if length > 2:
    last = my_list.pop()
    my_list.insert(0, last)
    result = my_list
else:
    result = my_list


print(my_list)