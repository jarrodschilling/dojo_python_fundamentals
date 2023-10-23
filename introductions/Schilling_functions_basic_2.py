#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(x):
    countdown_list = []
    for i in range(x, -1, -1):
        countdown_list.append(i)
    
    return countdown_list

# print(countdown(8))

#2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_return(two_num):
    print(two_num[0])
    return two_num[1]

# print(print_return([1,9]))

#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def fpl(x):
    i = x[0] + len(x)
    return i

check = [1,2,3,4,5]
# print(fpl(check))

#4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def greater_second(x):
    yes = []
    if len(x) < 2:
        return "False"
    else:
        for i in x:
            if i > x[1]:
                yes.append(i)
    
    print(len(yes))
    return yes

test = [5,2,3,2,1,4]
# print(greater_second(test))

#5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_value(size, value):
    that_value = []
    for i in range(0, size):
        that_value.append(value)

    return that_value

# print(length_value(6,2))