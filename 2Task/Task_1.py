def sumOfDigit(number):
    if number < 0:
        number *= -1
    digit = number % 10
    result = digit
    if digit == number:
        return result
    result += sumOfDigit((number - digit) / 10)
    return int(result)