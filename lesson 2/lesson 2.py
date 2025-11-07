# 1 task
number = int(input('Введіть число:  '))
a = number ** 2
print(a)
# 2 task
print('Введіть число:  ')
first = int(input("Перше число: "))
second = int(input("Друге число: "))
third = int(input("Третє число: "))
result = (first + second + third)/3
print(result)
# 3 task
minutes = int(input('Введіть хвилини:  '))
hours = minutes//60
mins = minutes % 60
print(hours, 'години ', mins, ' хвилин' )
# 4 task
price =  int(input('Введіть ціну:  '))
discount = int(input('Введіть знижку у відсотках:  '))
final_price = price - price * (discount/100)
print(final_price)
# 5 task
full_number = int(input('Введіть ціле число:  '))
last_number = full_number % 10
print(last_number)
# 6 task
length =  int(input('Введіть довжину:  '))
width =  int(input('Введіть ширину:  '))
p = (length + width) * 2
print(p)
# 7 task
long_number =  int(input('Введіть 4-х значне число з клавіатури:  '))
b = long_number // 1000
c = long_number // 100 % 10
d = long_number // 10 % 10
e = long_number % 10

print(b)
print(c)
print(d)
print(e)