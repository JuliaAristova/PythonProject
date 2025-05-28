# Python reading files (.txt, .json, .csv
import json
import csv

# Reading .txt file
file_path_txt = "output.txt"

try:
    with open(file_path_txt, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("This file is not found")
except PermissionError:
    print("You do not have permission to read this file")

# Reading .json file
file_path_json = "C:/Users/julia/OneDrive/Desktop/output.json"
try:
    with open(file_path_json, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"], content["age"], content["position"])
except FileNotFoundError:
    print("This file is not found")
except PermissionError:
    print("You do not have permission to read this file")


# Reading .csv
file_path_csv = "C:/Users/julia/OneDrive/Desktop/emp.csv"

try:
    with open(file_path_csv, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            print("name:", line[0], "| age:", line[1], "| position: ", line[2])

except FileNotFoundError:
    print("This file is not found")
except PermissionError:
    print("You do not have permission to read this file")