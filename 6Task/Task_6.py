def printEvenIndex(inputList):
    def indexPrint(inputIndex):
        if inputIndex > len(inputList) - 1:
            return
        print(inputList[inputIndex])
        inputIndex += 2
        indexPrint(inputIndex)
    indexPrint(0)