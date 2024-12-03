import vosk as vk
import pyaudio
import queue
import json

class Reconhecimento:
    def __init__(self):
        self.audioQueue = queue.Queue()
        self.model = vk.Model("")
        self.HZ = 16000
        self.DEVICE = 1
        self.CHUNK_SIZE = 80000
        self.CHANNELS = 1
        self.recognizer = vk.KaldiRecognizer(self.model, self.HZ)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                 channels=self.CHANNELS,
                 rate=self.HZ,
                 input=True,
                 frames_per_buffer=self.CHUNK_SIZE)
        self.res = None

    def reconhecer(self):
        r = False
        recognizer = vk.KaldiRecognizer(self.model, self.HZ)
        while r == False:
            print("Falar")
            data = self.stream.read(self.CHUNK_SIZE, exception_on_overflow=False)
            self.audioQueue.put(data)
            if self.recognizer.AcceptWaveform(data):
                self.res = json.loads(self.recognizer.Result())
                print(self.res.get("text", ""))
                r = True
                self.stream.stop_stream
                self.stream.close()
                self.p.terminate()
                return self.res.get("text", "")
