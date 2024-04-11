import os


def find(path):
    outputList = []
    list = os.listdir(path)
    os.chdir(path)

    def file_find(inputList, inputIndex):
        list = inputList
        index = inputIndex
        if index > len(inputList) - 1:
            os.chdir("..")
            return
        newPath = "./" + list[index]
        if os.path.isdir(newPath):
            newList = os.listdir(newPath)
            os.chdir(newPath)
            file_find(newList, 0)
            index += 1
        else:
            outputList.append(list[index])
            index += 1
        file_find(list, index)
        return

    file_find(list, 0)
    return outputList

