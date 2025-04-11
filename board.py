import chess


class Board:
    def __init__(self):
        self.digiBoard = chess.Board()
        self.movesList = []

    def executeDigitalMove(self, command):
        try:
            move = command
            try:
                chessMove = chess.Move.from_uci(move)
                if chessMove in self.digiBoard.legal_moves:
                    self.digiBoard.push(chessMove)
                    print(f"Move executed: {move}")
                    self.addMove(chessMove)
                else:
                    print(f"Illegal move: {move}")
            except ValueError:
                print(f"Invalid move format: {move}")
        except:
            print("No moves to execute")
        return self.digiBoard

    def addMove(self, move):
        self.movesList.append(move)

    def executePhysicalMove(self, command):
        pass
        # raspberry pi code logic
