import tkinter as tk
from tkinter import ttk,filedialog

def Fenster():
    '''
    Erstellt ein Fenster mit Willkommen und Buttons zu den anderen Teilen des Programms
    '''
    global Hauptfenster
    try:
       Verschlüsselnfester.destroy()
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
    global Verschlüsselnfester
    Verschlüsselnfester = tk.Tk()
    Verschlüsselnfester.geometry('400x300')
    Verschlüsselnfester.resizable('False','False')
    Verschlüsselnfester.title('Ligma')
    tk.Button(Verschlüsselnfester,text='← Zurück',command=Fenster).place(x='25',y='25')
    tk.Button(Verschlüsselnfester,text='Schlüssel',command=False).place(x='50',y='150')
    tk.Button(Verschlüsselnfester,text='Nachricht',command=False).place(x='230',y='150')

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
    Entschlüsselbutton = tk.Button(Entschlüsselnfenster,text='Entschlüsseln',state='disabled')
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
    Key = Open()
    LKeyEnt['text'] = Key
    if Datei:
        Entschlüsselbutton['state'] = 'active'
def DateiMessageEnt():
    '''
    Fragt nach der Nachrichtdatei zum Entschlüsseln und Speichert diese in Datei
    '''
    global Datei
    Datei = Open()
    LFileEnt['text'] = Datei
    if Key:
        Entschlüsselbutton['state'] = 'active'

def Open():
    '''
    Dialog zum öffnen einer Datei
    '''
    return filedialog.askopenfilename()
Fenster()