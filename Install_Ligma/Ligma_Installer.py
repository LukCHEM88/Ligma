from tkinter import messagebox
import shutil
import os

if os.path.exists('Resources\\Ligma.exe') and os.path.exists('Resources\\Icon_Ligma.ico'):
    if not os.path.exists(os.path.expanduser('~\\Ligma')):
        os.makedirs(os.path.expanduser('~\\Ligma'))
    shutil.copy('Resources\\Icon_Ligma.ico', os.path.expanduser('~\\Ligma'))
    shutil.copy('Resources\\Ligma.exe', os.path.expanduser('~\\Ligma'))
    messagebox.showinfo('Ligma Installer', 'Ligma wurde erfolgreich in Ihrem Benutzerordner installiert')
else:
    messagebox.showerror('Ligma Installer', 'Ein Fehler ist aufgetreten.\nBitte laden Sie den Installer erneut herunter.')
