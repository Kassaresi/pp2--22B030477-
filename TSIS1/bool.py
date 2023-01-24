#Booleans 1 = True and 0 = False

#True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Functions can Return a Boolean
def myFunction() :
  return True
print(myFunction())

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
  
x = 200
print(isinstance(x, int))

#Exercises
print ("\n" + "Exercises:")

print (10 > 9)
#True

print (10 == 9)
#False

print (10 < 9)
#False

print(bool("abc"))
#True

print(bool(0))
#False