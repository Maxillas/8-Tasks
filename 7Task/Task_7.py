import unittest

def secondMaximum(inputList):
    if len(inputList) == 1:
        return inputList[0]
    if len(inputList) == 0:
        return
    def maximumSearch(index, firstMax, secondMax):
        if index >= len(inputList):
            return secondMax
        if inputList[index] >= firstMax:
            secondMax, firstMax = firstMax, inputList[index]
        elif inputList[index] >= secondMax:
            secondMax = inputList[index]
        index += 1
        return maximumSearch(index, firstMax, secondMax)

    if (inputList[0] >= inputList[1]):
        return maximumSearch(2, inputList[0], inputList[1])
    elif (inputList[0] <= inputList[1]):
        return maximumSearch(2, inputList[1], inputList[0])