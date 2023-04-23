import json, os, skimage
counter = 0
outputFile = open("coordinates_renumbered.json", 'w+')
outputData = {}
with open("coordinates.json", 'r+') as inputFile:
    inputData = json.loads(inputFile.read())
    for picture in inputData:
        image = skimage.io.imread(f"assets/{picture}")
        skimage.io.imsave(f"assets_renumbered/{counter}.jpg", image)
        outputData[f"{counter}.jpg"] = inputData[picture]
        counter += 1
outputFile.write(json.dumps(outputData))
