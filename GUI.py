import tkinter as tk
from tkinter import filedialog

def Fenster():
    '''
    Erstellt ein Fenster mit Willkommen und Buttons zu den anderen Teilen des Programms
    '''
    global Hauptfenster
    try:
       Verschlüsselnfenster.destroy()
    except NameError:
        pass
    except tk.TclError:
        pass
    try:
       Entschlüsselnfenster.destroy()
    except NameError:
        pass
    except tk.TclError:
        pass
    Hauptfenster = tk.Tk()
    Hauptfenster.geometry('400x300')
    Hauptfenster.resizable('False','False')
    Hauptfenster.title('Ligma')
    tk.Label(Hauptfenster,text='Willkommen').place(x='50',y='50')
    tk.Button(Hauptfenster,text='Verschlüsseln',command=Verschlüsseln).place(x='230',y='150')
    tk.Button(Hauptfenster,text='Entschlüsseln',command=Entschlüsseln).place(x='50',y='150')
    Hauptfenster.mainloop()

# Verschlüsseln
def Verschlüsseln():
    '''
    Erstellt das Fenster mit dem Programmteil zum Verschlüsseln
    '''
    Hauptfenster.destroy()
    global Verschlüsselnfenster
    Verschlüsselnfenster = tk.Tk()
    Verschlüsselnfenster.geometry('400x300')
    Verschlüsselnfenster.resizable('False','False')
    Verschlüsselnfenster.title('Ligma')
    tk.Button(Verschlüsselnfenster,text='← Zurück',command=Fenster).place(x='25',y='25')
    tk.Button(Verschlüsselnfenster,text='Schlüssel',command=DateiKeyVer).place(x='50',y='150')
    tk.Button(Verschlüsselnfenster,text='Nachricht',command=DateiMessageVer).place(x='230',y='150')
    global Verschlüsselbutton
    Verschlüsselbutton = tk.Button(Verschlüsselnfenster,text='Verschlüsseln',state='disabled')
    Verschlüsselbutton.place(x='130',y='220')
    global LKeyVer
    LKeyVer = tk.Label(Verschlüsselnfenster,text='Keine Datei ausgewählt',anchor='e')
    LKeyVer.place(x='50',y='130',width='150')
    global LFileVer
    LFileVer = tk.Label(Verschlüsselnfenster,text='Keine Datei ausgewählt',anchor='e')
    LFileVer.place(x='230',y='130',width='150')
def DateiKeyVer():
    '''
    Fragt nach der Schlüsseldatei zum Verschlüsseln und Speichert diese in Key
    '''
    global Key
    Key = filedialog.askopenfilename(filetypes=[("Schlüsseldateien", "*.lig")])
    if Key:
        LKeyVer['text'] = Key
    if Datei and Key:
        Verschlüsselbutton['state'] = 'normal'
def DateiMessageVer():
    '''
    Fragt nach der Nachrichtdatei zum Verschlüsseln und Speichert diese in Datei
    '''
    global Datei
    Datei = filedialog.askopenfilename(filetypes=[("Textatei", "*.txt")])
    if Datei:
        LFileVer['text'] = Datei
    if Key and Datei:
        Verschlüsselbutton['state'] = 'normal'



# Enstschlüsseln
def Entschlüsseln():
    '''
    Erstellt das Fenster mit dem Programmteil zum Entschlüsseln
    '''
    Hauptfenster.destroy()
    global Entschlüsselnfenster
    Entschlüsselnfenster = tk.Tk()
    Entschlüsselnfenster.geometry('400x300')
    Entschlüsselnfenster.resizable('False','False')
    Entschlüsselnfenster.title('Ligma')
    tk.Button(Entschlüsselnfenster,text='← Zurück',command=Fenster).place(x='25',y='25')
    tk.Button(Entschlüsselnfenster,text='Schlüssel',command=DateiKeyEnt).place(x='50',y='150')
    tk.Button(Entschlüsselnfenster,text='Datei',command=DateiMessageEnt).place(x='230',y='150')
    global Entschlüsselbutton
    Entschlüsselbutton = tk.Button(Entschlüsselnfenster,text='Entschlüsseln',state='disabled',command=Entsch)
    Entschlüsselbutton.place(x='130',y='220')
    global LKeyEnt
    LKeyEnt = tk.Label(Entschlüsselnfenster,text='Keine Datei ausgewählt',anchor='e')
    LKeyEnt.place(x='50',y='130',width='150')
    global LFileEnt
    LFileEnt = tk.Label(Entschlüsselnfenster,text='Keine Datei ausgewählt',anchor='e')
    LFileEnt.place(x='230',y='130',width='150')
def DateiKeyEnt():
    '''
    Fragt nach der Schlüsseldatei zum Entschlüsseln und Speichert diese in Key
    '''
    global Key
    Key = filedialog.askopenfilename(filetypes=[("Schlüsseldateien", "*.lig")])
    if Key:
        LKeyEnt['text'] = Key
    if Datei and Key:
        Entschlüsselbutton['state'] = 'normal'
def DateiMessageEnt():
    '''
    Fragt nach der Nachrichtdatei zum Entschlüsseln und Speichert diese in Datei
    '''
    global Datei
    Datei = filedialog.askopenfilename(filetypes=[("Verschlüsselte Datei", "*.ball")])
    if Datei:
        LFileEnt['text'] = Datei
    if Key and Datei:
        Entschlüsselbutton['state'] = 'normal'
def Entsch():
    pass

def Open():
    '''
    Dialog zum öffnen einer Datei
    '''
    return filedialog.askopenfilename()
Fenster()