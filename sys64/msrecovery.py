import argparse
import time
import os
import sys
import datetime
from configparser import ConfigParser
import requests
import shutil
from tkinter import *
import tkinter as tk
from tkinter import messagebox
with open("i64/log.msscript", "a") as f:
        nowt = datetime.datetime.now()
        f.write("""
--------------------------------------------
MicroSoftware opened on: """ + nowt.strftime("%Y-%m-%d %H:%M:%S") + "\n") 

def run():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
              Starting.""", end="\r")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
              Starting..""", end="\r")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
              Starting...""", end="\r")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
              Starting.""", end="\r")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
              Starting..""", end="\r")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
              Starting...""", end="\r")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()
    

def rest():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def recovery():
    mess = messagebox.showwarning("Warning", """
The software is still in experimentation.
                           """, type=messagebox.OKCANCEL)
    if mess == "ok":
        root = tk.Tk()
        root.title("Admin Console | MicroSoftware Recovery")
        root.lift()
        width1 = 850
        height1 = 550
        screen_width1 = root.winfo_screenwidth()
        screen_height1 = root.winfo_screenheight()
        x1 = int((screen_width1 - width1) / 2)
        y1 = int((screen_height1 - height1) / 2)
        root.geometry(f"{width1}x{height1}+{x1}+{y1}")
        root.mainloop()
    else:
        exit()
    

parser = argparse.ArgumentParser(description='Esempio di programma con argparse')
parser.add_argument('-recovery', action='store_true', help='MicroSoftware Recovery')
parser.add_argument('-start', action='store_true', help='Start')
parser.add_argument('-exit', action='store_true', help='Exit to software')
args = parser.parse_args()

if args.start and args.recovery:
    recovery()
elif args.exit:
    exit()
elif args.start:
    if os.path.exists("Config"):
        run()
    else:
        notrun = messagebox.showerror("Config not found", """

Foldare "Config" not found do you want to reinstall MicroSoftware?

                             """, type=messagebox.YESNO)
        if notrun == "yes":
            def autoreset():
                None
            autoreset()
else:
    print("Error")
