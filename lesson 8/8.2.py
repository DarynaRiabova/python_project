import string
def is_palindrome(text):
   new_text =  "".join(char for char in text if char not in string.punctuation + " ")
   lowercase = new_text.lower()
   reversed_text = "".join(reversed(lowercase))
   if lowercase == reversed_text:
       return True
   else:
       return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
