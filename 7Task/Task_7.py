def secondMaximum(inputList):
    def maximumSearch(index, secondMax, firstMax):
        if index == len(inputList):
            return secondMax
        if inputList[index] >= firstMax:
            secondMax, firstMax = firstMax, inputList[index]
        elif inputList[index] >= secondMax:
            secondMax = inputList[index]
        index += 1
        return maximumSearch(index, secondMax, firstMax)
    if len(inputList) == 0:
        return
    return maximumSearch(0, inputList[0], inputList[0])