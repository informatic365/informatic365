import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Cartella da monitorare
path_to_watch = r'C:\Users\HIPOS\Desktop\MicroSoftware 4.55.2\New'

# Cartella di destinazione sulla pendrive
path_to_pendrive = r'F:/'

# Handler per gestire gli eventi di modifica della cartella
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        # Copia la cartella sulla pendrive
        shutil.copytree(path_to_watch, os.path.join(path_to_pendrive, os.path.basename(path_to_watch)), dirs_exist_ok=True)
        print(f'Cartella {path_to_watch} copiata su {path_to_pendrive} alle ore {time.strftime("%H:%M:%S")}')

# Crea l'observer e avvia il monitoraggio
observer = Observer()
observer.schedule(Handler(), path=path_to_watch, recursive=True)
observer.start()

# Stampa un messaggio di avvio
print(f'Monitoraggio della cartella {path_to_watch} avviato...')

try:
    while True:
        time.sleep(2.5)
except KeyboardInterrupt:
    # Ferma l'observer se l'utente preme CTRL+C
    observer.stop()

# Attende che l'observer termini
observer.join()

# Stampa un messaggio di uscita
print(f'Monitoraggio della cartella {path_to_watch} terminato.')
time.sleep(2)