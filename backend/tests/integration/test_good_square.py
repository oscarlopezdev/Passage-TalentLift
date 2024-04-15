import unittest
from backend.good_square_counter import count_good_squares

matrix_3 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]

matrix_3_b = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

matrix_3_c = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 0],
]

matrix_empty = []

matrix_2_b = [
    [1, 1],
    [1, 0],
]

matrix_4 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

matrix_4_4_A =     [[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 0],
                    [1, 1, 1, 1]]

matrix_5_5 =   [[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]]

matrix_5_5_B =     [[1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1]]


class TestCountGoodSquares(unittest.TestCase):

    def test_empty_matrix(self):
        result = count_good_squares(matrix_empty)
        self.assertEqual(result, 0)

    def test_matrix_5_5(self):
        result = count_good_squares(matrix_5_5)
        self.assertEqual(result, 39)

    def test_matrix_5_5_B(self):
        result = count_good_squares(matrix_5_5_B)
        self.assertEqual(result, 36)

    def test_matrix_4_4_A(self):
        result = count_good_squares(matrix_4_4_A)
        self.assertEqual(result, 24)

    def test_matrix_x3(self):
        result = count_good_squares(matrix_3)
        self.assertEqual(result, 14)

    def test_matrix_x2_b(self):
        result = count_good_squares(matrix_2_b)
        self.assertEqual(result, 3)

    def test_matrix_x3_b(self):
        result = count_good_squares(matrix_3_b)
        self.assertEqual(result, 8)

    def test_matrix_x3_c(self):
        result = count_good_squares(matrix_3_c)
        self.assertEqual(result, 11)

    def test_matrix_x4_c(self):
        result = count_good_squares(matrix_4)
        self.assertEqual(result, 30)