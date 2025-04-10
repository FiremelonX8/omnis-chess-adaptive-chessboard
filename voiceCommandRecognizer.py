import sounddevice as sd
import queue
import vosk
import json


class VoiceCommandRecognizer:
    def __init__(self, samplerate=16000, grammar=None, modelPath="model/vosk-model-small-en-us-0.15"):
        self.qAux = queue.Queue()
        self.samplerate = samplerate
        self.model = vosk.Model(modelPath)
        self.grammar = grammar
        if grammar:
            self.recognizer = vosk.KaldiRecognizer(
                self.model, self.samplerate, self.grammar)
        else:
            self.recognizer = vosk.KaldiRecognizer(self.model, self.samplerate)

    def recognize(self):
        while t < 1:
            t = 1
            try:
                with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, dtype='int16', channels=1, callback=self.callback):
                    print("Say 'play' to start...")
                    while True:
                        data = self.qAux.get()
                        if self.recognizer.AcceptWaveform(data):
                            result = json.loads(self.recognizer.Result())
                            if 'text' in result:
                                return result['text'].strip()
                        else:
                            partial_result = json.loads(
                                self.recognizer.PartialResult())
                            if 'partial' in partial_result:
                                partial = partial_result['partial']
                                if partial == 'play':
                                    print("Starting...")
                                    break
                                else:
                                    print(partial)
                                return partial
            except Exception as e:
                print(f"Error in voice recognition: {e}")
                t = 0

    def concatenate(self, textCommand):
        acumCom = ""
        tC = list(textCommand)
        for i in tC:
            if i == 'play' or i == " ":
                tC.remove(i)
            i.strip()
            acumCom += i
        return acumCom
