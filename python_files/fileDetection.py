'''
Python file detection
'''

import os

file_path = 'testFile'

#'C:/Users/julia/PycharmProjects/PythonProject/test' OR
# 'C:\\Users\\julia\\PycharmProjects\\PythonProject\\test'

if os.path.exists(file_path):
    print(f"The location'{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("The location does not exist")
