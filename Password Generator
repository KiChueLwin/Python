import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_amount = int(input("Enter the amount of letters :"))
number_amount = int(input("Enter the amount of numbers :"))
symbol_amount = int(input("Enter the amount of symbols :"))

letter_lst = []
number_lst = []
symbol_lst = []

for i in range(0 , letter_amount ):
    letter = letters[random.randint(0, len(letters) - 1)]
    letter_lst.append(letter)

for i in range(0, number_amount):
    number = numbers[random.randint(0,len(numbers) -1)]
    number_lst.append(number)

for i in range(0, symbol_amount) :
    symbol = symbols[random.randint(0,len(symbols) -1)]
    symbol_lst.append(symbol)

password = letter_lst + number_lst + symbol_lst
random.shuffle(password)
password_str ="".join(password)
print(f"Your password is {password_str}")


