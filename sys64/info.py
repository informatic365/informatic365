import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os
import subprocess
import tkinter as Tk

def run0():
    run()
def run():
    w.destroy()
    w.quit()

r = os.path.exists("i64")
r1 = "i64"

if r:
    None
else:
    messagebox.showerror("Error 404", f"""
Folder "{r1}" not found unable to start the software.
                         """)
    exit()

w = tk.Tk()
w.title("MicroSoftware Info")
width1 = 650
height1 = 650
w.resizable(False, False)
w.config(bg="white")
aw = w.winfo_width()
aww = w.winfo_height()
screen_width1 = w.winfo_screenwidth()
screen_height1 = w.winfo_screenheight()
x1 = int((screen_width1 - width1) / 2)
y1 = int((screen_height1 - height1) / 2)
w.geometry(f"{width1}x{height1}+{x1}+{y1}")
ti = tk.Label(w, text="MicroSoftware Info:", font=("Arial, 35"), bg="white", fg="black")
ti.place(relx=0.5, rely=0.15, anchor='center')
t = tk.Label(w, text="""Version:        "4.55.2v" """, bg="white", fg="red", font=("Roboto, 19"))
t.place(relx=0.125, rely=0.32)
t = tk.Label(w, text="""ID:             "mNcXDMG79k1VRCe6ugtt" """, bg="white", fg="red", font=("Roboto, 19"))
t.place(relx=0.125, rely=0.42)
t = tk.Label(w, text="""License:        "Enterprise" """, bg="white", fg="red", font=("Roboto, 19"))
t.place(relx=0.125, rely=0.52)
t = tk.Label(w, text="""Other Software: "MSRecovery, MSInfo" """, bg="white", fg="red", font=("Roboto, 19"))
t.place(relx=0.125, rely=0.62)
w.protocol("WM_DELETE_WINDOW", run)
w.bind("<Escape>", run0)
w.mainloop()