class Move:
    check = False

    def __init__(self, white, game_round, move_sequence):
        self.white = white
        self.game_round = game_round
        self.move_sequence = move_sequence
        self.parse_move()

    def parse_move(self):
        move_sequence = self.move_sequence
        # if move_sequence.endswith("+"):
        #     self.check = True
        #     move_sequence = move_sequence[:-1]
        print(move_sequence)


class KingsideCastling:
    def __init__(self, white, game_round):
        self.white = white
        self.game_round = game_round


class QueensideCastling(KingsideCastling):
    pass


special_moves = {
    "O-O": KingsideCastling,
    "0-0": KingsideCastling,
    "O-O-O": QueensideCastling,
    "0-0-0": QueensideCastling,
}
