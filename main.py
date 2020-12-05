import json
from back.board import *

def cl_ui(board):
    for i in range(7, -1, -1):
        line = ""
        for j in range(8):
            if board[i][j] is None:
                line += "0"
            else:
                if isinstance(board[i][j], Rook):
                    line += "R"
                if isinstance(board[i][j], Knight):
                    line += "N"
                if isinstance(board[i][j], Bishop):
                    line += "B"
                if isinstance(board[i][j], King):
                    line += "K"
                if isinstance(board[i][j], Queen):
                    line += "Q"
                if isinstance(board[i][j], Pawn):
                    line += "P"
        print(line)


new_board = Board()
board_json = new_board.getBoardJSON()
print(board_json)

piece_id = list(board_json.keys())[0]

a = json.dumps(new_board.getBoardJSON())
print(a)
b = json.loads(a)
print(new_board.setNewPiecePosition(piece_id, (6, 0)))
for i in range(8):
    new_board.setNewPiecePosition(piece_id, (6, i))
    cl_ui(new_board.board)
    print("")
a = json.dumps(new_board.getBoardJSON())
b = json.loads(a)
print(b[piece_id])
a = json.dumps(new_board.getBoardJSON())
print(len(json.loads(a)))