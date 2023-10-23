num1 = 42 # integer variable declaration
num2 = 2.3 # float variable declaration
boolean = True # boolean variable declaration
string = 'Hello World' # string variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # initialize tupple
print(type(fruit)) # print type check of variable fruit
print(pizza_toppings[1]) # access index 1 value from pizza_toppings list and print
pizza_toppings.append('Mushrooms') # add string "Mushrooms" to list pizza_toppings
print(person['name']) # access the value of the key "name" in the "person" dictionary and print
person['name'] = 'George' # change the value of the key "name" in the "person" dictionary
person['eye_color'] = 'blue' # change the value of the key "eye_color" in the "person" dictionary
print(fruit[2])

if num1 > 45: # create conditional if statement that runs if variable num1 is greater than 45
    print("It's greater")
else: # if the num1 variable is equal to or less than 45
    print("It's lower")

if len(string) < 5: # create conditional if statement that if the length of string is less than 5
    print("It's a short word!")
elif len(string) > 15: # create conditional if statement that if the length of string is greater than 15
    print("It's a long word!")
else: # if neither above is true print below
    print("Just right!")

for x in range(5): # print 0-4
    print(x)
for x in range(2,5): # print 2-4
    print(x)
for x in range(2,10,3): # print 2-10 in increments of 3
    print(x)
x = 0
while(x < 5): # print 0-4
    print(x)
    x += 1

pizza_toppings.pop() # remove that last item in pizza_toppings list
pizza_toppings.pop(1) # remove the item at index 1 from pizza_toppings list

print(person) # print person dict
person.pop('eye_color') # remove eye_color key:value pair from dict
print(person) # print person dict now without eye_color

for topping in pizza_toppings: #initialize for loop that iterates through pizza_toppings list
    if topping == 'Pepperoni': # once topping == pep, move to next statement
        continue
    print('After 1st if statement')
    if topping == 'Olives': # end for loop once topping in list == olives
        break

def print_hello_ten_times(): # creat function with no parameters
    for num in range(10): # initialize for loop that repeart 10 times
        print('Hello') # print hello 

print_hello_ten_times() # print hello 10 times

def print_hello_x_times(x): # create function that takes in one parameter x
    for num in range(x): # initialize for loop that repeats x times
        print('Hello') # print Hello

print_hello_x_times(4) # print hello 4 times

def print_hello_x_or_ten_times(x = 10): #create function that can take on arguement or none
    for num in range(x): #initialize for loop that loops x times
        print('Hello') # print hello

print_hello_x_or_ten_times() #print hello 10 times
print_hello_x_or_ten_times(4)# print hello 4 times


"""
Bonus section
"""

print(num3) #NameError: name <variable name> is not defined
num3 = 72
fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) #NameError: name <variable name> is not defined
print(pizza_toppings[7]) #IndexError: list index out of range
  print(boolean) #IndentationError: unexpected indent
fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'