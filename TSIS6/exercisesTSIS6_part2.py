import os
x = input()
#1
# for i, j, z in os.walk(x):
#     for j in j:
#         print (os.path.join(i, j))
#     for z in z:
#         print (os.path.join(i, z))
#print .

#2
# print(os.access(x, os.F_OK))
# print(os.access(x, os.R_OK))
# print(os.access(x, os.W_OK))
# print(os.access(x, os.X_OK))

#3


#4
# sum = 0
# with open(x, 'r',encoding="utf-8") as file:
#     for i in file:  
#         sum += len(i)
# print(sum) #folder/folder2/file.txt

#5

#6
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 
    open("test/{}.txt".format(i), 'a')
    
#7
# catcopy = input() 
# with open(x, 'r') as file, open(catcopy, 'w') as fileforcopy:
#     for i in file:#         
#         fileforcopy.write(i)
        
#8
if os.path.exists(x):
    os.remove(x)
else:
    print("does not exist")
        
