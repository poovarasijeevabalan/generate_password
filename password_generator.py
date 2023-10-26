import random
import string 


def generate_password(min_length, numbers = True, special_charater = True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation 

  # print(letters, digits, special)

  charater = letters
  if numbers:
    charater += digits

  if special_charater:
    charater += special

  pwd = ""
  meets_criteria = False
  has_number = False
  has_special = False

  while not meets_criteria or len(pwd) < min_length:
    new_char = random.choice(charater)
    pwd += new_char

    if new_char in digits:
      has_number = True
    elif new_char in special:
      has_special = True
    

    meets_criteria = True
    if numbers:
      meets_criteria = has_number

    if special_charater:
      meets_criteria = meets_criteria and has_special

  return pwd
min_length = int(input('enter the minimum length of password :- '))

has_number = input('do you want to number(y/n)? ').lower() == 'y'
has_special = input('do you want to special charator(y/n)? ').lower() == 'y'

pwd = generate_password(min_length, has_number, has_special)
print('The generated password is ', pwd)
