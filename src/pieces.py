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
