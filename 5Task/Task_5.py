def printEvenNumber(inputList):
    def indexPrint(inputIndex):
        if inputIndex > len(inputList) - 1:
            return
        if inputList[inputIndex] % 2 == 0:
            print(inputList[inputIndex])
        inputIndex += 1
        indexPrint(inputIndex)
    indexPrint(0)