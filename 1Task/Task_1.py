class RaisingToExp:
    def raising(self, inputNumber, inputExp):
        number = inputNumber
        exp = inputExp
        if exp == 1:
            return number
        if exp == 0:
            return 1
        if exp < 0:
            return 1 / (number * self.raising(number, -exp - 1))
        return number * self.raising(number, exp - 1)