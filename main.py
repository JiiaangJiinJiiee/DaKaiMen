import tkinter as tk
from tkinter import ttk
import pandas as pd

root = tk.Tk()
root.title("DaKaiMen - 大开门")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="====施工中====").grid(column=1, row=0)

ttk.Button(mainframe, width=5, text="辞职！", command=exit).grid(column=1, row=2)

root.mainloop()
