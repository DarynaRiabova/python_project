number = int(input('Введіть ціле число  '))
while number > 9:
    result = 1
    for d in str(number):
        result *= int(d)
    number = result

print(number)