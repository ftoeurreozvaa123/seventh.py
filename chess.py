
from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.

        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací možné tahy pěšce.
        Bílý postupuje nahoru, černý dolů.
        """
        row, col = self.position

        direction = 1 if self.color == "white" else -1

        move = (row + direction, col)

        if self.is_position_on_board(move):
            return [move]

        return []

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]

        final_moves = []

        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné diagonální tahy střelce.
        """
        row, col = self.position
        moves = []

        directions = [
            (1, 1), (1, -1),
            (-1, 1), (-1, -1)
        ]

        for dr, dc in directions:
            for step in range(1, 8):
                move = (row + dr * step, col + dc * step)

                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné vodorovné a svislé tahy věže.
        """
        row, col = self.position
        moves = []

        directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]

        for dr, dc in directions:
            for step in range(1, 8):
                move = (row + dr * step, col + dc * step)

                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy.
        Dáma se pohybuje jako střelec i věž.
        """
        row, col = self.position
        moves = []

        directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1),
            (1, 1), (1, -1),
            (-1, 1), (-1, -1)
        ]

        for dr, dc in directions:
            for step in range(1, 8):
                move = (row + dr * step, col + dc * step)

                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále.
        Král se může posunout o jedno pole všemi směry.
        """
        row, col = self.position
        moves = []

        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue

                move = (row + dr, col + dc)

                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'
