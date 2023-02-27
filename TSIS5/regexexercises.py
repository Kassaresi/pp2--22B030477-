import re
#(Task 1) Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
with open('regex_example.txt' , "r") as file:
        f = file.read()
pattern1 = ("ab{0,}")
# x = re.findall(pattern1,f)
# print (x)

# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
pattern2 = ("ab{2,3}")
# x = re.findall(pattern2,f)
# print(x)

# Write a Python program to find sequences of lowercase letters joined with a underscore.
pattern3 = ("[a-z]{1,}_[a-z]{1,}")
# f = "abc_abc f"
# x = re.findall(pattern3,f)
# print(x)

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
pattern4 = ("[A-Z][a-z]{0,}")
# f = "Abc jf ew Er"
# x = re.findall(pattern4,f)
# print(x)

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
pattern5 = 'a.*b'
# f = "sbf andfjskb"
# x = re.findall(pattern5,f)
# print(x)

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
pattern6 = ("['\s,.']")
# x = re.sub(pattern6 , ':' , f)
# print (x)

# Write a python program to convert snake case string to camel case string.
def pattern7(s:str):
    f = re.findall('_[a-z]', s)
    for i in f:
        temp = s.index(i)
        temp2 = s[temp+1]
        s = re.sub('_[a-z]', '{}'.format(temp2.capitalize()),s)
    return s
# x = "-dmslkf _njfndskj"
# print (pattern7(f))

# Write a Python program to split a string at uppercase letters.
def pattern8(s:str):
    x = re.findall('[A-Z]', s)
    list = []
    for i in x:
        temp = s.index(i)
        if(temp == 0):
            continue
        temp2 = s[temp]
        s = s.replace(i, f'{temp2}')     
    return re.split(' ', s)
# print (pattern8(f))

# Write a Python program to insert spaces between words starting with capital letters.
def pattern9(s:str):
    x = re.findall('[A-Z]', s)
    for i in x:
        temp = s.index(i)
        if(temp == 0):
            continue
        temp2 = s[temp]
        s = s.replace(i, f' {temp2}')     
    return s
# print(pattern9(f))

# Write a Python program to convert a given camel case string to snake case.
def pattern10(s:str):
    f = re.findall('[A-Z]', s)
    for i in f:
        temp = s.index(i)
        temp2 = s[temp]
        s = s.replace(i, f'_{temp2.lower()}')
    return s
# print(pattern10(f))