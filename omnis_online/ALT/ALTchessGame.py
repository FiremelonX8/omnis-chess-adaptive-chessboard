import chess
from omnis_online.recognition import Reconhecimento

class Chess:
    def __init__(self):
        self.board = chess.Board()
        self.move = None

    def play_game(self):
        rec = Reconhecimento()
        print(self.board)

        while not self.board.is_game_over():
            print(f"Turno do jogador {'Branco' if self.board.turn else 'Preto'}")
            moves = rec.reconhecerJogada()
            move_input = moves[0][0] + moves[0][1]

            try:
                move = chess.Move.from_uci(move_input)
                if move in self.board.legal_moves:
                    self.board.push(move)
                    self.move = move_input
                else:
                    print("Movimento ilegal. Tente novamente.")
            except ValueError:
                print("Formato inválido. Tente novamente.")

            print(self.board)

        print("Fim de jogo!")
        print("Resultado:", self.board.result())
