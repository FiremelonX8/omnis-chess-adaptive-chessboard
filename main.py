from voiceCommandRecognizer import VoiceCommandRecognizer
import json

with open("json/grammar.json", "r") as f:
    grammar = json.load(f)
print(grammar, type(grammar))
with open("json/text_to_numbers.json", "r") as f:
    textToNumbers = json.load(f)

vRec = VoiceCommandRecognizer(
    16000, grammar, "model/vosk-model-small-en-us-0.15")
textCommand = vRec.recognize()
print(textCommand)
if textCommand:
    mappedCommand = textToNumbers.get(textCommand)
if len(textCommand) > 0:
    textCommand = vRec.concatenate(textCommand)
    print(textCommand)
    mappedCommand = textToNumbers.get(textCommand)

print(mappedCommand)
if mappedCommand is not None:
    print(f"Mapped command: {mappedCommand}")
else:
    print("No command found")
