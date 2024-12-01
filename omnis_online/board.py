# adaptações são necessárias ainda

import RPi.GPIO as GPIO
import time
import smbus
import chess
from datetime import datetime

# Configurações iniciais
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pinos de Controle do Motor e Eletroímã
MOTOR_RIGHT_STEP = 27
MOTOR_RIGHT_DIR = 29
MOTOR_LEFT_STEP = 40
MOTOR_LEFT_DIR = 39
MAGNET = 12

# # Configuração do display LCD via I2C
# LCD_ADDRESS = 0x20
# bus = smbus.SMBus(1)
# lcd_columns = 16
# lcd_rows = 2

# Variáveis de controle do jogo
game_board = chess.Board()
sequence = "start"
new_turn_countdown = False
timer = datetime.now()

# Configuração dos pinos GPIO
GPIO.setup(MAGNET, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_STEP, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_DIR, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_STEP, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_DIR, GPIO.OUT)

# # Função de controle do LCD
# def lcd_display(line1, line2=""):
#     print(f"LCD Line 1: {line1}")
#     print(f"LCD Line 2: {line2}")
#     # Aqui usaremos o I2C para escrever no LCD. O exemplo a seguir é simplificado
#     # bus.write_byte_data(LCD_ADDRESS, 0x80, ord(line1))  # Implementar com controle específico da biblioteca do LCD

# Funções de controle de hardware


def motor(direction, speed, distance):
    step_number = int(distance * 1.0)  # Considerando SQUARE_SIZE = 1.0
    GPIO.output(MOTOR_RIGHT_DIR, GPIO.HIGH if direction in [
                'R_L', 'T_B'] else GPIO.LOW)
    GPIO.output(MOTOR_LEFT_DIR, GPIO.HIGH if direction in [
                'B_T', 'R_L'] else GPIO.LOW)

    for _ in range(step_number):
        GPIO.output(MOTOR_RIGHT_STEP, GPIO.HIGH)
        GPIO.output(MOTOR_LEFT_STEP, GPIO.HIGH)
        time.sleep(speed / 1e6)  # Converte microsegundos para segundos
        GPIO.output(MOTOR_RIGHT_STEP, GPIO.LOW)
        GPIO.output(MOTOR_LEFT_STEP, GPIO.LOW)
        time.sleep(speed / 1e6)


def electromagnet(state):
    GPIO.output(MAGNET, GPIO.HIGH if state else GPIO.LOW)
    time.sleep(0.6)

# Funções do Jogo


def setup():
    # lcd_display("AUTOMATIC", "CHESSBOARD")
    time.sleep(2)
    # lcd_display("CALIBRATION", "")
    calibrate()
    # lcd_display("PLAYER 1 TO MOVE")


def loop():
    global sequence
    while not game_board.is_game_over():
        # lcd_display("Player 1" if game_board.turn else "Player 2", "Your Move")
        print(game_board)

        move = input("Enter move (e.g., e2e4): ")
        if chess.Move.from_uci(move) in game_board.legal_moves:
            game_board.push(chess.Move.from_uci(move))
            move_piece(move)
            sequence = "player_black" if game_board.turn else "player_white"
        else:
            print("Invalid move. Try again.")

    # lcd_display("GAME OVER")
    GPIO.cleanup()


def calibrate():
    # Movimentos rápidos até a posição inicial (e7)
    motor("R_L", 500, 7)
    motor("T_B", 500, 7)


def move_piece(move):
    start_x, start_y = ord(move[0]) - ord('a'), 8 - int(move[1])
    end_x, end_y = ord(move[2]) - ord('a'), 8 - int(move[3])

    # Calcula deslocamento em X e Y
    displacement_x, displacement_y = end_x - start_x, end_y - start_y

    # Movimentos de transição
    motor("T_B" if displacement_x > 0 else "B_T", 1000, abs(displacement_x))
    motor("L_R" if displacement_y > 0 else "R_L", 1000, abs(displacement_y))
    electromagnet(True)  # Agarra a peça

    # Movimentação final
    motor("B_T" if displacement_x > 0 else "T_B", 1000, abs(displacement_x))
    motor("R_L" if displacement_y > 0 else "L_R", 1000, abs(displacement_y))
    electromagnet(False)  # Solta a peça

# Função principal


if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
