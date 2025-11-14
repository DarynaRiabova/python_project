my_list = [1, 2, 3, 4, 5, 6]
if len(my_list) == 0 :
    new_list = [[], []]
else:
    new_list = (len(my_list) +1) //2
    first_part = my_list[:new_list]
    second_part = my_list[new_list:]
    new_list = [first_part, second_part]
print(new_list)