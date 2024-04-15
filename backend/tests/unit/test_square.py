import unittest

from backend.good_square_counter import Square

class TestSquare(unittest.TestCase):

    def test_upgrade_square(self):
        # Create an instance of the Square class
        square = Square((0, 0), (1, 1))

        # Call the upgrade_square method
        square.upgrade_square()

        # Verify if the start and end values are as expected after the upgrade
        self.assertEqual(square.start, (0, 0))
        self.assertEqual(square.end, (2, 2))

    def test_downgrade_square(self):
        # Create an instance of the Square class
        square = Square((0, 0), (2, 2))

        # Call the downgrade_square method
        square.downgrade_square()

        # Verify if the start and end values are as expected after the downgrade
        self.assertEqual(square.start, (0, 0))
        self.assertEqual(square.end, (1, 1))
