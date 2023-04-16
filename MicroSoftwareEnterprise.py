from tkinter import *
from tkinter import Tk
import tkinter as tk
import tkinter.ttk
from tkinter import messagebox
import configparser
import os
from cryptography.fernet import Fernet
from cryptography.fernet import *
import subprocess
import urllib
import urllib3
from urllib import *
from urllib3 import *
import multiprocessing
import requests
from argparse import *
import argparse
from tkinter.ttk import *
import shutil
import pyrebase
import datetime
import time
import sys
from tkinter import ttk
import json
from jsonschema import validate

def init():
    None
with open("sys64/cript.bin", "rb") as key_file:
    key = key_file.read()

# Crea un oggetto Fernet per la crittografia e decrittografia dei dati
f = Fernet(key)

# Leggi i dati crittografati dal file
with open("sys64/version.script", "rb") as f_in:
    encrypted_data = f_in.read()

# Decrittografa i dati
decrypted_data = f.decrypt(encrypted_data)
vr = "4.55.2v Enterprise"
vrv = decrypted_data.decode()
if vrv == vr:
    None
else:
    messagebox.showerror("Error", """
                            
    version.script or cript.bin not working. Please reset file: "version.script" on application folder "sys64"


""")
    exit()



with open("run.inms", "r") as f:
    fv = f.read().strip()
pv = """[MicroSoftware]
code = 4.55.1 ;
type = default ;
ID = t5t8cyaoihgf374hdwfgdh"""
if os.path.exists("sys64"):
    None
else:
    messagebox.showerror("Error 404", """
Folder "sys64" not found unable to start the software.
                         """)
    exit()
if os.path.exists("sys64/cript.bin"):
    None
else:
    messagebox.showerror("Error", """
                         
version.script or cript.bin not working. Please reset file: "version.script" on application folder "sys64"


""")
    exit()

if fv == pv:
    public = configparser.ConfigParser()
    public.read('sys64/settings.ini')
    data = configparser.ConfigParser()
    def info0(event):
        info()
    def info():
        def run0(event):
            run()
        def run():
            w.destroy()
            root.deiconify()
            width1 = 1050
            height1 = 650
            screen_width1 = root.winfo_screenwidth()
            screen_height1 = root.winfo_screenheight()
            x1 = int((screen_width1 - width1) / 2)
            y1 = int((screen_height1 - height1) / 2)
            root.geometry(f"{width1}x{height1}+{x1}+{y1}")

        r = os.path.exists("sys64/i64")
        r1 = "i64"

        if r:
            None
        else:
            messagebox.showerror("Error 404", f"""
        Folder "{r1}" not found unable to start the software.
                                """)
            exit()
        root.withdraw()
        w = tk.Tk()
        w.attributes("-topmost", True)
        w.attributes('-alpha', 0.8)
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
    def admin0(event):
        admin()
    def admin():
        if public.getboolean('MicroSoftware', 'ActiveAdmin'):
            def admins():
                def adm0(event):
                    adm()
                def adm():
                    def succ():
                        def conf():
                            su.destroy()
                            root.deiconify()
                            width1 = 1050
                            height1 = 650
                            screen_width1 = root.winfo_screenwidth()
                            screen_height1 = root.winfo_screenheight()
                            x1 = int((screen_width1 - width1) / 2)
                            y1 = int((screen_height1 - height1) / 2)
                            root.geometry(f"{width1}x{height1}+{x1}+{y1}")
                        su = tk.Tk()
                        su.update_idletasks()
                        auth.destroy()
                        su.lift()
                        su.title("MicroSoftware Enterprise 4.55.2v | Admin Page ( Login Succefull )")
                        su.config(bg="white")
                        suw = su.winfo_screenwidth()
                        suh = su.winfo_screenheight()
                        sw = 1050
                        sh = 650
                        sx = int((suw - sw) / 2)
                        sy = int((suh - sh) / 2)
                        su.resizable(False, False)
                        su.geometry(f"{sw}x{sh}+{sx}+{sy}")
                        su.protocol("WM_DELETE_WINDOW", conf)
                        def switch_mode():
                            current_mode = settings.get("display", "mode")
                            if current_mode == "light":
                                settings.set("display", "mode", "dark")
                                button.config(text="Light Mode")
                                su.configure(bg="black")
                            else:
                                settings.set("display", "mode", "light")
                                button.config(text="Dark Mode")
                                su.configure(bg="white")
                            # Salva le modifiche sul file settings.ini
                            with open("sys64/settings.ini", "w") as f:
                                settings.write(f)

                        # Carica le impostazioni dal file settings.ini
                        settings = configparser.ConfigParser()
                        settings.read("sys64/settings.ini")

                        # Imposta lo sfondo in base alle impostazioni
                        current_mode = settings.get("display", "mode")
                        if current_mode == "light":
                            su.configure(bg="white")
                            button_text = "Dark Mode"
                        else:
                            su.configure(bg="black")
                            button_text = "Light Mode"

                        # Crea il pulsante
                        button = tk.Button(su, text=button_text, command=switch_mode)
                        button.pack(pady=10)
                        su.mainloop()
                    def bb():
                        ab.config(text="")
                    if pas.get() == "Admin365":
                        ad.place_forget()
                        pad.place_forget()
                        pas.place_forget()
                        pasb.place_forget()
                        ab.place_forget()
                        auth.update_idletasks()
                        aas = tk.Label(auth, text="Please Waiting ...", font="Arial, 35", bg="#0D8C65", fg="white")
                        aas.place(relx=0.5, rely=0.45, anchor='center')
                        auth.after(1750, succ)
                        
                    else:
                        messagebox.showerror("Password", "Password not correct. Try again.")
                        ab.config(text="Password not correct. Try Again")
                        auth.after(2000, bb)
                def ex(event):
                    conf()
                def conf():
                    auth.destroy()
                    root.deiconify()
                    root.lift()
                    width1 = 1050
                    height1 = 650
                    screen_width1 = root.winfo_screenwidth()
                    screen_height1 = root.winfo_screenheight()
                    x1 = int((screen_width1 - width1) / 2)
                    y1 = int((screen_height1 - height1) / 2)
                    root.geometry(f"{width1}x{height1}+{x1}+{y1}")
                auth = tk.Tk()
                auth.config(bg="#0D8C65")
                root.withdraw()
                auth.update_idletasks()
                w0 = 950
                w01 = 575
                scrw = auth.winfo_screenwidth()
                scrh = auth.winfo_screenheight()
                ax = int((scrw - w0) / 2)
                ay = int((scrh - w01) / 2)
                auth.geometry(f"{w0}x{w01}+{ax}+{ay}")
                auth.resizable(False, False)
                auth.lift()
                infw = auth.winfo_width()
                infh = auth.winfo_height()
                
                ad = tk.Label(auth, text="Admin Access Page", font=("Roboto, 30"), bg="#0D8C65", fg="white")
                ad.place(relx=0.5, rely=0.23, anchor='center')
                pad = tk.Label(auth, text="Password:", font=("Arial, 14"), bg="#0D8C65", fg="black")
                pad.place(relx=0.5, rely=0.355, anchor='center')
                pas = ttk.Entry(auth, width=40, background="white", foreground="black", font=("Roboto, 13"), show="*")
                pas.place(relx=0.5, rely=0.4, anchor='center')
                pasb = tk.Button(auth, text="       Login      ", font=("Roboto, 13"), bg="#1F8F9C", fg="red", command=adm)
                pasb.place(relx=0.5, rely=0.5, anchor='center')
                ab = tk.Label(auth, text="", bg="#0D8C65", fg="red")
                ab.place(relx=0.5, rely=0.445, anchor='center')
                pas.bind("<Return>", adm0)
                auth.title("MicroSoftware Enterprise 4.55.2v | Admin Access Page")
                auth.protocol("WM_DELETE_WINDOW", conf)
                auth.bind("<Escape>", ex)
                auth.mainloop()
            admins()
        else:
            messagebox.showinfo("Error", "Page for admin and status have been disabled by default settings!")
            COMMAND=root
    def sett0(event):
        sett()
    def sett():
        def conf():
            se.destroy()
            root.deiconify()
            root.lift()
            width1 = 1050
            height1 = 650
            screen_width1 = root.winfo_screenwidth()
            screen_height1 = root.winfo_screenheight()
            x1 = int((screen_width1 - width1) / 2)
            y1 = int((screen_height1 - height1) / 2)
            root.geometry(f"{width1}x{height1}+{x1}+{y1}")
        se = tk.Tk()
        se.config(bg="#00FF9D")
        root.withdraw()
        se.title("MicroSoftware Enterprise 4.55.2v | Settings")
        width0 = 1050
        height0 = 650
        se.resizable(False, False)
        screen_width0 = se.winfo_screenwidth()
        screen_height0 = se.winfo_screenheight()
        x0 = int((screen_width0 - width0) / 2)
        y0 = int((screen_height0 - height0) / 2)
        se.geometry(f"{width0}x{height0}+{x0}+{y0}")
        se.protocol("WM_DELETE_WINDOW", conf)
        se.mainloop()
    def oadvrest():
        os.system("shutdown -r -o -t 0")

    def orest():
        os.system("shutdown -r -t 0")

    def oshut():
        if public.getboolean('MicroSoftware', 'ShutdownGraphic'):
            os.system("cmd /c slidetoshutdown")
        else:
            os.system("shutdown -s -t 0")
    def pct0(event):
        pct()
    def pct():
        def conf0(event):
            conf
        def conf():
            pc.destroy()
            root.deiconify()
            root.lift()
            width1 = 1050
            height1 = 650
            screen_width1 = root.winfo_screenwidth()
            screen_height1 = root.winfo_screenheight()
            x1 = int((screen_width1 - width1) / 2)
            y1 = int((screen_height1 - height1) / 2)
            root.geometry(f"{width1}x{height1}+{x1}+{y1}")
        pc = tk.Tk()
        root.withdraw()
        pc.lift()
        pc.title("MicroSoftware Enterprise 4.55.2v | PCTools")
        pc.config(bg="white")
        sw1 = pc.winfo_screenwidth()
        sh1 = pc.winfo_screenheight()
        s1 = 1050
        s11 = 650
        x02 = int((sw1 - s1) / 2)
        x12 = int((sh1 - s11) / 2)
        pc.geometry(f"{s1}x{s11}+{x02}+{x12}")
        pc.update_idletasks()
        pc.protocol("WM_DELETE_WINDOW", conf)
        pc.bind("<Escape>", conf0)
        pc.mainloop()
    def advt0(event):
        advt()
    def advt():
        def ex(event):
            conf()
        def conf():
            a.destroy()
            root.deiconify()
            root.lift()
            width1 = 1050
            height1 = 650
            screen_width1 = root.winfo_screenwidth()
            screen_height1 = root.winfo_screenheight()
            x1 = int((screen_width1 - width1) / 2)
            y1 = int((screen_height1 - height1) / 2)
            root.geometry(f"{width1}x{height1}+{x1}+{y1}")
        a = tk.Tk()
        root.withdraw()
        st0 = ttk.Style()
        st0.theme_use("clam")
        st0.configure("La.TLabel", foreground="white", background="black", font="Roboto, 20")
        a.lift()
        a.title("MicroSoftware Enterprise 4.55.2v | Advanced Tools")
        sw = a.winfo_screenwidth()
        sh = a.winfo_screenheight()
        s = 1050
        s1 = 650
        x01 = int((sw - s) / 2)
        x11 = int((sh - s1) / 2)
        a.geometry(f"{s}x{s1}+{x01}+{x11}")
        a.config(bg="#009BFF")
        a.protocol("WM_DELETE_WINDOW", conf)
        note = ttk.Notebook(a)
        fr0 = tk.Frame(note)
        fr1 = tk.Frame(note)
        fr2 = tk.Frame(note)
        fr0.configure(background="#009BFF")
        fr1.configure(background="#009BFF")
        fr2.configure(background="black")
        note.add(fr0, text="Main Page")
        note.add(fr1, text="More Tools")
        note.add(fr2, text="MicroBot")
        mtext = tk.Label(fr2, text="Start Chating with MicroBot", font=("Helvetica, 20"), bg="black", fg="#F77400")
        mtext.place(relx=0.5, rely=0.355, anchor='center')
        mb = tk.Button(fr2, text="""Start with "MicroBot" """, font=("Roboto, 15"), bg="white", fg="#24A681", width=100)
        note.pack(expand=True, fill='both')
        mb.place(relx=0.5, rely=0.445, anchor='center')
        la = tk.Label(fr0, text="Advanced tools", bg="#009BFF", fg="white", font=("Roboto, 25"))
        la.place(relx=0.5, rely=0.125, anchor='center')
        a.bind("<Escape>", ex)
        a.mainloop()
    splash = configparser.ConfigParser()
    splash.read('sys64/settings.ini')
    if splash.getboolean('MicroSoftware', 'SplashScreen'):
        root = tk.Tk()
        root.attributes("-alpha", 0.905)
        gg = root.winfo_width()
        gh = root.winfo_height()
        root.title("MicroSoftware Enterprise 4.55.2v")
        root.overrideredirect(True)
        root.config(bg="#00C8FF")
        width = 550
        height = 350
        root.resizable(False,False)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        root.geometry(f"{width}x{height}+{x}+{y}")
        copy = tk.Label(root, text="Copyright 2022-2023 @informatic365 MicroSoftware", bg="#00C8FF", fg="black")
        copy.place(relx=0.006, rely=0.929)
        welc = tk.StringVar()
        welc.set("")
        welcs = tk.Label(root, textvariable=welc, font="Arial, 25", bg="#00C8FF", fg="white")
        welcs.place(relx=0.5, rely=0.425, anchor='center')
        def aa():
            os.system('cls' if os.name=='nt' else 'clear')
            root.destroy()
        def start_writing():
            phrase = """
Welcome To MicroSoftware

Enterprise 4.55.2v

"""
            for letter in phrase:
                welc.set(welc.get() + letter)
                root.update()
                time.sleep(0.02)
            time.sleep(0.5)
            root.destroy()
        root.bind("<F1>", lambda event: aa())
        root.after(0, start_writing)
        root.mainloop()
    def local():
        with open("sys64/cript.bin", "rb") as key_file:
            key = key_file.read()

        # Crea un oggetto Fernet per la crittografia e decrittografia dei dati
        f = Fernet(key)

        # Leggi i dati crittografati dal file
        with open("sys64/version.script", "rb") as f_in:
            encrypted_data = f_in.read()

        # Decrittografa i dati
        decrypted_data = f.decrypt(encrypted_data)
        vr = "4.55.2v Enterprise"
        vrv = decrypted_data.decode()
        if vrv == vr:
            if public.get('MSVersion', 'version') == "4.55.2":
                if public.get('MSVersion', 'License') == "Enterprise":
                    os.system('start https://informatica365.tk/projects/microsoftware/')
                else:
                    messagebox.showerror("License error", "The license do not match. Please reset the program")
            else:
                messagebox.showerror("Version error", "The versions do not match. Please reset the program")
        else:
            messagebox.showerror("Error", """
                                    
            version.script or cript.bin not working. Please reset file: "version.script" on application folder "sys64"


        """)
            exit()
    def restartsoftware():
        python = sys.executable
        subprocess.Popen([python, __file__])
        root.destroy()
    def verclose0(event):
        verclose()
    def verclose():
        if public.getboolean('MicroSoftware', 'CloseMessage'):
            if messagebox.askyesno("Confirm", "Are you sure you close?"):
                os.system('cls' if os.name=='nt' else 'clear')
                root.destroy()
                sys.exit()
        else:
            os.system('cls' if os.name=='nt' else 'clear')
            root.destroy()
            sys.exit()
    root = tk.Tk()
    os.system('cls' if os.name=='nt' else 'clear')
    root.config()
    root.update_idletasks()
    os.system('cls' if os.name=='nt' else 'clear')
    root.attributes("-topmost", False)
    root.attributes("-alpha", 0.9)
    root.lift()
    width1 = 1050
    height1 = 650
    screen_width1 = root.winfo_screenwidth()
    screen_height1 = root.winfo_screenheight()
    x1 = int((screen_width1 - width1) / 2)
    y1 = int((screen_height1 - height1) / 2)
    root.geometry(f"{width1}x{height1}+{x1}+{y1}")
    root.iconbitmap("sys64/img/icon.ico")
    title = vrv
    root.title('MicroSoftware '+ title)
    if public.getboolean('MicroSoftware', 'EnableLog'):
        with open("sys64/msdata.txt", "a") as f:
            nowt = datetime.datetime.now()
            f.write("""
--------------------------------------------
MicroSoftware opened on: """ + nowt.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    else:
        None
    root.config(bg="#37889E")
    dat = ttk.Style()
    dat.theme_use("clam")
    dat.configure("Datefr.TLabelframe", foregound="#37889E", background="white")
    datefr = tk.Frame(root, width=400, height=235, borderwidth=1, bg="white")
    datefr.place(relx=0.9, rely=0.885, anchor='center')
    datal = tk.Label(datefr, text="", font=("Roboto, 20"), bg="white", fg="#09CEFF")
    datal.pack(anchor='center')
    datal1 = tk.Label(datefr, text="", font=("Roboto, 20"), bg="white", fg="#09CEFF")
    datal1.pack(anchor='center')
    def update_date_time():
        os.system('cls' if os.name=='nt' else 'clear')
        now = datetime.datetime.now()
        datal.config(text=now.strftime("%H:%M:%S"))
        datal1.config(text=now.strftime("%m/%d/%Y"))
        datal.after(1000, update_date_time)
    update_date_time()
    root.resizable(False, False)
    welc1 = tk.StringVar()
    welc1.set("")
    welcs1 = tk.Label(root, textvariable=welc1, font="Arial, 30", bg="#37889E", fg="white")
    welcs1.place(relx=0.5, rely=0.205, anchor='center')
    def start_writing1():
        phrase1 = "MicroSoftware Enterprise 4.55.2v"
        for letter1 in phrase1:
            welc1.set(welc1.get() + letter1)
            root.update()
            time.sleep(0.0195)
    root.after(0, start_writing1)
    root.update_idletasks()
    root.lift()
    style1 = ttk.Style()
    style = ttk.Style()
    style2 = ttk.Style()
    style3 = ttk.Style()
    style3.theme_use("clam")
    style2.theme_use("clam")
    style1.theme_use("clam")
    style.theme_use("clam")
    style3.configure("Alls.TButton", foreground="#AAB7B8", background="#ECF0F1", borderwidth=0, padding=7, font=("Roboto", 12, "bold"), anchor="center")
    style2.configure("Three.TButton", foreground="#D8FF00", background="#FF9A18", borderwidth=0, padding=5, font=("Helvetica", 12, "bold"), anchor="center")
    style.configure("Shut.TButton", foreground="white", background="#66DEFF", borderwidth=0, padding=5, font=("Helvetica", 12, "bold"), anchor="center")
    style1.configure("Sec.TButton", foreground="black", background="#1CA57A", borderwidth=0, padding=5, font=("Helvetica", 12, "bold"), anchor="center")
    shut = ttk.Button(root, text="Turn Off", style="Shut.TButton", command=oshut)
    shut.place(relx=0.275, rely=0.41, anchor='center')
    shut = ttk.Button(root, text="Restart", style="Shut.TButton", command=orest)
    shut.place(relx=0.475, rely=0.41, anchor='center')
    shut = ttk.Button(root, text="Advanced Restart", style="Shut.TButton", command=oadvrest)
    shut.place(relx=0.685, rely=0.41, anchor='center')
    sec = ttk.Button(root, text="PC Tools", style="Sec.TButton", command=pct)
    sec.place(relx=0.375, rely=0.57, anchor='center')
    sec1 = ttk.Button(root, text="Advanced Tools", style="Sec.TButton", command=advt)
    sec1.place(relx=0.585, rely=0.57, anchor='center')
    three = ttk.Button(root, text="Support", style="Three.TButton", command=local)
    three.place(relx=0.175, rely=0.71, anchor='center')
    alls = ttk.Button(root, text="Restart Software", command=restartsoftware, style="Alls.TButton")
    alls.place(relx=0.1, rely=0.935, anchor='center')

    copy = tk.Label(root, text="Copyright 2022-2023 @informatic365 MicroSoftware", bg="#37889E", fg="black")
    copy.place(relx=0, rely=0.965)

    root.bind("<Control-a>", admin0)
    root.bind("<Control-A>", admin0)
    root.bind("<Control-q>", advt0)
    root.bind("<Control-Q>", advt0)
    root.bind("<Control-p>", lambda event: pct())
    root.bind("<Control-P>", lambda event: pct())
    root.bind("<Control-i>", info0)
    root.bind("<Control-I>", info0)
    root.bind("<F5>", lambda event: local())
    root.bind("<Escape>", verclose0)
    if public.getboolean('MicroSoftware', 'ActiveAdvt'):
        sec1.configure(state='active')
        sec1.update_idletasks()
    else:
        sec1.configure(state='disabled')
        sec1.update_idletasks()

    bar = tk.Menu(root)
    root.config(menu=bar)
    bars = tk.Menu(bar, tearoff=0)
    bars.add_command(label="Info", command=info)
    bars.add_command(label="Update", command=local)
    bars.add_separator()
    bars.add_command(label="Turn Off ( PC )", command=oshut)
    bars.add_command(label="Restart ( PC )", command=orest)
    bars.add_command(label="Advanced Restart ( PC )", command=oadvrest)
    bars.add_separator()
    bars.add_command(label="Settings", command=sett)
    bars.add_command(label="Restart Software", command=restartsoftware)
    bars.add_command(label="Exit", command=lambda: exit())
    bar.add_cascade(label="Software", menu=bars)
    #
    bars1 = tk.Menu(bar, tearoff=0)
    bars1.add_command(label="Advanced Tools", command=advt)
    bars1.add_command(label="PC Tools", command=pct)
    bars1.add_separator()
    bars1.add_command(label="Admin Access", command=admin)
    bar.add_cascade(label="Commands", menu=bars1)
    #
    bars2 = tk.Menu(bar, tearoff=0)
    bars2.add_command(label="Help")
    bars2.add_command(label="Support")
    bar.add_cascade(label="Help", menu=bars2)
    root.protocol("WM_DELETE_WINDOW", verclose)
    root.mainloop()
else:
    messagebox.showerror("Error run.inms not working", """
                    Impossible
    
File run.inps not found or modified, unable to start the software.
                    
                    
                         """)
    