import unittest

def secondMaximum(inputList):
    if len(inputList) == 1:
        return inputList[0]
    if len(inputList) == 0:
        return
    def maximumSearch(index, firstMax, secondMax):
        if index >= len(inputList):
            return secondMax
        if inputList[index] >= firstMax:
            secondMax, firstMax = firstMax, inputList[index]
        elif inputList[index] >= secondMax:
            secondMax = inputList[index]
        index += 1
        return maximumSearch(index, firstMax, secondMax)

    if (inputList[0] >= inputList[1]):
        return maximumSearch(2, inputList[0], inputList[1])
    elif (inputList[0] <= inputList[1]):
        return maximumSearch(2, inputList[1], inputList[0])



class Tests(unittest.TestCase):

    def test_1(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(secondMaximum(array), 6)

    def test_2(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 7, 7]
        self.assertEqual(secondMaximum(array), 7)

    def test_3(self):
        array = [6, 6, 7]
        self.assertEqual(secondMaximum(array), 6)

    def test_4(self):
        array = [5, 4, 3, 2, 5]
        self.assertEqual(secondMaximum(array), 5)

    def test_5(self):
        array = [-5, -4, -3, -2, -5]
        self.assertEqual(secondMaximum(array), -3)

    def test_6(self):
        array = [-5, -4]
        self.assertEqual(secondMaximum(array), -5)

    def test_7(self):
        array = [-5]
        self.assertEqual(secondMaximum(array), -5)

    def test_8(self):
        array = []
        self.assertEqual(secondMaximum(array), None)

    def test_9(self):
        array = [5, -4, 7, -2, -5]
        self.assertEqual(secondMaximum(array), 5)

    def test_10(self):
        array = [5, 6, 7, -2, -5]
        self.assertEqual(secondMaximum(array), 6)


if __name__ == '__main__':
    unittest.main()