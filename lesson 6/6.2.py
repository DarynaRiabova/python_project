secund = input('Введіть кількість секунд:  ')
secund_number = int(secund)
if secund_number < 0 or secund_number > 8640000:
    print('Введіть число від 0 до 8640000')
else:
    days = secund_number // 86400
    remainder = secund_number % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    seconds = remainder % 60

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    print(f" {days} днів, {hours}:{minutes}:{seconds}")


