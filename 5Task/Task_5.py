def printEvenNumber(inputList):
    lst = inputList[:]
    if len(lst) == 0:
        return
    digit = lst.pop(0)
    if digit % 2 == 0:
        print(digit)
    printEvenNumber(lst)
