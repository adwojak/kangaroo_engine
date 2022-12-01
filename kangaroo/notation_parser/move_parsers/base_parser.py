from abc import ABC, abstractmethod


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
