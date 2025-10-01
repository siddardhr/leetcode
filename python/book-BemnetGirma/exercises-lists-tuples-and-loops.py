# Create a list of your email, name, gender and age, then print your name?
mydetails = ['name','email','gender',40]
print(mydetails[0])

# Create a list of your email, name, gender and age, then print your name and age?
mydetails = ['name','email','gender',40]
print(f'age: {mydetails[3]}, name: { mydetails[3]}')

# Create a list of your email, name, gender and age, then update your email and print index of all elements in the list?
mydetails = ['name','email','gender',40]
mydetails[1] = 'updatedemail'
for index, element in enumerate(mydetails):
  print(index, element)

# Create a list of your email, name, gender and age, then append your password and insert your username to the list at index 1?  
mydetails = ['name','email','gender',40]
mydetails.append('password')
mydetails.insert(1,'username')
print(mydetails)

# Create a list of your email, name, gender and age, then create another list which contains your birth date, month, year and extend/add it to former list? 
mydetails = ['name','email','gender',40]
birthdetails = [12,'month',1901]
mydetails.extend(birthdetails)
print(mydetails)

# Create a list of your email, name, gender and age, then if the email is not gmail delete it, if the gender is male delete all elements from the list?  
mydetails = ['name','a@yahoo.com','male',40]
if not mydetails[1].endswith('gmail.com'):
  del mydetails[1]
if mydetails[1] == 'male':
  mydetails.clear()
print(mydetails)

# Create a list of name of grade 10 students then sort them from A to Z and Z to A? 
names = ['Student', 'tudent', 'udent', 'dent', 'ent' ,'nt', 'list', 'of', 'studens', 'names']
print(names.sort())
print(names.sort(false))

# Create a list of name of grade 10 students then classify them as Section 10A and Section 10B students?  
names = ['Student', 'tudent', 'udent', 'dent', 'ent' ,'nt', 'list', 'of', 'studens', 'names']
section10A = names[0:5]
section10B = names[5:]
print(section10A, section10B)

# Create a list of name of grade 10 students then add extra student ‘John’ then copy the list?  
names = ['Student', 'tudent', 'udent', 'dent', 'ent' ,'nt', 'list', 'of', 'studens', 'names']
names.extend(['John'])
newnames = names.copy()
print(names)
print(newnames)

# Create a nested list of name of grade Section 10A and Section 10B students then add extra student ‘John’ then copy the list? 
import copy
names = [['Student', 'tudent', 'udent', 'dent', 'ent' ],['nt', 'list', 'of', 'studens', 'names']]
names.extend(['John'])
newnames = copy.deepcopy(names)
print(newnames)

# Create a list in range 1 to 10 first the computer picks one number and you guess that number then if your guess is correct, you win else you lose? 
import random

randomnumber = random.randint(1, 10)
usernumber = int(input("Please enter your choice: "))
if randomnumber == usernumber:
    print("You guessed it right. You won.")
else:
    print(f"You lost. The actual number was {randomnumber} Try again")

# Create a list of random five numbers then check whether there is duplicated number or not if it is there delete it, if sum of all numbers is even print maximum of the list else print minimum of the list.   
import random

numbers = [random.randint(1, 10) for _ in range(5)]
numbersset = set(numbers)
totalvalue = sum(numbersset)
print(numbersset)

if totalvalue % 2 == 0:
    print(max(numbersset))
else:
    print(min(numbersset))

# Create a list of random three numbers 1 to 10, then if 2 is in the list duplicate the list else delete the list?   
import random 

onetotenlist = [random.randint(1,10) for _ in range(5)]
duplicatelist = []  
if 2 in onetotenlist:
    duplicatelist = onetotenlist.copy()
if duplicatelist:
    print("Duplicated list:", duplicatelist)
else:
    print("2 was not found in the list.")


# Create a tuple of random three numbers 1 to 10, then if 2 is in the tuple sort the tuple else reverse sort then unpack the tuple? 


# Print all multiples of 7 from 1 to 100 using while loop?


# Print Fibonacci Sequence till 50? A Fibonacci Sequence is a series of numbers where each number is the sum of the two numbers that precede it. 0, 1, 1, 2, 3, 5, 8, …


# Find factorial (n!) of given number from user?


# Print all perfect square numbers from 0 to 10?
# Print all prime numbers from 0 to 100?


# Find sum of all prime numbers from 0 to 100?


# Print all vowels in a given string from user?


# Print all prime numbers from 1 to 100 except numbers divisible by 3?


# Print all even digits in a number from user?


# Print all vowels in a given string from user?


# Create a list using list comprehension that includes only the prime numbers from the original list? 


# Draw an Isosceles Triangle /Christmas Tree/ pattern which looks like as follows. Enter the number of rows: 4


# Draw Life Span /Hour Glass/ pattern which looks like as follows Enter the number of rows: 4


# Build a 6 by 6 multiplication table which looks like as follows Enter the number of rows: 6


# Draw an Alphabetical Triangle pattern which looks like as follows. Enter the number of rows: 4


