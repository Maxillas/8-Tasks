import unittest

def secondMaximum(inputList):
    def maximumSearch(index, firstMax, secondMax):
        if index == len(inputList):
            return secondMax
        if inputList[index] >= firstMax:
            secondMax, firstMax = firstMax, inputList[index]
        elif inputList[index] > secondMax:
            secondMax = inputList[index]
        index += 1
        return maximumSearch(index, firstMax, secondMax)
    return maximumSearch(0, inputList[0], inputList[0])