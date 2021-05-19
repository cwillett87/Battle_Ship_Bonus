from piece import Piece


class Pieces:

    def __init__(self):
        self.pieces = []
        self.make_pieces()

    def make_pieces(self):
        destroyer = Piece('Destroyer', ['D', 'D'])
        self.pieces.append(destroyer)
        submarine = Piece('Submarine', ['S', 'S', 'S'])
        self.pieces.append(submarine)
        battleship = Piece('Battleship', ['B', 'B', 'B', 'B'])
        self.pieces.append(battleship)
        carrier = Piece('Carrier', ['C', 'C', 'C', 'C', 'C'])
        self.pieces.append(carrier)