import tkinter as tk
from tkinter import ttk

def loop():
    angle = input("angle")
    canvas.itemconfig("arc", start=angle)
    root.after(100, loop)


root = tk.Tk()
root.title("Artifical_Horizon")
#root.geometry('1200x750')
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack(fill="both", expand=True)
arc = canvas.create_arc(-100, -100, 400, 400, start=0, extent=180, fill="orange3")

loop()

root.mainloop()
