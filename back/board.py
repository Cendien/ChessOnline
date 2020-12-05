import uuid
from back.pieces import *
import json
import copy

START_BOARD = {(0,0): "wr", (0,1): "wn", (0,2): "wb", (0,3): "wq", (0,4): "wk", (0,5): "wb", (0,6): "wn", (0,7): "wr",
               (1,0): "0", (1,1): "wp", (1,2): "wp", (1,3): "wp", (1,4): "wp", (1,5): "wp", (1,6): "wp", (1,7): "wp",
               (2,0): "0", (2,1): "0", (2,2): "0", (2,3): "0", (2,4): "0", (2,5): "0", (2,6): "0", (2,7): "0",
               (3,0): "0", (3,1): "0", (3,2): "0", (3,3): "0", (3,4): "0", (3,5): "0", (3,6): "0", (3,7): "0",
               (4,0): "0", (4,1): "0", (4,2): "0", (4,3): "0", (4,4): "0", (4,5): "0", (4,6): "0", (4,7): "0",
               (5,0): "0", (5,1): "0", (5,2): "0", (5,3): "0", (5,4): "0", (5,5): "0", (5,6): "0", (5,7): "0",
               (6,0): "bp", (6,1): "bp", (6,2): "bp", (6,3): "bp", (6,4): "bp", (6,5): "bp", (6,6): "bp", (6,7): "bp",
               (7,0): "br", (7,1): "bn", (7,2): "bb", (7,3): "bq", (7,4): "bk", (7,5): "bb", (7,6): "bn", (7,7): "br"}

EMPTY_ROW = [None, None, None, None, None, None, None, None]


class Board:
    def __init__(self):
        self.board_json = {}
        self.board = []
        for i in range(8):
            self.board.append(copy.copy(EMPTY_ROW))
            for j in range(8):
                piece_name = START_BOARD[(i, j)]

                if piece_name is "0":
                    continue

                new_piece = None
                new_piece_id = str(uuid.uuid1())

                #  white
                if piece_name is "wr":
                    new_piece = Rook((i, j), Colour.white, new_piece_id)
                elif piece_name is "wn":
                    new_piece = Knight((i, j), Colour.white, new_piece_id)
                elif piece_name is "wb":
                    new_piece = Bishop((i, j), Colour.white, new_piece_id)
                elif piece_name is "wq":
                    new_piece = Queen((i, j), Colour.white, new_piece_id)
                elif piece_name is "wk":
                    new_piece = King((i, j), Colour.white, new_piece_id)
                elif piece_name is "wp":
                    new_piece = Pawn((i, j), Colour.white, new_piece_id)

                #  black
                elif piece_name is "br":
                    new_piece = Rook((i, j), Colour.black, new_piece_id)
                elif piece_name is "bn":
                    new_piece = Knight((i, j), Colour.black, new_piece_id)
                elif piece_name is "bb":
                    new_piece = Bishop((i, j), Colour.black, new_piece_id)
                elif piece_name is "bq":
                    new_piece = Queen((i, j), Colour.black, new_piece_id)
                elif piece_name is "bk":
                    new_piece = King((i, j), Colour.black, new_piece_id)
                elif piece_name is "bp":
                    new_piece = Pawn((i, j), Colour.black, new_piece_id)

                self.board[i][j] = new_piece
                self.board_json[str(new_piece_id)] = {"name": piece_name, "pos": (i, j), "colour": new_piece.colour}

    def setNewPiecePosition(self, id, pos):
        for i in range(8):
            for piece in self.board[i]:
                if piece is not None and piece.id is id:
                    try:
                        old_id = piece.move(pos, self.board)
                        if old_id != 0:
                            self.board_json.pop(str(old_id))
                        self.board_json[str(id)] = {"name": self.board_json[str(id)]["name"],
                                                    "pos": pos,
                                                    "colour": self.board_json[str(id)]["colour"]}
                        return "OK"
                    except ValueError:
                        return "NOT OK"
        return "NOT OK"

    def getBoardJSON(self):
        return self.board_json

    def getBoard(self):
        return self.board