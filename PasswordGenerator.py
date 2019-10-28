import random

length = 0
letter_count =0
number_count = 0

while length<6:
    length = int(input("Enter the length of the password>"))

letter_count = int(input("Enter letter count>"))
number_count = int(input("Enter number count>"))

lowercase ="abcdefghijklmnopqrstuvwxyz"
uppercase ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
punctuation = "!@#$%^&*()_"
password = ''

for x in range(letter_count):
    password += random.choice(lowercase)+random.choice(uppercase)

for x in range(number_count):
    password += random.choice(numbers)

for x in range(length-letter_count-number_count):
    password += random.choice(punctuation)

password = "".join(random.sample(password,len(password)))


print(password)

