# Create a variable date and store todays date then print it
import datetime
todaysdate = datetime.date.today()
print("Todays Date is:", todaysdate)

# Create a variable bd and take input birth date from user then print it
import datetime
bd = datetime.datetime.strptime(input("Enter your date of birth: "),'%Y-%m-%d').date()
print("Your birthday is:", bd)

# Create a variable ap and accept apple price from user, then print user’s apple price ap and its memory location, then next reassign apple price to 34, again print apple price and its memory location, finally delete variable ap
ap = int(input("Enter Apple Price: "))
print('Apple Price: ', ap, ' Memory location: ',id(ap))
ap = 34
print('Apple Price: ', ap, ' Memory location: ',id(ap))
del(ap)

# Create a variable gf and print any general fact and its data type?
statement = ' Sun rises in the east.'
print(statement, '\n' , 'data type: ', type(statement));

# Create a variable s and store number of subjects you are taking on this semester then print it and its data type?
s = 3
print(s, '\n', 'Datatype: ', type(s))

# Create a variable T and store current temperature then print it and its data type?
currenttemp = 72.8
print('Current Temp: ', currenttemp, '\n', "Datatype: " , type(currenttemp))

# Create a variable n, s, q and store your name, your favorite song and your favorite quote respectively. then print it?
n, s, q = 'sid', 'tum', 'be.here.now.'
print(n, s, q)

# Write any python code that you have learned before then describe your code by title of code, name, date, place
title, name, date, place = 'Hello World', 'sid', '12 Oct 2001', 'Hyderabad'
print(title, name, date, place)

# Create a list of your favorite subjects then print it and its data type?
subjects = ['math', 'comp', 'biology', 'philosophy']
print(subjects, '\n', 'datatype: ', type(subjects))

# Create a tuple of days in a week then print it and its data type?
daysinaweek = ('MOnday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(daysinaweek,'\n', 'datatype: ',  type(daysinaweek))

# Create a set of your favorite books then print it and its data type?
books = { 'one', 'two', 'three' }
print(books)
print(type(books))

# Create a football player and jersey pair of dictionary then print it and its data type?
footballplayers = {'Messi':'a', 'Ronaldo':'b'}
print(footballplayers)
print('Datatype:', type(footballplayers))

# Create a string variable name and store your name then copy it to a new variable, after that print both variables and their memory location?
name = 'sid'
print(name)
print(id(name))
newname = name
print(newname)
print(id(newname))

# Create two integer variables a and b accept values from a user then calculate their average?
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
average = (a + b) / 2
print(average)

# Create two integer variables avg and b accept from user then calculate their average using compound operators?
avg = int(input("Enter avg value: "))
b = int(input("Enter b value: "))
avg += b
avg / 2
print(avg)

# Create two variables my_age and friend_age accept from user then compare them?
my_age = input('Enter your age: ')
friend_age = input('Enter Friend"s age: ' )
if my_age > friend_age:
    print("You are older than your friend.")
elif my_age < friend_age:
    print("Your friend is older than you.")
else:
    print("You and your friend are the same age.")


# Create two variables a and b then compare them?
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a and b are equal")





