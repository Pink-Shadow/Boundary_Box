import sys, json

files = sys.argv[1:]

with open('../coordinates.json', 'r') as data_file:
    data = json.load(data_file)

for file in files:
    if file in data:
        del data[file]
        print("removed", file)

with open('../coordinates.json', 'w') as data_file:
    data = json.dump(data, data_file)
