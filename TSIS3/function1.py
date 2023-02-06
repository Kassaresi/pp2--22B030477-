#A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def ouches(gramm):
    return 28.3495231 * gramm

# gramm = int(input())
# print (ouches(gramm))

# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def c(f):
    return (5/9) * (f-32)
# f = int(input())
# print(c(f))

# Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def chicken_rabbit(nheads,nlegs):
    # 2*chicken + 4*rabbit = nlegs
    # chicken + rabbit = nheads
    rabbit = nlegs/2 - nheads
    chicken = nheads - rabbit
    return chicken,rabbit
# nheads = int(input())
# nlegs = int(input())
# print(chicken_rabbit(nheads,nlegs))

# You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def prime(lists):
    for number in lists:
        check = True
        for i in range(2,int(number/2)):
            if number % i == 0:
                check = False
        if check and number != 4 and number != 1:
            prime_numbers.append(number)
    return prime_numbers

# prime_numbers=[]
# n = int(input())
# lists = list(map(float,input().strip().split()))[:n]
# print(prime(lists))
                
# Write a function that accepts string from user and print all permutations of that string.
def permitation(strings):
    new_lists = []
    lists = list(strings)
    lists.sort()
    sets = set(lists)
    c = 1
    i = 1
    while i <= len(lists):
        c = c * i
        i += 1
    j = 1
    r = 1
    while j <= (len(lists) - len(sets))+1:
        r = r * j
        j += 1
    return c/r
# strings = str(input())
# print(permitation(strings))

# Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def reverses(string):
    new_string = " h"
    lists = list(string)
    lists.reverse()
    for i in lists:
        new_string.format(i)
    return new_string
# lists = []
# string = str(input())
# print(reverses(string))

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def dublicates(lists):
    a = 0
    for i in range(len(lists) -1):
        if lists[i] == lists[i+1] and lists[i] == 3:
            a += 1
    tf = ""
    if a >= 1:
        tf = "True"
    else:
        tf = "False"
        
# number = int(input())
# lists = list(map(int,input().strip().split()))
# print(dublicates)

# Write a function that takes in a list of integers and returns True if it contains 007 in order
def agent(lists):
    zero = 0
    seven = 0
    booler = True
    for i in range(len(lists)):
        if seven != 1 and zero < 3:
            if lists[i] == 0:
                zero += 1
            elif lists [i] == 7:
                seven += 1
        elif (seven == 1 and zero == 2):
            break
        else:
            booler = False
            break
    return booler
# n = int(input())
# lists = list(map(int,input().strip().split())) [:n]
# print(agent(lists))

def spy_game(list):
    che = True
    for i in range(len(list)):
        if list[i] == 7:
            che = True
        elif list[i] == 0:
            che = False
    return che

# n = int(input())
# list = list(map(int,input().strip().split()))[:n]
# print(spy_game(list))

# Write a function that computes the volume of a sphere given its radius.
def volume(radius):
    p = 3.14
    vol = float(4/3 * p *radius*radius*radius)
    return vol
# radius = int(input())
# print(volume(radius)) 

# Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def unique(list):
    i = 0
    while i < len(list):
        j = 0
        while j < len(list):
            if list[i] == list[j] and i!=j:
                list.pop(j)
            j += 1
        i += 1
    return list
# n = int(input())
# list = list(map(str,input().strip().split()))[:n]
# print (unique(list))

# Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def polindrome(string):
    left = string[0:int(len(string) / 2)]
    right = string[int(len(string)/2 + 1):len(string)]
    if left[len(left)::-1] == right:
        return True
    else:
        return False
# string = str(input())
# print(polindrome(string))
def histogram(list):
    histo = ""
    for i in range(len(list)):
        if i == 0:
            histo += "*"*list[i]
        else:
            histo += "\n" + "*"*list[i]
    return histo
# n = int(input())
# list = list(map(int,input().strip().split()))[:n]
# print (histogram(list))

# Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
import random

random_number = random.randrange(1,20)
number_of_guesses = 0

name = (input("Hello! What is your name?" + "\n"))
print ("\n")
print("Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess")
while True:
    number_of_guesses += 1
    number_of_player = int(input())
    print("\n")
    if number_of_player == random_number:
        print("Good job, {name}! You guessed my number in {number_of_guesses} guesses!")
        break
    elif number_of_player < random_number:
        print ("Your guess is too low. \nTake a guess")
        continue
    else:
        print ("Your guess is too high. \nTake a guess")
        continue