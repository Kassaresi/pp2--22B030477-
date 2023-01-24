# We have 3 type of numbers. The`re "int", "float", "complex"

x = 1    # int
y = 2.8  # float
z = 1j   # complex 

#int
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
print ("\n")

#float
x = 1.10
y = 1.0
z = -35.59
#also float can be
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
print ("\n")

#Complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
print ("\n")

#Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
print("\n")

#Random number
import random
print(random.randrange(1, 10))

#Exercises
x = 5
x = float(x)
print (x)

x = 5.5
x = int(x)
print(x)

x = 5
x = complex(x)
print (x)

