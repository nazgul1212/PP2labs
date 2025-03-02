import os
from string import ascii_uppercase
'''
#task 1
location1 = r'/Users/nazekkhurshitova/Desktop/pp2labs/lab6'
print([name for name in os.listdir(location1)]) #everything
print([name for name in os.listdir(location1) if os.path.isdir(os.path.join(location1, name))]) #only directories
print([name for name in os.listdir(location1) if not os.path.isdir(os.path.join(location1, name))]) #only files
'''

'''
#task 2
print('Path exists:', os.access(r'/Users/nazekkhurshitova/Desktop/pp2labs/lab6', os.F_OK))
print('Path readable:', os.access(r'/Users/nazekkhurshitova/Desktop/pp2labs/lab6', os.R_OK))
print('Path writable:', os.access(r'/Users/nazekkhurshitova/Desktop/pp2labs/lab6', os.W_OK))
print('Path executable:', os.access(r'/Users/nazekkhurshitova/Desktop/pp2labs/lab6', os.X_OK))
'''
#task 3
'''
path = input('Insert path \n')
path_bool = os.access(path, os.F_OK)
if path_bool == False:
    print("Path does not exist")
elif path_bool == True:
    print("Directories:", ', '.join([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]))
    print("Files:", ', '.join([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]))
   
'''
#task 4 
'''
with open(r'/Users/nazekkhurshitova/Desktop/pp2labs/lab6/file.txt', 'r') as file:
    x = len(file.readlines())
    print("Number of lines:", x)
'''


#task 5
'''
mylist = ['A', 'B', 'C', 'D']
with open(r'/Users/nazekkhurshitova/Desktop/pp2labs/lab6/file2.txt', 'w') as file:
    for i in mylist:
        file.write(i + '\n')
file.close()
'''


#task 6
'''
import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is the file {letter}.txt")

generate_text_files()
'''

#task 7
'''
with open('file.txt', 'r') as file1, open('filee.txt', 'a') as file2:
    for line in file1:
        file2.write(line)
'''
#task 8
'''
path = r'/Users/nazekkhurshitova/Desktop/pp2labs/lab6/file.txt'
path_bool = os.access(path, os.F_OK)
if path_bool == False:
    print('Path does not exist')
elif path_bool == True:
    os.remove(path)
    print("File has been removed")
'''