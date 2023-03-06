import os
import re
file = open("/Users/kassi/TSIS6/example_lec6.txt" , "r")
f = file.read()
# Write a Python program with builtin function to multiply all the numbers in a list
def multiplication(f):
    pattern = ("\d")
    x = re.findall(pattern,f)
    if x ==[]:
        m = 0
    else:
        m = 1
        for i in x:
            n = int(i)
            m = m * n
    return m   
# print(multiplication(f))

def small_letters(f):
    pattern1 = ("[a-z]")
    small = re.findall(pattern1,f)
    s = len(small)
    return s
def big_letters(f):
    pattern2 = ("[A-Z]")
    big = re.findall(pattern2,f)
    b = len(big)
    return b
# print("Number of lowercase letters: " , small_letters(f))
# print("Number of uppercase letters: " , big_letters(f))

# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
file = open("example_lec6_polindrome.txt","r")
f = file.read()
def polindrome(f):
    pattern = ("[A-Za-z]")
    polin = re.findall(pattern,f)
    for i in range(0, int(len(polin)/2)):
        if polin[i] != polin[len(polin)-i-1]:
            return False
    return True
# print(polindrome(f))

# Write a Python program that invoke square root function after specific milliseconds.
import time
import math
# start = time.time()
# print((time.time() - start )*1000)
start = time.time()
def square(number):
    return math.sqrt(number)
def time_of_operation(start):
    t = (time.time() - start) * 1000
    return t
# number = int(input())
# print ("Square root of " ,number," after ", time_of_operation(start), " miliseconds is ", square(number))

# Write a Python program with builtin function that returns True if all elements of the tuple are true.
file = open("/Users/kassi/TSIS6/example_lec6_tuple.txt","r")
f = file.read()
def tuple(f):
    if f == "True" or "1" == f :
        return True
    return False
# print (tuple(f))

    