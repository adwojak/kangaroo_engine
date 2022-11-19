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
print(Pieces["a"])
