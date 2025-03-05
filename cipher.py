import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    return ''.join(chr((ord(c) + shift) % 256) if mode == 'encrypt' else chr((ord(c) - shift) % 256) for c in text)

def process_message(action):
    try:
        message = message_entry.get() if action == "encrypt" else cipher_text_output.get(1.0, tk.END).strip()
        if not message:
            messagebox.showerror("Invalid Input", "Please enter a message.")
            return
        shift = shift_value_slider.get()
        result = caesar_cipher(message, shift, action)
        if action == "encrypt":
            cipher_text_output.delete(1.0, tk.END)
            cipher_text_output.insert(tk.END, result)
            decrypted_text_output.delete(1.0, tk.END)
        else:
            decrypted_text_output.delete(1.0, tk.END)
            decrypted_text_output.insert(tk.END, ''.join(c for c in result if c.isalnum() or c in ['@', '.', '-', '_']))
    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid input for shift key.")

def refresh():
    message_entry.delete(0, tk.END)
    shift_value_slider.set(0)
    cipher_text_output.delete(1.0, tk.END)
    decrypted_text_output.delete(1.0, tk.END)

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("800x400")

tk.Label(root, text="Enter your message:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

tk.Label(root, text="Select shift (0-255):").pack(pady=5)
shift_value_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, length=300)
shift_value_slider.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Encrypt", command=lambda: process_message("encrypt"), bg="darkblue", fg="white").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Decrypt", command=lambda: process_message("decrypt"), bg="darkgreen", fg="white").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Refresh", command=refresh, bg="gray", fg="white").grid(row=0, column=2, padx=5)

output_frame = tk.Frame(root)
output_frame.pack(pady=10)

tk.Label(output_frame, text="Cipher Text:").grid(row=0, column=0, padx=10)
cipher_text_output = tk.Text(output_frame, height=6, width=30)
cipher_text_output.grid(row=1, column=0, padx=10)

tk.Label(output_frame, text="Decrypted Text:").grid(row=0, column=1, padx=10)
decrypted_text_output = tk.Text(output_frame, height=6, width=30)
decrypted_text_output.grid(row=1, column=1, padx=10)

root.mainloop()