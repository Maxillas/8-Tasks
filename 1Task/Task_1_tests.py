import unittest
from Task_1 import RaisingToExp


class TestTask1(unittest.TestCase):
    def testRaising(self):
        solverObject = RaisingToExp()
        self.assertEqual(solverObject.raising(2, 1), 2)
        self.assertEqual(solverObject.raising(2, 2), 4)
        self.assertEqual(solverObject.raising(2, 3), 8)
        self.assertEqual(solverObject.raising(2, 0), 1)
        self.assertEqual(solverObject.raising(2, -1), 0.5)
        self.assertEqual(solverObject.raising(2, -2), 0.25)
        self.assertEqual(solverObject.raising(2, -3), 0.125)