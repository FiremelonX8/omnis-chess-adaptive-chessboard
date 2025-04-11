import sounddevice as sd
import queue
import vosk
import json


class VoiceCommandRecognizer:
    def __init__(self, samplerate=16000, grammar=None, modelPath="model/vosk-model-small-en-us-0.15"):
        self.qAux = queue.Queue()
        self.samplerate = samplerate
        self.model = vosk.Model(modelPath)

        # Corrigir: grammar precisa ser uma string JSON se fornecida
        if grammar:
            if isinstance(grammar, list):
                grammar = json.dumps(grammar)
            self.recognizer = vosk.KaldiRecognizer(
                self.model, self.samplerate, grammar)
        else:
            self.recognizer = vosk.KaldiRecognizer(self.model, self.samplerate)

    def callback(self, indata, frames, time, status):
        self.qAux.put(bytes(indata))

    def recognize(self):
        try:
            with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000,
                                   dtype='int16', channels=1, callback=self.callback):
                print("Say a command...")

                while True:
                    data = self.qAux.get()
                    if self.recognizer.AcceptWaveform(data):
                        result = json.loads(self.recognizer.Result())
                        if 'text' in result:
                            recognized = result['text'].strip()
                            if recognized:
                                return recognized
                    else:
                        partial_result = json.loads(
                            self.recognizer.PartialResult())
                        if 'partial' in partial_result:
                            partial = partial_result['partial'].strip()
                            if partial:
                                print("Parcial:", partial)
        except Exception as e:
            print(f"Error in voice recognition: {e}")
            return None

    def concatenate(self, textCommand):
        if not isinstance(textCommand, str):
            return ""
        words = textCommand.split()
        filtered = [w.strip() for w in words if w.lower() != 'play']
        return ''.join(filtered)
