# Create a generator that generates the squares of numbers up to some number N.
def square(n):
    for i in range(n):
        yield i**2
# n = int(input())
# for i in square(n):
#     print (i)

# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even(number):
    for i in range(number):
        if i % 2 == 0:
            yield i
# number = int(input())
# list = []
# for j in even(number):
#     list.append(j)
# str = str(list)
# print (str)

# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def div_to_3_and_4(number):
    for i in range(number):
        if i % 3 == 0 and i % 4 == 0:
            yield i
# number = int(input())
# for i in div_to_3_and_4(number):
#     print (i)

# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def square_start_number1_to_number2_by_while(number1,number2):
    i = number1
    while i < number2:
        yield i**2
        i+=1
# number1 = int(input())
# number2 = int(input())
# for i in square_start_number1_to_number2_by_while(number1,number2):
#     print(i)

def square_start_number1_to_number2_by_for(number1,number2):
    for i in range(number1,number2):
        yield i**2
# number1 = int(input())
# number2 = int(input())
# for i in square_start_number1_to_number2_by_for(number1,number2):
    print(i)

# Implement a generator that returns all numbers from (n) down to 0.
def reverse(number):
    for i in range(number):
        yield i
number = int(input())
list = []
for i in reverse(number):
    list.append(i)
list.reverse()
for i  in list:
    print (i)