import json
from voiceCommandRecognizer import VoiceCommandRecognizer
from board import Board
from move import TextMove

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
while (not b.digiBoard.is_game_over()):
    print(b.digiBoard)
    textCommand = vRec.recognize()
    m = TextMove(textCommand)
    command = m.mapCommand(vRec, textToNumbers)
    if not (command is None) and "stop" in command:
        break
    print(command)
    digiBoard = b.executeDigitalMove(command)
    print("Board after move {command}: ", digiBoard)

print("End of program")
