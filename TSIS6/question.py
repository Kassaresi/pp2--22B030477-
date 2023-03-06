import re
import os
import time
file = open("/Users/kassi/TSIS6/exercisesTSIS6.py" , "r")
f = file.read()
def square(f):
    pattern = ("/d")
    x = re.findall(pattern,f)
    str = ''
    for i in x:
        ''.join(x)
    number = int(str)
    return pow(number,0.5)
def time_of_operation():
    start = time.time()
    t = time.time() - start
    return t
pattern = "/d"
y = re.findall(pattern,f)
print ("Square root of " ,y," after ", time_of_operation(), " miliseconds is ", square(f))
