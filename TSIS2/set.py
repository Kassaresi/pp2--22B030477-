#Sets
thisset = {"apple", "banana", "cherry"}
print(thisset) #{'apple', 'banana', 'cherry'}
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #{'banana', 'cherry', 'apple'}

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1) #{'apple', 'banana', 'cherry'}
print(set2) #{1, 3, 5, 7, 9}
print(set3) #{False, True}

set1 = {"abc", 34, True, 40, "male"}
print(set1) #{'abc', True, 34, 40, 'male'}

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset) #{'banana', 'cherry', 'apple'}
# Note: the set list is unordered, so the result will display the items in a random order.

print("\n")

# Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
# banana
# apple
# cherry

# Bool
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) #True

print("\n")

# Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #{'cherry', 'papaya', 'banana', 'apple', 'mango', 'pineapple'}

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #{'orange', 'cherry', 'kiwi', 'apple', 'banana'}

print("\n")

# Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) #{'apple', 'cherry'}

#Discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #{'cherry', 'apple'}

#Pop
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #cherry
print(thisset)#{'apple', 'banana'}

#Clear
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #set()

#Del
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset) #this will raise an error because the set no longer exists

print("\n")

# Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
# cherry
# apple
# banana

print("\n")

# Join Two Sets (union)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) #{1, 2, 3, 'a', 'b', 'c'}

#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)#{1, 2, 3, 'a', 'b', 'c'}

# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) #{'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) #{'apple'}

#Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) #{'banana', 'microsoft', 'google', 'cherry'}

#Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# add() - Adds an element to the set
# clear() - Removes all the elements from the set
# copy() - Returns a copy of the set
# difference() -	Returns a set containing the difference between two or more sets
# difference_update() - Removes the items in this set that are also included in another, specified set
# discard() - Remove the specified item
# intersection() - Returns a set, that is the intersection of two other sets
# intersection_update() - Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() - Returns whether two sets have a intersection or not
# issubset() - Returns whether another set contains this set or not
# issuperset() - Returns whether this set contains another set or not
# pop() - Removes an element from the set
# remove() - Removes the specified element
# symmetric_difference() - Returns a set with the symmetric differences of two sets
# symmetric_difference_update() - inserts the symmetric differences from this set and another
# union() - Return a set containing the union of sets
# update() - Update the set with the union of this set and others

print("\n")

#Exercises
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!") #"Yes, apple is a fruit!"

fruits = {"apple", "banana", "cherry"}
fruits.add("orange") #{'apple', 'banana', 'orange', 'cherry'}
print(fruits) 

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits) #{'grapes', 'mango', 'orange', 'apple', 'cherry', 'banana'}

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) #{'apple', 'cherry'}

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)#{'apple', 'cherry'}
