import string

name = input("Введіть рядок:")

clean_text = ""
for ch in name:
    if ch in string.punctuation or ch == " ":
        clean_text += " "
    else:
        clean_text += ch

words = clean_text.split()
capitalized_words = [w.capitalize() for w in words]

hashtag = "#" + "".join(capitalized_words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)