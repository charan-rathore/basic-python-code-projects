letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
import random
# pass_word = ""
# for i in range (0,nr_letters):
#     pass_word+=random.choice(letters)
# for i in range (0,nr_symbols):
#     pass_word+= random.choice(symbols)
# for i in range (0 , nr_numbers):
#     pass_word+= random.choice(numbers)
# print(pass_word)

#hard version
hard_pass = []
for i in range (0,nr_letters):
    hard_pass+=random.choice(letters)
for i in range (0,nr_symbols):
    hard_pass+= random.choice(symbols)
for i in range (0 , nr_numbers):
    hard_pass+= random.choice(numbers)
random.shuffle(hard_pass)
pass_ = ""
for char in hard_pass:
    pass_ += char
print(pass_)

