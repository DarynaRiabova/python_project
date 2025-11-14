first_number = int(input('Введіть число:  '))
second_number = int(input('Введіть число:  '))
operation = input('Введіть математичні дії (+, -, *, /):  ')
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        result = "Помилка!"
    else:
        result = first_number / second_number
else:
    result = "Помилка!Введіть математичні дії (+, -, *, /)"

print(result)
