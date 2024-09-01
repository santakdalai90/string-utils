import tkinter as tk
from tkinter import messagebox
import base64
import codecs

# Function for slash escape
def slash_escape():
    input_string = input_text.get("1.0", tk.END).strip()
    if input_string:
        escaped_string = codecs.escape_encode(input_string.encode('utf-8'))[0].decode('utf-8')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, escaped_string)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid string.")

# Function for slash unescape
def slash_unescape():
    input_string = input_text.get("1.0", tk.END).strip()
    if input_string:
        try:
            unescaped_string = codecs.escape_decode(input_string.encode('utf-8'))[0].decode('utf-8')
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, unescaped_string)
        except Exception as e:
            messagebox.showerror("Decoding Error", f"Error while unescaping: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter a valid string.")

# Function for Base64 encoding
def base64_encode():
    input_string = input_text.get("1.0", tk.END).strip()
    if input_string:
        byte_string = input_string.encode("utf-8")
        base64_encoded = base64.b64encode(byte_string).decode("utf-8")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, base64_encoded)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid string.")

# Function for Base64 decoding
def base64_decode():
    input_string = input_text.get("1.0", tk.END).strip()
    if input_string:
        try:
            base64_decoded = base64.b64decode(input_string).decode("utf-8")
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, base64_decoded)
        except Exception as e:
            messagebox.showerror("Decoding Error", f"Error while decoding Base64: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter a valid Base64 string.")

# Create main window
root = tk.Tk()
root.title("String Utility Program")

# Configure grid weight to make it scalable
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_columnconfigure(1, weight=1)

# Create input label and text box
input_label = tk.Label(root, text="Input:")
input_label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

input_text = tk.Text(root, height=5, width=50)
input_text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Create output label and text box
output_label = tk.Label(root, text="Output:")
output_label.grid(row=1, column=0, padx=10, pady=10, sticky="n")

output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Create buttons for each function
slash_escape_button = tk.Button(root, text="Slash Escape", command=slash_escape)
slash_escape_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

slash_unescape_button = tk.Button(root, text="Slash Unescape", command=slash_unescape)
slash_unescape_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

base64_encode_button = tk.Button(root, text="Base64 Encode", command=base64_encode)
base64_encode_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

base64_decode_button = tk.Button(root, text="Base64 Decode", command=base64_decode)
base64_decode_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

# Start the Tkinter loop
root.mainloop()
