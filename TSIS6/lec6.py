# file handing
f = open("lec6_example.txt" , "w")
txt = input()
f.write(txt)
f.close

f = open("lec6_example.txt" , "r")
print (f.read())