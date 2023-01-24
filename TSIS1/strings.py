# "Str" and 'Str' are same
print("Hello")
print('Hello')

a = "Hello"
print(a)

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#or use three '
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are array
a = "Hello"
print (a[0])

#Looping Through a String
for x in ("Banana"):
    print (x)

#String length
x = "big boy"
print(len(x))

#Check string
txt = "The best things in life are free!"
print("free" in txt)

#check if not
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

print ("\n")

#slicing
b = "Hello, World!"
print(b[2:5])

#Slice From the Start
b = "Hello, World!"
print(b[:5])

#Slice to the end
b = "Hello, World!"
print(b[2:])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

print ("\n")

#Upper case
a = "Hello, World!"
print(a.upper())

#lower case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace "return 0"
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String (switch)
a = "Hello, World!"
print(a.replace("H","J"))

#Split String (divided)
a = "Hello, World!"
print (a.split(","))

print ("\n")

#String Concatenation
a = "Hello"
b = "World!"
c = a + b
print (c) #HelloWorld!
c = a + " " + b
print (c) #Hello World!

#Format string
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Exercises
print("\n" + "Exercises")

x = "Hello, World!"
print(len(x))

txt = "Hello, World!"
x = txt[0]
print (x)

txt = "Hello, World!"
x = txt[2:5]
print (x)

txt = "Hello, World!"
x = txt.strip()
print (x)

txt = "Hello, World!"
txt = txt.upper()
print (txt)

txt = "Hello, World!"
txt = txt.lower()
print (txt)

txt = "Hello, World!"
txt = txt.replace("H","J")
print (txt)

age = 36
txt = "My name is John, and I am {} "
print(txt.format(age))