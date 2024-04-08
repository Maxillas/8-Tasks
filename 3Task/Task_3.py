def listLen(inputList):
    list = inputList
    if not list:
        return 0
    list.pop(0)
    return 1 + listLen(list)

