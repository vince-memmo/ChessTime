from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def calc_moves(self, piece, row, col):
        def knight_moves():
            print(row, col, 'piece grabbed')
            possible_moves = [
                (row + 1, col + 2),
                (row - 1, col + 2),
                (row + 1, col - 2),
                (row - 1, col - 2),
                (row + 2, col + 1),
                (row - 2, col + 1),
                (row + 2, col - 1),
                (row - 2, col - 1)
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    # print(self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color))
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        print(possible_move_row, possible_move_col, 'moves possible')
                        move = Move(initial, final)
                        piece.add_move(move)

        def move_horizontally():
            horizontal_moves = []
            new_col = col + 1
            while new_col < 8:
                if not self.squares[row][new_col].has_piece():
                    horizontal_moves.append((row, new_col))
                    new_col += 1
                elif self.squares[row][new_col].has_enemy_piece(piece.color):
                    horizontal_moves.append((row, new_col))
                    break
                else:
                    break

            new_col = col - 1
            while new_col > -1:
                if not self.squares[row][new_col].has_piece():
                    horizontal_moves.append((row, new_col))
                    new_col -= 1
                elif self.squares[row][new_col].has_enemy_piece(piece.color):
                    horizontal_moves.append((row, new_col))
                    break
                else:
                    break

            return horizontal_moves

        def move_vertically():
            vertical_moves = []
            new_row = row + 1
            while new_row < 8:
                if self.squares[new_row][col].has_piece():
                    vertical_moves.append((new_row, col))
                    new_row += 1
                elif self.square.has_enemy_piece(piece.color):
                    vertical_moves.append((new_row, col))
                    break
                else:
                    break

            new_row = row - 1
            while new_row > -1:
                if self.squares[row][new_row].has_piece():
                    vertical_moves.append((new_row, col))
                    new_row -= 1
                elif self.square.has_enemy_piece(piece.color):
                    vertical_moves.append((new_row, col))
                    break
                else:
                    break

            return vertical_moves

        def move_diagonally():
            diagonal_moves = []
            new_row = row + 1
            new_col = col + 1
            while Square.in_range(new_row, new_col):
                if self.squares[new_row][new_col].has_piece():
                    diagonal_moves.append((new_row, new_col))
                    new_row += 1
                    new_col += 1
                elif self.square.has_enemy_piece(piece.color):
                    diagonal_moves.append((row, new_row))
                    break
                else:
                    break

            new_row = row + 1
            new_col = col - 1
            while Square.in_range(new_row, new_col):
                if self.squares[row][new_row].has_piece():
                    diagonal_moves.append((row, new_row))
                    new_row += 1
                    new_col -= 1
                elif self.square.has_enemy_piece(piece.color):
                    diagonal_moves.append((row, new_row))
                    break
                else:
                    break

            new_row = row - 1
            new_col = col + 1
            while Square.in_range(new_row, new_col):
                if self.squares[row][new_row].has_piece():
                    diagonal_moves.append((row, new_row))
                    new_row -= 1
                    new_col += 1
                elif self.square.has_enemy_piece(piece.color):
                    diagonal_moves.append((row, new_row))
                    break
                else:
                    break

            new_row = row - 1
            new_col = col - 1
            while Square.in_range(new_row, new_col):
                if self.squares[row][new_row].has_piece():
                    diagonal_moves.append((row, new_row))
                    new_row -= 1
                    new_col -= 1
                elif self.square.has_enemy_piece(piece.color):
                    diagonal_moves.append((row, new_row))
                    break
                else:
                    break

        def knight_moves():
            possible_moves = [
                (row + 1, col + 2),
                (row - 1, col + 2),
                (row + 1, col - 2),
                (row - 1, col - 2),
                (row + 2, col + 1),
                (row - 2, col + 1),
                (row + 2, col - 1),
                (row - 2, col - 1)
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    # print(self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color))
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

        def rook_moves():
            moves = move_horizontally()
            for move in moves:
                initial = Square(row, col)
                final = Square(move[0], move[1])
                move = Move(initial, final)
                piece.add_move(move)

        if isinstance(piece, Pawn):
            pass
        if isinstance(piece, Rook):
            rook_moves()
        if isinstance(piece, Bishop):
            pass
        if isinstance(piece, Knight):
            knight_moves()
        if isinstance(piece, King):
            pass
        if isinstance(piece, Queen):
            pass


    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        self.squares[5][3] = Square(5, 3, Pawn('black'))
        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        self.squares[5][5] = Square(5, 5, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
