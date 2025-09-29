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


# Create a list of name of grade 10 students then classify them as Section 10A and Section 10B students?  


# Create a list of name of grade 10 students then add extra student ‘John’ then copy the list?  


# Create a nested list of name of grade Section 10A and Section 10B students then add extra student ‘John’ then copy the list? 


# Create a list in range 1 to 10 first the computer picks one number and you guess that number then if your guess is correct, you win else you lose? 


# Create a list of random five numbers then check whether there is duplicated number or not if it is there delete it, if sum of all numbers is even print maximum of the list else print minimum of the list.   


# Create a list of random three numbers 1 to 10, then if 2 is in the list duplicate the list else delete the list?   


# Create a tuple of random three numbers 1 to 10, then if 2 is in the tuple sort the tuple else reverse sort then unpack the tuple? 


# Print all multiples of 7 from 1 to 100 using while loop?


# Print Fibonacci Sequence till 50? A Fibonacci Sequence is a series of numbers where each number is the sum of the two numbers that precede it. 0, 1, 1, 2, 3, 5, 8, …


# Find factorial (n!) of given number from user?


# Print all perfect square numbers from 0 to 100?


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


