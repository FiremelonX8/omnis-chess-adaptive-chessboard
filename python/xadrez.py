import chess
import reconhecimento as r


def print_board(board):
    print(board)


def main():
    # cria objeto de reconhecimento (reconhecimento.Reconhecimento())
    rec1 = r.Reconhecimento()

    # defines the board as the chessboard in class Board from python-chess library
    board = chess.Board()
    player_turn = "White"  # White starts the game
    print_board(board)

    while not board.is_game_over():
        print(f"{player_turn}'s turn")
        # move = input("Enter your move in UCI format (e.g., e2e4): ")

        # defines move as user's audio
        move = rec1.reconhecer_audio()

        # print(rec1.jogada_f)
        try:
            board.push_uci(move)
        except ValueError:
            print("Invalid move format or illegal move. Try again.")
            continue

        print_board(board)
        player_turn = "Black" if player_turn == "White" else "White"

    print("Fim de jogo!")
    print("Resultado: ", board.result())


if __name__ == "__main__":
    main()
