from typing import List, Tuple

class Square:
    def __init__(self, start: Tuple, end: Tuple):
        self.start = start
        self.end = end

    def have_inside(self, coordinate: Tuple) -> bool:
        """
        Check if coordinate is inside the Square
        """
        x, y = coordinate
        start_x, start_y = self.start
        end_x, end_y = self.end
        return start_x <= x <= end_x and start_y <= y <= end_y

    def upgrade_end_coordinate(self, end_coordinate:Tuple)->None:
        x_end, y_end = self.end
        x_coordinate, y_coordinate = end_coordinate

        # Do not need to upgrade border squares
        if x_coordinate==x_end or y_coordinate==y_end:
            return

        x_difference = x_coordinate-x_end
        y_difference = y_coordinate-y_end

        # Take the smaller difference
        if x_difference < y_difference:
            increase_value = x_difference
        else:
            increase_value = y_difference
        self.end = (x_end+increase_value, y_end+increase_value)

    def upgrade_square(self):
        """
        Upgrade the square by increasing the end coordinate
        e.g.:
        start = (0,0), end = (1,1) to -> start = (0,0), end = (2,2)
        """
        x, y = self.end
        x += 1
        y += 1
        self.end = (x, y)


    def downgrade_square(self):
        """
        Upgrade the square by increasing the end coordinate
        e.g.:
        start = (0,0), end = (1,1) to -> start = (0,0), end = (2,2)
        """
        x, y = self.end
        x += -1
        y += -1
        self.end = (x, y)

    def square_size(self)-> int:
        return self.end[0] - self.start[0] + 1

def is_good_value(value: int) -> bool:
    return True if value==1 else 0

def get_value(matrix: List[List], coordinates: Tuple):
    return matrix[coordinates[0]][coordinates[1]]

def valid_right_and_botton_square_border(matrix:  List[List], square: Square) -> bool:
    """
    This method check the right and bottom values of a square
    e.g. for a 3x3 square it will check the following position (?)
    1, 1, ?
    1, 1, ?
    ?, ?, ?
    """
    x_end, y_end = square.end
    x_start, y_start = square.start
    valid_borders = True
    square_size = square.square_size()
    x_matrix_weid = len(matrix)

    if x_end >= x_matrix_weid or y_end >= x_matrix_weid:
        return False
    

    # check border values
    for i in range(square_size):
        right_coordinates = (x_end, y_start+i)
        bottom_coordinates = (x_start+i, y_end)
        right_value = get_value(matrix, right_coordinates)
        bottom_value = get_value(matrix, bottom_coordinates)

        if not is_good_value(right_value) or not is_good_value(bottom_value):
            return False
        
    return valid_borders

def get_good_square(matrix, square: Square) -> Square:
    
    square.upgrade_square()
    if valid_right_and_botton_square_border(matrix, square):
        square = get_good_square(matrix, square)
    else:
        square.downgrade_square()
    
    return square

def count_good_squares(matrix: List[List]) -> int:
    total=0
    last_square = None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            coordinates = (j,i)
            square = Square(coordinates, coordinates)
            
            # Validate it is a good 1x1 square
            value = get_value(matrix, coordinates)
            if not is_good_value(value):
                continue
            
            # Re-use the last good square
            if last_square and last_square.have_inside(coordinates):
                square.upgrade_end_coordinate(last_square.end)
            else:
                last_square=square
            
            # Calculate square dimentions
            square = get_good_square(matrix, square)
            count_of_good_squat = square.square_size()
            total = total + count_of_good_squat
    return total
