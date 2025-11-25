import string
import keyword

name = input("Введіть ім'я змінної:")

is_true = True

if len(name) == 0 or name[0].isdigit():
    is_true = False

if name in keyword.kwlist:
    is_true = False

if name.count("_") > 1:
    is_true = False

for ch in name:
    if ch.isupper():
        is_true = False
        break

if " " in name:
    is_true = False

for p in string.punctuation:
    if p != "_" and p in name:
        is_true = False
        break

print(is_true)