import chess

class Board:
    def __init__(self):
        self.board = chess.Board()
        self.movesList = []
    
    def executeDigitalMove(self, command, board):
        if self.movesList:
            move = command
            try:
                chessMove = chess.Move.from_uci(move)
                if chessMove in board.legal_moves:
                    board.push(chessMove)
                    print(f"Move executed: {move}")
                else:
                    print(f"Illegal move: {move}")
            except ValueError:
                print(f"Invalid move format: {move}")
        else:
            print("No moves to execute")
        return board
    
    def addMove(self, move):
        self.movesList.append(move)