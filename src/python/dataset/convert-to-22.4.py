import os
import subprocess

# Caminho da pasta com os arquivos .wav
input_folder = "./audios/todo"
output_folder = os.path.join("./audios", "convertidos")
os.makedirs(output_folder, exist_ok=True)

tot = len(os.listdir(input_folder))
pcs = 0

# Loop pelos arquivos .wav
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".wav"):
        pcs += 1
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Comando ffmpeg para converter para 22.05 kHz
        cmd = ["ffmpeg", "-y", "-i", input_path, "-ar", "22050", output_path]

        print(f"Convertendo: {filename}... Arquivo: {pcs}/{tot}")
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Conversão concluída.")
