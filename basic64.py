import tkinter as tk
import urllib.request
import os
import subprocess

# URL del file version.txt
version_url = 'https://example.com/version.txt'

# URL del file di aggiornamento
update_url = 'https://example.com/update.exe'

def check_for_update():
    # Scarica il contenuto del file version.txt
    with urllib.request.urlopen(version_url) as response:
        version_data = response.read().decode('utf-8')

    # Leggi la versione corrente dal file locale
    with open('version.txt', 'r') as f:
        current_version = f.read()

    # Confronta la versione corrente con quella più recente
    if current_version != version_data:
        # Se la versione più recente è disponibile, scarica l'aggiornamento e installalo
        update_message = f'È disponibile una nuova versione ({version_data})! Vuoi scaricarla e installarla ora?'
        if tk.messagebox.askyesno('Aggiornamento disponibile', update_message):
            # Scarica l'aggiornamento dal server
            with urllib.request.urlopen(update_url) as response:
                update_data = response.read()

            # Salva l'aggiornamento sul disco
            with open('update.exe', 'wb') as f:
                f.write(update_data)

            # Esegui l'aggiornamento
            subprocess.Popen('update.exe')
            # Chiudi l'applicazione corrente
            os._exit(0)
    else:
        # Se la versione corrente è la più recente, mostra un messaggio di conferma
        tk.messagebox.showinfo('Aggiornamento non necessario', 'La versione corrente è già aggiornata!')

# Esempio di utilizzo
root = tk.Tk()
root.geometry('200x200')

button = tk.Button(root, text='Verifica aggiornamenti', command=check_for_update)
button.pack()

root.mainloop()
