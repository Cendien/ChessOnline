from enum import IntEnum
from copy import copy

class Colour(IntEnum):
    white = 1
    black = -1


class Piece:
    def __init__(self, position, colour, id):
        self.position = position
        self.colour = colour
        self.id = id

    def isMovePossible(self, new_pos, board):
        raise NotImplementedError

    def move(self, new_pos, board):
        if self.isMovePossible(new_pos, board):
            old_piece = copy(board[new_pos[0]][new_pos[1]])
            board[new_pos[0]][new_pos[1]] = self
            board[self.position[0]][self.position[1]] = None
            self.position = new_pos
            if old_piece is not None:
                old_id = old_piece.id
                return old_id
            return 0

    def isFree(self, pos, board):
        inGrid = lambda xy: 0 <= xy[0] <= 7 and 0 <= xy[1] <= 7
        if inGrid(pos):
            return board[pos[0]][pos[1]] is None
        else:
            return False

    def canCapture(self, pos, board):
        inGrid = lambda xy: 0 <= xy[0] <= 7 and 0 <= xy[1] <= 7
        return inGrid(pos) and board[pos[0]][pos[1]] is not None and board[pos[0]][pos[1]].colour != self.colour


class Pawn(Piece):
    def __init__(self, position, colour, id):
        super().__init__(position, colour, id)
        self.hasMoved = False

    def isMovePossible(self, new_pos, board):
        direction = self.colour
        possible_moves = []

        forward = (self.position[0] + direction, self.position[1])
        forward2 = (self.position[0] + 2 * direction, self.position[1])
        [left, right] = [(self.position[0] + direction, self.position[1] - 1),
                         (self.position[0] + direction, self.position[1] + 1)]

        if not self.hasMoved:
            possible_moves.append(forward2)
        if self.isFree(forward, board):
            possible_moves.append(forward)
        if self.canCapture(left, board):
            possible_moves.append(left)
        if self.canCapture(right, board):
            possible_moves.append(right)

        if new_pos in possible_moves:
            return True
        else:
            raise ValueError

    def move(self, new_pos, board):
        if self.isMovePossible(new_pos, board):
            board[new_pos[0]][new_pos[1]] = self
            board[self.position[0]][self.position[1]] = None
            self.position = new_pos
            self.hasMoved = True


class Rook(Piece):
    def __init__(self, position, colour, id):
        super().__init__(position, colour, id)

    def isMovePossible(self, new_pos, board):
        possible_moves = []
        y = self.position[0]
        x = self.position[1]
        x += 1
        y += 1
        while x < 8:
            if self.isFree((self.position[0], x), board):
                possible_moves.append((self.position[0], x))
                x += 1
            elif self.canCapture((self.position[0], x), board):
                possible_moves.append((self.position[0], x))
                break
            else:
                break
        while y < 8:
            if self.isFree((y, self.position[1]), board):
                possible_moves.append((y, self.position[1]))
                y += 1
            elif self.canCapture((y, self.position[1]), board):
                possible_moves.append((y, self.position[1]))
                break
            else:
                break
        y = self.position[0]
        x = self.position[1]
        x -= 1
        y -= 1
        while x >= 0:
            if self.isFree((self.position[0], x), board):
                possible_moves.append((self.position[0], x))
                x -= 1
            elif self.canCapture((self.position[0], x), board):
                possible_moves.append((self.position[0], x))
                break
            else:
                break
        while y >= 0:
            if self.isFree((y, self.position[1]), board):
                possible_moves.append((y, self.position[1]))
                y -= 1
            elif self.canCapture((y, self.position[1]), board):
                possible_moves.append((y, self.position[1]))
                break
            else:
                break

        if new_pos in possible_moves:
            return True
        else:
            raise ValueError


class Knight(Piece):
    def __init__(self, position, colour, id):
        super().__init__(position, colour, id)

    def isMovePossible(self, new_pos, board):
        raise NotImplementedError


class King(Piece):
    def __init__(self, position, colour, id):
        super().__init__(position, colour, id)

    def isMovePossible(self, new_pos, board):
        raise NotImplementedError


class Queen(Piece):
    def __init__(self, position, colour, id):
        super().__init__(position, colour, id)

    def isMovePossible(self, new_pos, board):
        raise NotImplementedError


class Bishop(Piece):
    def __init__(self, position, colour, id):
        super().__init__(position, colour, id)

    def isMovePossible(self, new_pos, board):
        raise NotImplementedError
