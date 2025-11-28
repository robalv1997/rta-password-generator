import random
import string
import pyperclip

print("Password Generator")
print("------------------")

# ---- LENGTH OPTIONS ----
print("\nChoose password strength:")
print("1) Weak (8 characters)")
print("2) Medium (12 characters)")
print("3) Strong (16 characters)")
print("4) Custom length")

strength_choice = input("\nEnter option (1–4): ")

if strength_choice == "1":
    length = 8
elif strength_choice == "2":
    length = 12
elif strength_choice == "3":
    length = 16
elif strength_choice == "4":
    length = int(input("Enter custom password length: "))
else:
    print("Invalid choice. Defaulting to 12 characters.")
    length = 12

# ---- CHARACTER TOGGLES ----
print("\nInclude the following?")
use_upper = input("Uppercase letters (Y/N): ").strip().lower() == "y"
use_lower = input("Lowercase letters (Y/N): ").strip().lower() == "y"
use_numbers = input("Numbers (Y/N): ").strip().lower() == "y"
use_symbols = input("Symbols (Y/N): ").strip().lower() == "y"

characters = ""

if use_upper:
    characters += string.ascii_uppercase
if use_lower:
    characters += string.ascii_lowercase
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

# Safety check — prevent empty character set
if characters == "":
    print("\nERROR: You must select at least one character type.")
    input("\nPress Enter to exit...")
    exit()

# ---- PASSWORD GENERATION ----
password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:", password)

# ---- CLIPBOARD ----
pyperclip.copy(password)
print("\nPassword has been COPIED to clipboard!")

input("\nPress Enter to exit...")
