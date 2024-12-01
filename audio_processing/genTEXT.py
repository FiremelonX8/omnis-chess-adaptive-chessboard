import os

#files and ranks
files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8']

#output dir for wav.scp
output_dir = "c:/Users/filip/OneDrive/Documents/GitHub/omnis_chess/AUD_PROC/kaldimodel/"
os.makedirs(output_dir, exist_ok=True)

#create all the possible squares
pos_moves = [file + rank for file in files for rank in ranks]

#create the wav.scp file
with open(os.path.join(output_dir, "text"), "w") as text_file:
    for move in pos_moves:
        text_file.write(f"{move} {move}\n")

print(f"Arquivo text criado com {len(pos_moves)} movimentos.")
