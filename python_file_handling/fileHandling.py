'''
open(file_name, mode) - to work with files
Modes:
- "r"   read - open file for reading; default; error if file does not exist
- "a"   append - open file for appending; create a file if it does not exist
- "w"   write - open file for writing; create a file if it does not exist
- "x"   create - create the specified file; error if file exists
--------------
"test"     text; default; text mode
"b"     binary mode (ex., images)
'''

#same as - "rt" default, no need to specify
#f = open("demofile.txt", "rt")

f = open("C:\\Users\\julia\\PycharmProjects\\PythonProject\\basic\\20_File_Handling\\demofile.txt")
# print(f.read())           # read the whole file
print(f. read(10))          # read 10 characters

#If file is opened without using WITH statement - it must be closed
f.close()

# open using WITH statement
with open("C:\\Users\\julia\\PycharmProjects\\PythonProject\\basic\\20_File_Handling\\demofile2.txt") as f2:
    # print(f2.read())        # to read the whole file
    # print(f2.readline())            # reads one line (to read 2 - call twice

    # loop through the file line by line
    for line in f2:
        print(line)


