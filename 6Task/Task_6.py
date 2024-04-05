def printEvenIndex(inputList):
    lst = inputList
    if len(lst) != 0:
        print(lst[0])
        printEvenIndex(lst[2:])
        return
    return