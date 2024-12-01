import os

#dir where the audio files are in
audio_dir = "c:/Users/filip/OneDrive/Documents/GitHub/omnis_chess/AUD_PROC/kaldiaudios/"

#ranks and files
colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
linhas = ['1', '2', '3', '4', '5', '6', '7', '8']

#output dir for wav.scp
output_dir = "c:/Users/filip/OneDrive/Documents/GitHub/omnis_chess/AUD_PROC/kaldimodel/"
os.makedirs(output_dir, exist_ok=True)

#create all the possible squares
movimentos_possiveis = [coluna + linha for coluna in colunas for linha in linhas]

#create the wav.scp file
with open(os.path.join(output_dir, "wav.scp"), "w") as wav_scp:
    for movimento in movimentos_possiveis:
        audio_file = os.path.join(audio_dir, f"{movimento}.wav")
        wav_scp.write(f"{movimento} {audio_file}\n")

print(f"Arquivo wav.scp criado com {len(movimentos_possiveis)} movimentos.")
