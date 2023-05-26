from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        if isinstance(piece, Pawn):
            if final.row == 0 or final.row == 7:
                self.squares[final.row][final.col].piece = Queen(piece.color)


        piece.moved = True
        if peice True = board.moved

        piece.clear_moves()

        self.last_move = move

    def calc_moves(self, piece, row, col):
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

        def king_moves():
            possible_moves = [
                (row + 1, col + 1),
                (row + 1, col - 1),
                (row - 1, col + 1),
                (row - 1, col - 1),
                (row, col + 1),
                (row, col - 1),
                (row + 1, col),
                (row - 1, col)
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                # print(isinstance(self.squares[possible_move_row][possible_move_col].piece, King))
                if Square.in_range(possible_move_row, possible_move_col):
                    # print(self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color))
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

        def pawn_moves():
            moves = []
            color = self.squares[row][col].piece.color
            if color == 'black' and self.squares[row + 1][col].is_empty():
                moves.append((row + 1, col))
                if row == 1 and self.squares[row + 2][col].is_empty():
                    moves.append((row + 2, col))
            elif color == 'white' and self.squares[row - 1][col].is_empty():
                moves.append((row - 1, col))
                if row == 6 and self.squares[row - 2][col].is_empty():
                    moves.append((row - 2, col))

            if color == 'black':
                if row + 1 < 8 and col + 1 < 8:
                    if self.squares[row + 1][col + 1].has_enemy_piece(piece.color):
                        moves.append((row + 1, col + 1))
                if row + 1 < 8 and col - 1 > -1:
                    if self.squares[row + 1][col - 1].has_enemy_piece(piece.color):
                        moves.append((row + 1, col - 1))

            if color == 'white':
                if row - 1 > -1 and col - 1 > -1:
                    if self.squares[row - 1][col - 1].has_enemy_piece(piece.color):
                        moves.append((row - 1, col - 1))
                if row - 1 > -1 and col + 1 < 8:
                    if self.squares[row - 1][col + 1].has_enemy_piece(piece.color):
                        moves.append((row - 1, col + 1))

            for move in moves:
                initial = Square(row, col)
                final = Square(move[0], move[1])
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
                if not self.squares[new_row][col].has_piece():
                    vertical_moves.append((new_row, col))
                    new_row += 1
                elif self.squares[new_row][col].has_enemy_piece(piece.color):
                    vertical_moves.append((new_row, col))
                    break
                else:
                    break

            new_row = row - 1
            while new_row > -1:

                if not self.squares[new_row][col].has_piece():
                    vertical_moves.append((new_row, col))
                    new_row -= 1
                elif self.squares[new_row][col].has_enemy_piece(piece.color):
                    vertical_moves.append((new_row, col))
                    print('first_break')
                    break
                else:
                    print('second_break')
                    break

            return vertical_moves

        def move_diagonally():
            diagonal_moves = []
            new_row = row + 1
            new_col = col + 1
            while Square.in_range(new_row, new_col):
                if not self.squares[new_row][new_col].has_piece():
                    diagonal_moves.append((new_row, new_col))
                    new_row += 1
                    new_col += 1
                elif self.squares[new_row][new_col].has_enemy_piece(piece.color):
                    diagonal_moves.append((new_row, new_col))
                    break
                else:
                    break

            new_row = row + 1
            new_col = col - 1
            # print(row, col, 'original')
            while Square.in_range(new_row, new_col):
                if not self.squares[new_row][new_col].has_piece():
                    diagonal_moves.append((new_row, new_col))
                    new_row += 1
                    new_col -= 1
                elif self.squares[new_row][new_col].has_enemy_piece(piece.color):
                    diagonal_moves.append((new_row, new_col))
                    break
                else:
                    break

            new_row = row - 1
            new_col = col + 1
            while Square.in_range(new_row, new_col):
                if not self.squares[new_row][new_col].has_piece():
                    diagonal_moves.append((new_row, new_col))
                    new_row -= 1
                    new_col += 1
                elif self.squares[new_row][new_col].has_enemy_piece(piece.color):
                    diagonal_moves.append((new_row, new_col))
                    break
                else:
                    break

            new_row = row - 1
            new_col = col - 1
            while Square.in_range(new_row, new_col):
                if not self.squares[new_row][new_col].has_piece():
                    diagonal_moves.append((new_row, new_col))
                    new_row -= 1
                    new_col -= 1
                elif self.squares[new_row][new_col].has_enemy_piece(piece.color):
                    diagonal_moves.append((new_row, new_col))
                    break
                else:
                    break

            return diagonal_moves

        def bishop_moves():
            moves = move_diagonally()
            for move in moves:
                initial = Square(row, col)
                final = Square(move[0], move[1])
                move = Move(initial, final)
                piece.add_move(move)

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
            moves_horiz = move_horizontally()
            moves_vert = move_vertically()
            moves = moves_horiz + moves_vert
            for move in moves:
                initial = Square(row, col)
                final = Square(move[0], move[1])
                move = Move(initial, final)
                piece.add_move(move)

        def queen_moves():
            moves_horiz = move_horizontally()
            moves_vert = move_vertically()
            moves_diag = move_diagonally()
            moves = moves_horiz + moves_diag + moves_vert
            for move in moves:
                initial = Square(row, col)
                final = Square(move[0], move[1])
                move = Move(initial, final)
                piece.add_move(move)

        if isinstance(piece, Pawn):
            pawn_moves()
        if isinstance(piece, Rook):
            rook_moves()
        if isinstance(piece, Bishop):
            bishop_moves()
        if isinstance(piece, Knight):
            knight_moves()
        if isinstance(piece, King):
            king_moves()
        if isinstance(piece, Queen):
            queen_moves()

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        # self.squares[5][4] = Square(5, 4, Bishop('black'))

        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))


        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
