SIZE = 8


class Pawn:
    is_white = False

    vertical_position = 1
    horizontal_position = 3

    # def moving_algorithm(self):
    #     if self.is_white:
    #         pass
    #     else:
    #         self.vertical_position += 1

    def get_standard_moves(self):
        possible_moves = []
        for vertical_move in range(self.vertical_position + 1, SIZE - self.vertical_position + 1):
            possible_moves.append((vertical_move, self.horizontal_position))
        return possible_moves

    def get_attack_moves(self):
        return [(self.vertical_position + 1, self.horizontal_position - 1), (self.vertical_position + 1, self.horizontal_position + 1)]

    def calculate_moves(self):
        moves = self.get_standard_moves()
        moves.extend(self.get_attack_moves())
        return moves


class BoardSide:
    def __init__(self, is_white=True):
        self.is_white = is_white


class Board:
    white_moves = True
    sides = (BoardSide(), BoardSide(False))

    def execute_move(self):
        tmp_move = ""

#
# board = Board()
#
#
# pawn = Pawn()
# printer(pawn)
