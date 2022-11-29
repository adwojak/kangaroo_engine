from enum import Enum, EnumMeta
import re
from abc import ABC, abstractmethod
from moves.moves import special_moves, Move


PGN_MOVE_REGEX = r"(W|B)(\d+).([a-h1-8KQBNRxO\-\+\=\#]+)"


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
        return re.match(PGN_MOVE_REGEX, pgn_move).groups()

    @staticmethod
    def create_move_object(move_parameters):
        color, round_value, move_sequence = move_parameters
        if move_sequence in special_moves:
            return special_moves[move_sequence](color == "W", int(round_value))
        return Move(color == "W", int(round_value), move_sequence)


class NotationParser:
    def __init__(self, parser):
        self.parser = parser

    def parse_moves(self, pgn_notation):
        return self.parser.notation_to_moves(pgn_notation)


if __name__ == "__main__":
    with open("tests/single_game.txt") as file_stream:
        pgn = file_stream.readline().replace("\n", "")

moves_to_perform = pgn
moves = NotationParser(StandardParser).parse_moves(moves_to_perform)
