import os
import base64
from tkinter import filedialog, Tk, Label, Entry, Button, StringVar
from pydub import AudioSegment
from cryptography.fernet import Fernet
import hashlib

def password_to_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def split_and_encrypt(file_path, password):
    audio = AudioSegment.from_wav(file_path)
    duration = len(audio)
    part_length = duration // 3
    key = password_to_key(password)
    f = Fernet(key)

    os.makedirs("encrypted_parts", exist_ok=True)

    for i in range(3):
        start = i * part_length
        end = duration if i == 2 else (i + 1) * part_length
        part = audio[start:end]
        part_path = f"part{i}.wav"
        part.export(part_path, format="wav")

        with open(part_path, "rb") as f_in:
            data = f_in.read()
        encrypted_data = f.encrypt(data)
        with open(f"encrypted_parts/part{i}.enc", "wb") as f_out:
            f_out.write(encrypted_data)

        os.remove(part_path)

def decrypt_and_join(password):
    key = password_to_key(password)
    f = Fernet(key)
    combined_audio = AudioSegment.empty()

    for i in range(3):
        with open(f"encrypted_parts/part{i}.enc", "rb") as f_in:
            encrypted = f_in.read()
        decrypted = f.decrypt(encrypted)

        temp_path = f"temp_part{i}.wav"
        with open(temp_path, "wb") as temp_file:
            temp_file.write(decrypted)

        part = AudioSegment.from_wav(temp_path)
        combined_audio += part

        os.remove(temp_path)

    combined_audio.export("reconstructed.wav", format="wav")
    print("✅ Reconstructed file: reconstructed.wav")

# GUI
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("WAV Files", "*.wav")])
    selected_file_path.set(file_path)

def start_encryption():
    file = selected_file_path.get()
    pwd = password.get()
    if file and pwd:
        split_and_encrypt(file, pwd)
        status.set("🔒 Encryption was successful.")

def start_decryption():
    pwd = password.get()
    if pwd:
        decrypt_and_join(pwd)
        status.set("🔓 Decryption and connection completed.")

app = Tk()
app.title("WAV file encryption")

selected_file_path = StringVar()
password = StringVar()
status = StringVar()

Label(app, text="📂 Select WAV file:").pack()
Button(app, text="File selection", command=select_file).pack()

Label(app, text="🔑 Password:").pack()
Entry(app, textvariable=password, show="*").pack()

Button(app, text="🔒 File encryption", command=start_encryption).pack(pady=5)
Button(app, text="🔓 Decoding and connection", command=start_decryption).pack(pady=5)

Label(app, textvariable=status, fg="green").pack(pady=10)

app.mainloop()
