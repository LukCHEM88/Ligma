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
    tk.Button(Verschlüsselnfester,text='Auswählen',command=False).place(x='50',y='150')
    tk.Button(Verschlüsselnfester,text='Auswählen',command=False).place(x='230',y='150')

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
    tk.Button(Entschlüsselnfenster,text='Auswählen',command=False).place(x='50',y='150')
    tk.Button(Entschlüsselnfenster,text='Auswählen',command=False).place(x='230',y='150')
    SpeichernEnt = tk.Button(Entschlüsselnfenster,text='Entschlüsseln',state='disabled')
    SpeichernEnt.place(x='130',y='220')
    LKeyEnt = tk.Label(Entschlüsselnfenster,text='Keine Datei ausgewählt')
    LKeyEnt.place(x='50',y='130')
    LFileEnt = tk.Label(Entschlüsselnfenster,text='Keine Datei ausgewählt')
    LFileEnt.place(x='230',y='130')



Fenster()