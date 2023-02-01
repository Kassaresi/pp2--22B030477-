#While loops
# while loops
# for loops

#While
i = 1
while i < 6:
  print(i)
  i += 1 #1,2,3,4,5
print("\n")
  
#The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 #1,2,3
print("\n")
  
# The continue Statement
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)
print("\n")  
  
# The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print("\n")

#Exersices
i = 1
while i < 6:
  print(i)
  i += 1 #1,2,3,4,5
print("\n")  
  
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 #1,2,3
print ("\n")
  
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)
print("\n")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")