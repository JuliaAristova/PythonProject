'''
To write:
"a"     append to the end of the file
"w"     write - will ovewrite any existing content
'''

with open("C:\\Users\\julia\\PycharmProjects\\PythonProject\\basic\\20_File_Handling\\demofile.txt", "a") as f:
    f.write("Now the file has more content!")

# open and read after appending
with open("C:\\Users\\julia\\PycharmProjects\\PythonProject\\basic\\20_File_Handling\\demofile.txt") as f:
    print(f.read())

# overwrite existing content

with open("C:\\Users\\julia\\PycharmProjects\\PythonProject\\basic\\20_File_Handling\\demofile.txt", "w") as f:
    f.write("Woops!  I have deleted the content!")

with open("C:\\Users\\julia\\PycharmProjects\\PythonProject\\basic\\20_File_Handling\\demofile.txt") as f:
    print(f.read())

# This is a demofile to open and read it.