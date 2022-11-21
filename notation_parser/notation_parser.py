from enum import Enum, EnumMeta


class King:
    # TMP
    pass


class Queen:
    # TMP
    pass


class Bishop:
    # TMP
    pass


class Knight:
    # TMP
    pass


class Rook:
    # TMP
    pass


class Pawn:
    # TMP
    pass


class DefaultEnumMeta(EnumMeta):
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError:
            return super().__getitem__("DEFAULT")


class Pieces(Enum, metaclass=DefaultEnumMeta):
    DEFAULT = Pawn
    K = King
    Q = Queen
    B = Bishop
    N = Knight
    R = Rook


class Move:
    def __init__(self, white, piece):
        self.white = white
        self.piece = piece


# aa = Pieces["a"]
# print(aa)
# print(Pieces["a"])
# aaa = {'B', 'O', 'a', 'Q', '#', 'N', 'd', 'h', '+', 'R', 'g', 'e', 'x', 'c', 'f', 'b', '-', '=', 'K'}


class NotationParser:
    # def __init__(self, pgn_string):
    #     self.pgn_string = pgn_string
    #     self.pgn_list = pgn_string.split(" ")
    #     print(self.pgn_list)

    @staticmethod
    def pgn_to_object(pgn_move):
        sequence, move = pgn_move.split(".")
        print(sequence)
        print(move)


with open("tests/sample2.txt") as file_stream:
    pgn = file_stream.readline().replace("\n", "")
# notation_parser = NotationParser(pgn)
pgn_list = pgn.split(" ")
print(pgn_list)
NotationParser.pgn_to_object(pgn_list[0])
