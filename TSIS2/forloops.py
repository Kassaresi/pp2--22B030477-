#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
# #apple
# banana
# cherry
print("\n")

#Looping Through a String
for x in "banana":
  print(x)

print ("\n")
  
#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
# apple
# banana
print("\n")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #apple

# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) #['apple','cherry']

# The range() Function
for x in range(6):
  print(x) #0,1,2,3,4,5
print("\n")
  
for x in range(2, 6):
  print(x) #2,3,4,5
print("\n")
  
for x in range(2, 30, 3):
  print(x) #2,5,8,11,14,17,20,23,26,29
print("\n")

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
print("\n")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") #If the loop breaks, the else block is not executed.
  
#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass #nothing

print("\n")

#Exercises
fruits = ["apple", "banana", "cherry"]
for x in fruits:  
    print(x)

print ("\n")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
print("\n")

for x in range(6) :
  print(x)
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)