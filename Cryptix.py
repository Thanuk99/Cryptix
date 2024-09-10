import tkinter as tk
from tkinter import messagebox
import random
import string

class CryptixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptix Password Generator")
        self.root.geometry("400x300")

        # Title Label
        self.title_label = tk.Label(root, text="Welcome to Cryptix", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Password Length Input
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        # Special Characters Option
        self.special_chars_var = tk.BooleanVar()
        self.special_chars_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.special_chars_var)
        self.special_chars_check.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Password Display
        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack(pady=5)

        self.password_text = tk.Entry(root, width=50)
        self.password_text.pack(pady=5)

        # Copy to Clipboard Button
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            use_special_chars = self.special_chars_var.get()
            password = self._create_password(length, use_special_chars)
            self.password_text.delete(0, tk.END)
            self.password_text.insert(0, password)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid length.")

    def _create_password(self, length, use_special_chars):
        characters = string.ascii_letters + string.digits
        if use_special_chars:
            characters += string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def copy_to_clipboard(self):
        password = self.password_text.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

def main():
    root = tk.Tk()
    app = CryptixApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

