import string
user_string = input('Введіть через дефіс дві літери:  ')
first, second = user_string.split('-')
letters = string.ascii_letters
start = letters.index(first)
end = letters.index(second)
print(letters[start:end+1])

