from kangaroo.notation_parser.parsers.pgn_parser import PgnParser


class NotationParser:
    def __init__(self, parser):
        self.parser = parser

    def parse_moves(self, pgn_notation):
        return self.parser.notation_to_moves(pgn_notation)


if __name__ == "__main__":
    with open("parsers/tests/single_game.txt") as file_stream:
        pgn = file_stream.readline().replace("\n", "")

    moves_to_perform = pgn
    moves = NotationParser(PgnParser).parse_moves(moves_to_perform)
