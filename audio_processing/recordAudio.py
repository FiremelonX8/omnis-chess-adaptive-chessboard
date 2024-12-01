import pyaudio
import wave
import string

# Parâmetros da gravação
fs = 16000  # Taxa de amostragem
duration = 1.5  # Duração em segundos
channels = 1  # Mono
frames_per_buffer = 1024  # Tamanho do buffer
format = pyaudio.paInt16  # Formato de áudio: 16 bits

# Função para gravar áudio
def gravar_audio(file_name, duration, fs):
    p = pyaudio.PyAudio()
    
    # Abrir stream para gravação
    stream = p.open(format=format,
                    channels=channels,
                    rate=fs,
                    input=True,
                    input_device_index=1,  # Substitua pelo índice correto do microfone
                    frames_per_buffer=frames_per_buffer)

    print(f"Gravando {file_name}...")

    frames = []

    # Gravar áudio por 'duration' segundos
    for _ in range(0, int(fs / frames_per_buffer * duration)):
        data = stream.read(frames_per_buffer)
        frames.append(data)

    print(f"Gravação {file_name} terminada.")

    # Fechar stream e PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Salvar em um arquivo WAV
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))

# Lista de alfabetos A-H, seguido de números 1-2 para gerar 16 nomes únicos
alphabet = list(string.ascii_uppercase[:8])

# Repetir a gravação 16 vezes
for i, letter in enumerate(alphabet):
    for j in range(1, 9):  # Gera 1 e 2 para cada letra
        file_name = f"{letter}{j}.wav"  # Nome do arquivo: A1.wav, A2.wav, B1.wav, ..., H2.wav
        gravar_audio(file_name, duration, fs)
