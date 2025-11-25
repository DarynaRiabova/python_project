while True:
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
        result = "Помилка! Введіть дію (+, -, *, /)"

    print("Результат:", result)

    start_new_operation = input('Чи хочете продовжити? (yes):  ')

    if start_new_operation.lower() not in ("yes"):
        print("Роботу завершено.")
        break
