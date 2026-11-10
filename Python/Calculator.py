import tkinter as tk
from tkinter import messagebox

# Fungsi operasi
def hitung(operasi):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if operasi == "+":
            hasil = a + b
        elif operasi == "-":
            hasil = a - b
        elif operasi == "*":
            hasil = a * b
        elif operasi == "/":
            if b == 0:
                messagebox.showerror("Error", "Tidak bisa dibagi nol!")
                return
            hasil = a / b

        label_hasil.config(text=f"Hasil: {hasil}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Window utama
root = tk.Tk()
root.title("Kalkulator 2 Input")
root.geometry("300x250")

# Input
tk.Label(root, text="Angka 1").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Angka 2").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Tombol operasi
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="+", width=5, command=lambda: hitung("+")).grid(row=0, column=0)
tk.Button(frame, text="-", width=5, command=lambda: hitung("-")).grid(row=0, column=1)
tk.Button(frame, text="×", width=5, command=lambda: hitung("*")).grid(row=1, column=0)
tk.Button(frame, text="÷", width=5, command=lambda: hitung("/")).grid(row=1, column=1)

# Hasil
label_hasil = tk.Label(root, text="Hasil: ")
label_hasil.pack(pady=10)

root.mainloop()
