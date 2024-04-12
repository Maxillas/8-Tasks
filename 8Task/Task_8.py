import os


def find(path):
    outputList = []
    list = os.listdir(path)
    for item in list:
        newPath = path + '/' + item
        if os.path.isdir(newPath):
            outputList += find(newPath)
        else:
            outputList.append(item)
    return outputList
