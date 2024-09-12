import os
 

file_path = 'C:/Users/test.txt'  # file path
 
# using basename function from os 
# module to print file name

file_name = os.path.basename(file_path)
 

print(file_name)