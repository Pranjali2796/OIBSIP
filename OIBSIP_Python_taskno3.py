import random
import string

print("*** Random Password Generator ***")

length = int(input("Enter password length: "))

use_letters = input("Include letters? (yes/no): ").lower()
use_numbers = input("Include numbers? (yes/no): ").lower()
use_symbols = input("Include symbols? (yes/no): ").lower()

characters = ""

if use_letters == "yes":
    characters += string.ascii_letters   

if use_numbers == "yes":
    characters += string.digits          

if use_symbols == "yes":
    characters += string.punctuation    


if characters == "":
    print("Error: Please select at least one character type.")
else:
    
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)
