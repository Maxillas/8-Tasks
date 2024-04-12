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
    elif len(inputList) == 1:
        return inputList[0]
    if inputList[0] > inputList[1]:
        firstMax = inputList[0]
        secondMax = inputList[1]
    else:
        firstMax = inputList[1]
        secondMax = inputList[0]

    return maximumSearch(0, secondMax, firstMax)