import json
from voiceCommandRecognizer import VoiceCommandRecognizer
from board import Board
from move import Move

with open("json/grammar.json", "r") as f:
    grammar = json.load(f)  # deve ser uma lista de strings
print("Grammar carregada:", grammar, type(grammar))

with open("json/text_to_numbers.json", "r") as f:
    textToNumbers = json.load(f)

vRec = VoiceCommandRecognizer(
    16000,
    grammar,
    "model/vosk-model-small-en-us-0.15"
)
b = Board()
while not b.digiBoard.is_game_over():
    print(b.digiBoard)
    textCommand = vRec.recognize()
    m = Move(textCommand)
    command = m.mapCommand(vRec, textToNumbers)
    b.addMove(command)
    digiBoard = b.executeDigitalMove(command, None)
    print("Board after move {command}: ", digiBoard)

print("End of program")
