from enum import Enum, EnumMeta
import re
from abc import ABC, abstractmethod


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
    def __init__(self, white, round, move_sequence):
        self.white = white
        self.round = round
        self.move_sequence = move_sequence


STANDARD_REGEX_SPLITTER = r"(W|B)(\d+).(\w+)"


class BaseParser(ABC):
    @staticmethod
    @abstractmethod
    def notation_to_moves(pgn_string):
        """Split single notation line into multiple elements representing each move"""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def parse_move(pgn_move):
        """Parse single move into multiple informations - color, round, move ets."""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_move_object(move_parameters):
        """Create Move object from given parameters"""
        raise NotImplementedError


class StandardParser(BaseParser):
    """
    Parser for below notation:
    W1.d4 B1.d5 W2.c4 B2.e6 W3.Nc3 B3.Nf6 W4.cxd5 B4.exd5 W5.Bg5 B5.Be7 W6.e3 B6.Ne4 W7.Bxe7 B7.Nxc3 W8.Bxd8 B8.Nxd1
    """

    @staticmethod
    def notation_to_moves(pgn_string):
        moves = []
        for element in pgn_string.split(" "):
            move_parameters = StandardParser.parse_move(element)
            moves.append(StandardParser.create_move_object(move_parameters))
        return moves

    @staticmethod
    def parse_move(pgn_move):
        return re.match(STANDARD_REGEX_SPLITTER, pgn_move).groups()

    @staticmethod
    def create_move_object(move_parameters):
        color, round_value, move_sequence = move_parameters
        return Move(color == "W", round_value, move_sequence)


class NotationParser:
    def __init__(self, parser):
        self.parser = parser

    def parse_moves(self, pgn_notation):
        moves = self.parser.notation_to_moves(pgn_notation)
        print(moves)


with open("tests/sample2.txt") as file_stream:
    pgn = file_stream.readline().replace("\n", "")
NotationParser(StandardParser).parse_moves(pgn)
print(0)
