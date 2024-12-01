import chess
import reconhecimento as r
import playsound as ps

def print_board(board):
    print(board)

def main():
    # cria objeto de reconhecimento (reconhecimento.Reconhecimento())
    rec1 = r.Reconhecimento()

    # defines the board as the chessboard in class Board from python-chess library
    board = chess.Board()
    player_turn = "White"  # White starts the game
    print_board(board)
    move1 = 0
    move2 = 0
    while not board.is_game_over():
        print(f"Turno de {player_turn}")
        # defines move as user's audio
        moves = rec1.reconhecerJogada()
        move1 = moves[0][0]
        move2 = moves[0][1]
        
        move = move1 + move2
        print(move)

        try:
            print(board)
            board.push_uci(move)
        except ValueError:
            print("Movimento inválido ou ilegal. Tente novamente!")
            continue

        print_board(board)
        player_turn = "Black" if player_turn == "White" else "White"

    print("Fim de jogo!")
    print("Resultado: ", board.result())

if __name__ == "__main__":
    main()