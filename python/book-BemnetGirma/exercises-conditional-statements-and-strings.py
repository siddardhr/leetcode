# Create a variable "age" and take input from user then check vote eligibility (age > 18)?
age = int(input("Enter your age: "))
if age > 18:
    print("Vote ELigible")
else:
    print("Not Eligible yet.")
  
# Create a variable "username" and its value is your name then create log in conditional statement based on username?
username = 'sid'
userinput = input("Enter the username: ")
if userinput == username:
    print('Successful')
else:
    print("Please enter correct username!")

# Create two variable and "nationality" and "cgpa" and store values is your name and nationality, then create scholarship conditional statement based on nationality and cgpa?
nationality = 'asian'
cgpa = 9
usernationality = input('please enter your nationality: ')
usercgpa = float(input("Please enter your cgpa in numbers: "))
if usernationality == nationality and usercgpa >= cgpa:
    print("Scholarship eligible.")
else:
    print("Scholarship isn't granted.")

# Create two variable "username" and "password" and store values is your name and password, then create log in conditional statement based on username and password?
username = 'sid'
password = 'newpassword'
usernameinput = input('Enter the username:')
passwordinput = input('Enter the password:')
if usernameinput == username and passwordinput == password:
  print("Login Successful")
else: 
  print("Login Failed")

# Create a variable "score" and take input from user, then classify them based on their score?
score = int(input("Enter your score: "))
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 50:
    print("Average")
elif score >= 35:
    print("Below Average")
else:
    print("Fail - Needs Improvement.")

# Create two integer variables "a" and "b" take input from a user, then calculate their average by using eval() function?
a , b = int(input("Enter a value: ")), int(input("Enter b value: "))
print("Average of both values: ", eval("(a + b) / 2"))

# Calculate ln(e), cos(90°), 10 the power of 5, Square root of 625, Ceil and Floor of 6.5

# Create a string variable "name" and store your name then print only vowel letters from your name?
name = input("Enter your last name: ")
vowels = 'aeiouAEIOU'
for char in name:
    if char in vowels:
        print(char, end="")

# Create a string variable "quote" and store your favorite quote then print each words from the quote?
quote = "you are not the body or mind"
print(quote.split(" "))

# Create four string variables "UPPER", "lower", "Symbols", "digits" and store uppercase letters, lowercase letters, special symbols and digits(0-9) respectively then create a password which contains all of them?
import string
import random

UPPER = string.ascii_uppercase
lower = string.ascii_lowercase
symbols = string.punctuation
digits = string.digits

password_chars = [random.choice(UPPER), random.choice(lower), random.choice(symbols), 
                 random.choice(digits)]
                 
allchars = UPPER + lower + symbols + digits
password_chars += random.choices(allchars, k = 6)

password = "".join(password_chars)

print(password)

# Create a string variable "quote" and store your favorite quote then find length of the quote?
quote = "you are not the body or mind"
char_length = 0
for char in quote:
    char_length = char_length + 1
print(char_length)
print(len(quote))

# Create a string variable "name" and store a string “Yonatan” then remove all vowel letters from the string?
name = 'Yonatan'
vowels = 'AEIOUaeiou'
result = ''

for char in name:
  if char not in vowels:
    result = result + char
print(result)

# Create username validation program excluding whitespace?
username = 'woman123'
userinput = input('Please enter the username: ')
cleanusername = userinput.replace(" ", "")
if username == cleanusername:
    print("Username matched.")
else:
    print("username not correct.")

# Create a string variable "quote" an store your favorite quote then find letter "x" in the quote?
quote = "you are not your body or mind xyz" 
for char in quote:
  if char == 'x' or char == 'X':
    print(char)

# Create a string variable "quote" and store your favorite quote then find index of letter "a" in the quote?
quote = "you are not your body or mind xyz" 
for index, char in enumerate(quote):
    if char == 'a' or char ==  'A':
        print(f"Char a found at {index}")

# Create a string variable "name" and store your name then find no. of vowel letters in your name?
name = 'New man name is here'
vowels = 'AEIOUaeiou'
charcount = 0
for char in name:
  if char in vowels:
    charcount += 1
print(charcount)

# Create a string variable "email" and store your gmail then convert it into yahoo mail?
email = 'siddardh@gmail.com'
email = email.replace("gmail.com", 'yahoo.com')
print(email)

# Create a string variable "name" and store your full name then split it?
fullname = 'New man name is here'
splitedname = fullname.split()
print(splitedname)

# Create a list variable "name" and store your first name, your middle name and surname then join it?
name = ['new', 'man', 'name']
print(" ".join(name))

# Create a Instagram username validation program using the following rules? Minimum 5 characters Maximum 10 characters Only lowercase letters Underscore and dot is allowed Whitespace, symbol are not allowed
import string

allowedchars = string.ascii_lowercase + '._'

enteredusername = input("Please enter username: ")
if 5 <= len(enteredusername) <= 10:
  if all(char in allowedchars for char in enteredusername):
    print("valid username")
  else:
    print('Inavlid chars')
else:
  print("only 5 - 10 chars allowed")




