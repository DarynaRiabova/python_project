lst = [0, 1, 7, 2, 4, 8]

if len(lst) == 0:
    result = 0
    print(result)
else:
    number = 0
    for num in lst:
        if lst.index(num) % 2 == 0:
            number = number + num
    result = number * lst[-1]
    print(result)
