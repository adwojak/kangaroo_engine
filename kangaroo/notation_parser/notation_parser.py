from kangaroo.notation_parser.move_parsers.pgn_parser import PgnParser
from kangaroo.notation_parser.notation_splitters.pgn_splitter import PgnSplitter


class NotationParser:
    metadata = None
    moves = None

    def __init__(self, move_parser=None, metadata_parser=None, notation_splitter=None):
        self.move_parser = move_parser
        self.metadata_parser = metadata_parser
        self.notation_splitter = notation_splitter

    def identify_notation(self, notation):
        # TODO Find out which parser should be used
        if not all([self.move_parser, self.metadata_parser, self.notation_splitter]):
            # self.move_parser = ""
            # self.metadata_parser = ""
            # self.notation_splitter = ""
            pass

    def split_notation(self, notation):
        return self.notation_splitter.split_notation(notation)

    def parse_metadata(self, metadata):
        # self.metadata = self.metadata_parser.parse(metadata)
        pass

    def parse_moves(self, moves):
        pass
        # self.moves = self.move_parser.parse(moves)

    def parse_notation(self, notation):
        self.identify_notation(notation)
        pure_metadata, pure_moves = self.split_notation(notation)
        # self.parse_metadata(pure_metadata)
        # self.parse_moves(pure_moves)
        return 1


if __name__ == "__main__":
    with open("move_parsers/tests/single_game.txt") as file_stream:
        pgn = file_stream.read()

    moves = NotationParser(PgnParser, "qwe", PgnSplitter).parse_notation(pgn)
