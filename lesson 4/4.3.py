import random
my_first_list = []
my_second_list = []
for i in range(random.randint(3, 10)):
    my_first_list.append(random.randint(1, 9))
my_second_list = [my_first_list[0], my_first_list[2], my_first_list[-2]]
print(my_first_list)
print(my_second_list)
