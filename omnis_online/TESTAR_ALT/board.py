import RPi.GPIO as GPIO
import time
from datetime import datetime
from chessGame import Chess

chessGame = Chess()

#initial config GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#gpio pinout config
PINS = {
    "MOTOR_RIGHT_STEP": 27,
    "MOTOR_RIGHT_DIR": 22,
    "MOTOR_LEFT_STEP": 23,
    "MOTOR_LEFT_DIR": 24,
    "MAGNET": 12
}

for pin in PINS.values():
    GPIO.setup(pin, GPIO.OUT)

#moves const
SQUARE_SIZE = 1.0  # Ajuste do tamanho de um quadrado
DEFAULT_SPEED = 1000  # Velocidade padrão em microsegundos

# Funções de hardware
def motor(direction, speed=DEFAULT_SPEED, distance=SQUARE_SIZE):
    steps = int(distance * 100)  # Conversão para número de passos
    GPIO.output(PINS["MOTOR_RIGHT_DIR"], GPIO.HIGH if direction in ["R_L", "T_B"] else GPIO.LOW)
    GPIO.output(PINS["MOTOR_LEFT_DIR"], GPIO.HIGH if direction in ["B_T", "R_L"] else GPIO.LOW)

    for _ in range(steps):
        GPIO.output(PINS["MOTOR_RIGHT_STEP"], GPIO.HIGH)
        GPIO.output(PINS["MOTOR_LEFT_STEP"], GPIO.HIGH)
        time.sleep(speed / 1e6)  # Microsegundos para segundos
        GPIO.output(PINS["MOTOR_RIGHT_STEP"], GPIO.LOW)
        GPIO.output(PINS["MOTOR_LEFT_STEP"], GPIO.LOW)
        time.sleep(speed / 1e6)

def electromagnet(state):
    GPIO.output(PINS["MAGNET"], GPIO.HIGH if state else GPIO.LOW)
    time.sleep(0.6)

def calibrate():
    # Move rapidamente para a posição inicial
    motor("R_L", 500, 7)
    motor("T_B", 500, 7)

def move_piece(move):
    start_x, start_y = ord(move[0]) - ord('a'), 8 - int(move[1])
    end_x, end_y = ord(move[2]) - ord('a'), 8 - int(move[3])

    displacement_x, displacement_y = end_x - start_x, end_y - start_y

    #transition moves
    motor("T_B" if displacement_x > 0 else "B_T", DEFAULT_SPEED, abs(displacement_x))
    motor("L_R" if displacement_y > 0 else "R_L", DEFAULT_SPEED, abs(displacement_y))
    electromagnet(True)  #grabs piece

    #final moves
    motor("B_T" if displacement_x > 0 else "T_B", DEFAULT_SPEED, abs(displacement_x))
    motor("R_L" if displacement_y > 0 else "L_R", DEFAULT_SPEED, abs(displacement_y))
    electromagnet(False)  #releases piece

#main func
if __name__ == "__main__":
    try:
        #initial calib
        calibrate()

        #maing logic
        while not chessGame.board.is_game_over():
            print(chessGame.board)
            chessGame.play_game()
            move_piece(chessGame.move)

        print("Fim de jogo!")
    except KeyboardInterrupt:
        print("Encerrando...")
    finally:
        GPIO.cleanup()
