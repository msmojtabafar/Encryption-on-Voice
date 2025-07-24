🔐 Voice Split & Encrypt
A Python project that takes a voice file, splits it into multiple segments, encrypts each part individually, and finally decrypts and stitches them back together into the original voice.

🎧 "Because every voice has secrets… and we know how to keep them safe."

🚀 Features
🎙️ Audio Splitting – Automatically splits audio files into multiple chunks.

🔒 Secure Encryption – Encrypts each chunk using a password-based key.

🛡️ Chunk-Wise Security – Even if one part is leaked, others stay safe.

🧩 Reconstruction – Decrypts and seamlessly combines chunks back into the original audio.

🖥️ Simple GUI – User-friendly interface using tkinter for non-programmers.

🧰 Requirements
Python 3.8+

pydub

tkinter

cryptography

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

🎮 How to Use
Launch the App

bash
Copy
Edit
python main.py
Choose an Audio File

Supported formats: .wav

Enter Your Password

This will be used to generate encryption keys.

Split & Encrypt

Audio is split and each chunk is encrypted and saved.

Decrypt & Rebuild

Select encrypted chunks and enter the correct password to reconstruct the original audio.

💡 Use Cases
Secure voice messaging

Audio watermarking systems

Privacy-focused voice backups

Audio file obfuscation

🌟 Star this repo if you like the idea!
Feel free to contribute, report issues, or fork the project to make it even better!
