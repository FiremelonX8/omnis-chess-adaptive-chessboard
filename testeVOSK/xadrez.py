import chess
import reconhecimento as r
import playsound as ps
import fuzzywuzzy as fw

def print_board(board):
    print(board)

def melhor_correspond(move, target_coordinates):
    best_match = None
    highest_ratio = 0
    for coord in target_coordinates:
        ratio = fw.ratio(move.lower(), coord)
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = coord
    return best_match, highest_ratio

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
        print(f"{player_turn}'s turn")
        #move = input("Enter your move in UCI format (e.g., e2e4): ")
        letras = 'abcdefgh'
        numeros = '12345678'
        target_coordinates = [f"{letter1}{number1}{letter2}{number2}" for letter1 in letras for number1 in numeros for letter2 in letras for number2 in numeros]
        #defines move as user's audio
        move1 = rec1.reconhecer_audio()[0][0]
        move2 = rec1.reconhecer_audio()[0][1]
        move1 = melhor_correspond(move1, target_coordinates)
        move2 = melhor_correspond(move2, target_coordinates)
        move = move1 + move2

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
