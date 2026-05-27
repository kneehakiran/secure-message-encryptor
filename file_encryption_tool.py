# File Encryption Tool
import tkinter as tk
window = tk.Tk()
window.title("File Encryption Tool")
window.geometry("500x400")
window.config(bg="#1e1e1e")

title_label = tk.Label(
    window,
    text="🔐 File Encryption Tool",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)
title_label.pack(pady=5)
message_label = tk.Label(window, text="Enter Message", bg="#1e1e1e",
fg="white")
message_label.pack(pady=5)
message_entry = tk.Entry(window, width=40)
message_entry.pack(pady=5)
key_label = tk.Label(window, text="Enter Secret Key", bg="#1e1e1e",
fg="white")
key_label.pack(pady=5)
key_entry = tk.Entry(window, width=40)
key_entry.pack(pady=5)
output_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
    bg="#1e1e1e",
    fg="lime"
)
output_label.pack(pady=5)

#Encryption
def encrypt_message():
    message = message_entry.get()
    key = int(key_entry.get())
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) + key)
    output_label.config(text="Encrypted: " + encrypted_message)
encrypt_button = tk.Button(
    window,
    text="Encrypt",
    bg="cyan",
    fg="black",
    width=15,
    command=encrypt_message
)
encrypt_button.pack(pady=5)

#Decryption
def decrypt_message():
    message = message_entry.get()
    key = int(key_entry.get())
    decrypted_message = ""
    for char in message:
        decrypted_message += chr(ord(char) - key)
    output_label.config(text="Decrypted: " + decrypted_message)
decrypt_button = tk.Button(
    window,
    text="Decrypt",
    bg="orange",
    fg="black",
    width=15,
    command=decrypt_message
)
decrypt_button.pack(pady=5)

window.mainloop()