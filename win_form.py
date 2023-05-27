#!/usr/bin/env python3
#
import tkinter as tk
from tkinter import ttk

__version__ = "0.0.3" # 2021/01

window = tk.Tk()
window.title("win_form")
window.geometry("350x200")

f24b = "Calibri 24 bold"

title_label = ttk.Label(master=window,text="test", font = f24b)
title_label.pack()

input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text="ENTER")
entry.pack(side="left")
button.pack(side="left")
input_frame.pack()

output_string = tk.StringVar()
output_label = ttk.Label(master=window,text="data", font = f24b)
output_label.pack()

#run
window.mainloop()
