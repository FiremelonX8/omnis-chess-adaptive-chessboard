import vosk as vk
import pyaudio
import queue
import json

model = vk.Model("C:/Users/filip/OneDrive/Documents/GitHub/omnis_chess/testeVOSK/vosk-model-small-pt-0.3")
audioQueue = queue.Queue()

HZ = 16000 #samplerate - this model works in 16000 hertz
DEVICE = 1 #audio DEVICE index
CHUNK_SIZE = 64000 #audio block size
CHANNELS = 1 #mono audio

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                 channels=CHANNELS,
                 rate=HZ,
                 input=True,
                 frames_per_buffer=CHUNK_SIZE)

def rec():
    recognizer = vk.KaldiRecognizer(model, HZ)

    print("Fale")

    while True:
        data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
        audioQueue.put(data)
        
        if recognizer.AcceptWaveform(data):
            res = json.loads(recognizer.Result())
            print(res.get("text", ""))
        else:
            print("partial result:", json.loads(recognizer.PartialResult()).get("partial", ""))

if __name__ == "__main__":
    try:
        rec()
    except KeyboardInterrupt:
        print("rec interrompido")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()