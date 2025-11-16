lst = [0,0,6,7,0,8]
zero_count = lst.count(0)
zero_lst = [0] * zero_count
result = []
for num in lst:
    if num != 0:
        result.append(num)

result.extend(zero_lst)

print(result)

