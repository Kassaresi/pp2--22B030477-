# Tuple - A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple) #('apple', 'banana', 'cherry')

# Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #('apple', 'banana', 'cherry', 'apple', 'cherry')
#length of tuples
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple)) #3

#Tuple
thistuple = ("apple",)
print(type(thistuple)) #<class 'tuple'>
#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #<class 'str'>

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1) #('apple', 'banana', 'cherry')
print(tuple2) #(1, 5, 7, 9, 3)
print(tuple3) #(True, False, False)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1) #'abc', 34, True, 40, 'male')

# type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # <class 'tuple'>

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #('apple', 'banana', 'cherry')

# Python Collections (Arrays)
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

print("\n")
# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #banana

# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #cherry

# Range Indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #('cherry', 'orange', 'kiwi')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #('orange', 'kiwi', 'melon')

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") #Yes, 'apple' is in the fruits tuple
  
print("\n")

# Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #('apple', 'kiwi', 'cherry')

# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) 
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

#Add tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y 
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) #('banana', 'cherry')

print("\n")
# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# apple
# banana
# cherry

# Using Asterisk (*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# apple
# banana
# ['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
# apple
# ['mango', 'papaya', 'pineapple']
# cherry

print("\n")

# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# apple
# banana
# cherry

# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# apple
# banana
# cherry

# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
# apple
# banana
# cherry

print ("\n")

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) #('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

print ("\n")

#Exercises

fruits = ("apple", "banana", "cherry")
print(fruits[0]) #apple

fruits = ("apple", "banana", "cherry")
print(len(fruits)) #3

fruits = ("apple", "banana", "cherry")
print(fruits[-1]) #cherry

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5]) #('cherry', 'orange', 'kiwi')