import string 
import random
print("""So You 
Want A New/Better
Password Huh...
""")
pass_len = int(input("How many characters\nWould like in Your new\npassword?:\n"))
all_characters = string. ascii_letters + string.digits + string. punctuation 
password = ""
for char in range(pass_len):
    random_len = random.choice (all_characters)
    password = password + random_len
    
print("Your *NEW* password is...\n")
print(f"{password}\n\n(Make sure \nYOU WRITE IT\ndown...)")