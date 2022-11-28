import re
from notation_parser.notation_parser import PGN_MOVE_REGEX

"""
= Pawn promotion
0-0 O-O Kingside castling
0-0-0 O-O-O Queenside castling
"(=)" Draw offer
x Capture
+ Check
# Checkmate
"""


def read_sample():
    with open("100games.txt") as file_stream:
        return [line.replace("\n", "") for line in file_stream.readlines()]


for line in read_sample():
    parsed_line = " ".join([f"{element[0]}{element[1]}.{element[2]}" for element in re.findall(PGN_MOVE_REGEX, line)])
    assert line == parsed_line
