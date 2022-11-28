special_moves = {
    "O-O": "Kingside castling",
    "0-0": "Kingside castling",
    "O-O-O": "Queenside castling",
    "0-0-0": "Queenside castling",
}


class Move:
    def __init__(self, white, game_round, move_sequence):
        self.white = white
        self.game_round = game_round
        self.move_sequence = move_sequence
        self.parse_move()

    def parse_move(self):
        piece = None
        if self.move_sequence in special_moves:
            print(special_moves[self.move_sequence])
        # for part in list(self.move_sequence):
        #     if not piece:
        #         if part.islower():
        #             piece = "P"
        #         elif part in ["K", "Q", "B", "N", "R"]:
        #             piece = part
        #         else:
        #             print("Special")
        # print(piece)


class KingsideCastling:
    def __init__(self, white, game_round):
        self.white = white
        self.game_round = game_round


class QueensideCastling(KingsideCastling):
    pass
