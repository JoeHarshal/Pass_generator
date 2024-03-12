import string
import random

# hb stores all the characters
hb = string.ascii_letters + string.digits + string.punctuation

# length of password of user choice
length = int(input("Enter the length of the password: "))

# generate a password
# using the 'choices' function from the random 
# and joining the resulting characters into a string
password = ''.join(random.choices(hb, k=length))

# display the generated password to the user
print("Your password is:", password)