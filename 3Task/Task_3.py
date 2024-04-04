def listLen(inputList):
    list = inputList
    count = 0
    if not list:
        return 0
    list.pop(0)
    count += 1 + listLen(list)
    return count
