def palindromeChecker(inputString):
    str = inputString.lower().replace(' ', '')
    if (len(str) <= 1) or (len(str) == 2 and str[0] == str[-1]):
        return True   
    return (str[0] == str[-1]) and palindromeChecker(str[1:-1])
