#create a function to calculate avg of two numbers.
def average(a, b):
  return (a+b) / 2

print(average(4, 5))

#create a function to calculate a power b using eval function.
def powervalue(a, b):
  return eval('a**b')
  
print(powervalue(3, 3))

#create a function to calculate (return) sum and avg of two numbers.
def sumandaverage(a, b):
  sum = a + b
  average = (a + b) / 2
  return sum, average

print('Sum and average respectively: ', sumandaverage(12, 6))

#create a parametric function to check a number is odd or even.
def oddoreven(a):
  if a % 2 == 0:
    print(" It's Even!")
  else:
    print("Odd")
          
oddoreven(30)

#create a function to print student id and student name using keyword arguments
def studentidandname(id, name):
  print('Student Id:', id)
  print('Student Name:', name)

studentidandname(id= 12, name= 'Roy')

#create a function to print phone brand and phone price using positional keyword arguments 
def phonebrandandprice(brand, price):
  print('Phone Brand:', brand)
  print('Phone Price:', price)

phonebrandandprice('Samsung', price = 13000)

#create a function to print football player name and number of goals he scored using default arguments. default number = 0.
def playernameandgoals(name, goals=0):
  print("Player's Name:",name)
  print("Player's Goals:",goals)

playernameandgoals("Messi")

#create a function to print player name and other details of the player using variable length arguments.
def playernameanddetails(name, *details):
  print("Player's Name:", name)
  print("Details:", details)
  
playernameanddetails("Messi", 2, 'argentina')

#create a function to calculate average of two numbers and assign return value to a variable.
def average(a, b):
  return (a+b) / 2

averagevalue = average(4, 5)
print(averagevalue)

#create a function to calculate tan(45) using two other functions sine and cosine return values by using eval() function.
def tanvalue(a):

#create a function to calculate tan(45)by passing sine and cosine functions as paramenter eval() functions.

#create a function to calculate sum of all numbers from 1 to 100.
def sumofallnumbers(a, b):
    def calculate_sum(first, last):
        return sum(range(first, last + 1))
    
    total = calculate_sum(a, b)
    average = total / (b - a + 1)  # correct average of all numbers from a to b
    return total, average

total_sum, avg = sumofallnumbers(3, 300)
print("Sum:", total_sum)
print("Average:", avg)
  
#create a lambda function to calculate average of two numbers.
average = lambda a, b : (a + b) / 2

print(average(2, 3))

#create a filter function to check a number is odd or even.
numberslist = [1,2,3,4,5,6,7,8,9,10]
oddoreven = filter(lambda x: x % 2 == 0, numberslist)
print(list(oddoreven))

#create a list variable and store price of foods then print all food prices after 25% discount using map function.
priceslist = [1,2,3,4,5,6,7,8,9,10]
newprices = map(Lambda x: x - (x * 0.25), priceslist)
print(list(newprices))

#create a list variable and store your mid semester exam results of each subject and calculate avg using the reduce function.
from functools import reduce 

markslist = [1,2,3,4,5,6,7,8,9,10]
average = reduce(lambda x, y: x + y, markslist)
print(average)

#create a decorator to divide two numbers but if a number is divided by zero, print invalid.

#create a decorator to divide two numbers but if numerator is always greater than the denominator.

#create a generator to print top 3 atheles who finish olympic marathon 2019.
