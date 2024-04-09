def palindromeChecker(inputString):
    str = inputString
    def foo(Inputindex):
        if Inputindex > len(str) / 2 - 1:
            return True
        if inputString[Inputindex] != inputString[-Inputindex - 1]:
            return False
        Inputindex += 1
        return foo(Inputindex)
    return foo(0)
