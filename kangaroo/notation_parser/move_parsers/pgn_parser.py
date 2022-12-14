import re
from kangaroo.moves.moves import special_moves, Move
from kangaroo.notation_parser.move_parsers.base_parser import BaseParser

PGN_MOVE_REGEX = r"(W|B)(\d+).([a-h1-8KQBNRxO\-\+\=\#]+)"


class PgnParser(BaseParser):
    """
    Parser for below notation:
    W1.d4 B1.d5 W2.c4 B2.e6 W3.Nc3 B3.Nf6 W4.cxd5 B4.exd5 W5.Bg5 B5.Be7 W6.e3 B6.Ne4 W7.Bxe7 B7.Nxc3 W8.Bxd8 B8.Nxd1
    """

    @staticmethod
    def notation_to_moves(pgn_string):
        moves = []
        for element in pgn_string.split(" "):
            move_parameters = PgnParser.parse_move(element)
            moves.append(PgnParser.create_move_object(move_parameters))
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
