import chess
import omnis_offline.recognition as r
from fuzzywuzzy import fuzz

def print_board(board):
    print(board)

def bestCorrespond(move, target_coordinates):
    best_match = None
    highest_ratio = 0
    for coord in target_coordinates:
        ratio = fuzz.ratio(move.lower(), coord)
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = coord
    return best_match, highest_ratio

def tirarEspaco(rec1):
    jogada = str(rec1.reconhecer())
    jogada = jogada.split(" ")
    x = ""
    for i in jogada:
        x += i
    return x.lower()

def textToMove(jogConcat):
    n = 0
    while n < 2:
        if jogConcat.find("um") >= 0:
            jogConcat = jogConcat.replace("um", "1")
        if jogConcat.find("dois") >= 0:
            jogConcat = jogConcat.replace("dois", "2")
        if jogConcat.find("tres")>=0 or jogConcat.find("três")>=0:
            jogConcat = jogConcat.replace("tres", "3")
            jogConcat = jogConcat.replace("três", "3")
        if jogConcat.find("quatro")>=0:
            jogConcat = jogConcat.replace("quatro", "4")
        if jogConcat.find("cinco")>=0:
            jogConcat = jogConcat.replace("cinco", "5")
        if jogConcat.find("seis")>=0:
            jogConcat = jogConcat.replace("seis", "6")
        if jogConcat.find("sete")>=0:
            jogConcat = jogConcat.replace("sete", "7")
        if jogConcat.find("oito")>=0:
            jogConcat = jogConcat.replace("oito", "8")
        n += 1
    return jogConcat
        
def main():
    # cria objeto de reconhecimento (reconhecimento.Reconhecimento())
    rec1 = r.Reconhecimento()
    jogConcat = str(tirarEspaco(rec1))
    print(jogConcat)

    # defines the board as the chessboard in class Board from python-chess library
    board = chess.Board()
    player_turn = "White"  # White starts the game
    print_board(board)
    move = 0
    while not board.is_game_over():
        print(f"{player_turn}'s turn")
        #move = input("Enter your move in UCI format (e.g., e2e4): ")
        letras = 'abcdefgh'
        numeros = '12345678'
        target_coordinates = [f"{letter1}{number1}{letter2}{number2}" for letter1 in letras for number1 in numeros for letter2 in letras for number2 in numeros]
        #defines move as user's audio
        move = textToMove(jogConcat)
        print(move)
        move = bestCorrespond(move, target_coordinates)[0]
        print(move)

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
