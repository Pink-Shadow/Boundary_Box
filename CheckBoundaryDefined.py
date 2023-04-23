import json
import os

files = os.listdir(os.getcwd() + "/assets")
files = [file for file in files if file.endswith(".jpg")]

for i in range(1, 267):
    if str(i) + ".jpg" not in files:
        print(str(i) + ".jpg is not defined in assets folder")

with open("coordinates.json", 'r+') as inputFile:
    inputData = json.loads(inputFile.read())
    for file in files:
        if file not in inputData.keys():
            print( file + " is not defined in coordinates.json")
