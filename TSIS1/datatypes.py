def f(x):
    print(type(x))
    print ("\n")
x = 5
f(x)
x = 4.5
f(x)
x = "FFF"
f(x)
x = 1j
f(x)
x = ["apple", "banana", "cherry"]
f(x)
x = ["apple", "banana", "cherry"]
f(x)
x = range(6)
f(x)
x = {"name" : "John", "age" : 36}
f(x)
x = {"apple", "banana", "cherry"}
f(x)
x = frozenset({"apple", "banana", "cherry"})
f(x)
x = True
f(x)
x = b"Hello"
f(x)
x = bytearray(5)
f(x)
x = memoryview(bytes(5))
f(x)
x = None
f(x)

#Also we can write person type
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

#Exercises

x = 5
print (type(x))
#int

x = "Hello, World!"
print(type(x))
#str

x = 20.5
print(type(x))
#float

x = ["apple", "banana", "cherry"]
print(type(x))
#list

x = ("apple", "banana", "cherry")
print(type(x))
#tuple

x = {"name" : "John", "age" : 36}
print(type(x))
#dict

x = True
print(type(x))
#bool