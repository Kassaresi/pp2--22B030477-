import os
#function to creat file
def creatfile(fname):
    f = open(fname,"w")
def readfile(fname):
    f = open(fname,"r")
    file = f.read()
    print (file)
def updatefile(fname,txt):
    f = open(fname,"r")
    print(f.read())
    f.close()
    
    f = open(fname,"a")
    f.write(txt)
    f.close()
    
    f = open(fname,"r")
    print (f.read())
def overwrite(fname,txt):
    f = open(fname,"a")
    f.write(txt)
def deletefile(fname):
    os.remove(fname)
# fname = input() + '.txt'
# option = int(input())

# if option == 1:
#     creatfile(fname)
# elif option == 2:
#     readfile(fname)
# elif option == 3:
#     txt = input()
#     updatefile(fname,txt)
# elif option == 4:
#     overwrite(fname)
# elif option == 5:
#     deletefile(fname)
# else:
#     print ("Option can be only 1-5")
    
#task 13
pathname = input()
path = os.path.abspath(pathname)
print (path)