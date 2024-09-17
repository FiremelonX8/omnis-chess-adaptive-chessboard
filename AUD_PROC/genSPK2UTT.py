import os

#files and ranks
files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8']

#output dir for wav.scp
output_dir = "c:/Users/filip/OneDrive/Documents/GitHub/omnis_chess/AUD_PROC/kaldimodel/"
os.makedirs(output_dir, exist_ok=True)

#create all the possible squares
posMoves = [file + rank for file in files for rank in ranks]
speaker = "speaker1"

#create the wav.scp file
with open(os.path.join(output_dir, "spk2utt"), "w") as spk2utt_file:
    spk2utt_file.write(f"{speaker} {' '.join(posMoves)}\n")

print(f"Arquivo spk2utt criado com {len(posMoves)} movimentos.")
