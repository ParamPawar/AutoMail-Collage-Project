import os
 

file_path = 'C:/Users/test.txt'
 

file_name = os.path.basename(file_path)

file = os.path.splitext(file_name)
 

print(file)  # returns tuple of string
 

print(file[0] + file[1])