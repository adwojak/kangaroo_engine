from dev_helpers.board_printer import printer
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


pawn = Pawn()
printer(pawn)
