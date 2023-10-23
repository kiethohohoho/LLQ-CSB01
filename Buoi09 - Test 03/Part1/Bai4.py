def is_palindrome(text):
  return text == text[::-1] 

text = input("Input a text: ")
if is_palindrome(text):
  print("This is a palindrome.")
else:
  print("This is not a palindrome.")
