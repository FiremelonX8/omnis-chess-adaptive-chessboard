from voiceCommandRecognizer import VoiceCommandRecognizer
import json

with open("grammar.json", "r") as f:
    grammar = json.load(f)
with open("textToNumbers.json", "r") as f:
    textToNumbers = json.load(f)

vRec = VoiceCommandRecognizer(16000, json.dumps(grammar))
textCommand = vRec.recognize()
print(textCommand)
if textCommand:
    mappedCommand = textToNumbers.get(textCommand)
if len(textCommand) > 0:
    textCommand = vRec.concatenate(textCommand)
    print(textCommand)
