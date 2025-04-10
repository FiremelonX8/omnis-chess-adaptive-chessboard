from voiceCommandRecognizer import VoiceCommandRecognizer
import json

# loading grammar
with open("json/grammar.json", "r") as f:
    grammar = json.load(f)  # deve ser uma lista de strings
print("Grammar carregada:", grammar, type(grammar))

with open("json/text_to_numbers.json", "r") as f:
    textToNumbers = json.load(f)

# initialize voice recognizer with grammar
vRec = VoiceCommandRecognizer(
    16000,
    grammar,
    "model/vosk-model-small-en-us-0.15"
)

textCommand = vRec.recognize()
print("Recognized command:", textCommand)

mappedCommand = None

if textCommand:
    mappedCommand = textToNumbers.get(textCommand.strip())

if not mappedCommand and len(textCommand.strip()) > 0:
    concatenated = vRec.concatenate(textCommand)
    print("Concatenated command:", concatenated)
    mappedCommand = textToNumbers.get(concatenated)

if mappedCommand is not None:
    print(f"Mapped command: {mappedCommand}")
else:
    print("No command found")
