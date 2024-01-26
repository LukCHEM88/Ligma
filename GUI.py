import tkinter as tk
from tkinter import filedialog
import os
import Ligma

def Fenster():
    '''
    Erstellt ein Fenster mit Willkommen und Buttons zu den anderen Teilen des Programms
    '''
    for element in Hauptfenster.winfo_children():
        element.destroy()
    tk.Label(Hauptfenster,text='Willkommen bei Ligma™\n\nDie schnellste und sicherste Verschlüsselungssoftware').place(x='200',y='75',anchor='center')
    tk.Label(Hauptfenster,text='© 2024 Aperture Laboratories').place(x='200',y='250',anchor='center')
    tk.Button(Hauptfenster,text='Verschlüsseln',command=Verschlüsseln).place(x='300',y='150',anchor='center')
    tk.Button(Hauptfenster,text='Entschlüsseln',command=Entschlüsseln).place(x='100',y='150',anchor='center')
    global FirstRun
    if FirstRun:
        Hauptfenster.geometry('400x300')
        Hauptfenster.resizable('False','False')
        Hauptfenster.title('Ligma')
        FirstRun = False
        Hauptfenster.mainloop()

# Verschlüsseln
def Verschlüsseln():
    '''
    Erstellt das Fenster mit dem Programmteil zum Verschlüsseln
    '''
    for element in Hauptfenster.winfo_children():
        element.destroy()
    tk.Button(Hauptfenster,text='← Zurück',command=Fenster).place(x='25',y='25')
    tk.Button(Hauptfenster,text='Durchsuchen',command=DateiKeyVer).place(x='100',y='150',anchor='center')
    tk.Button(Hauptfenster,text='Durchsuchen',command=DateiMessageVer).place(x='300',y='150',anchor='center')
    tk.Button(Hauptfenster,text='Generieren',command=config).place(x='100',y='185',anchor='center')
    global Verschlüsselbutton
    Verschlüsselbutton = tk.Button(Hauptfenster,text='Verschlüsseln',state='disabled',command=Versch)
    Verschlüsselbutton.place(x='200',y='250',anchor='center')
    global LKeyVer
    LKeyVer = tk.Label(Hauptfenster,text='Kein Schlüssel ausgewählt',anchor='center')
    LKeyVer.place(x='100',y='120',width='180',anchor='center')
    global LFileVer
    LFileVer = tk.Label(Hauptfenster,text='Keine Nachricht ausgewählt',anchor='center')
    LFileVer.place(x='300',y='120',width='180',anchor='center')
def DateiKeyVer():
    '''
    Fragt nach der Schlüsseldatei zum Verschlüsseln und Speichert diese in Key
    '''
    global Key
    Key = filedialog.askopenfilename(filetypes=[("Schlüsseldateien", "*.lig")])
    if Key:
        LKeyVer['text'] = os.path.basename(Key)
    if Datei and Key:
        Verschlüsselbutton['state'] = 'normal'
def DateiMessageVer():
    '''
    Fragt nach der Nachrichtdatei zum Verschlüsseln und Speichert diese in Datei
    '''
    global Datei
    Datei = filedialog.askopenfilename(filetypes=[("Textatei", "*.txt")])
    if Datei:
        LFileVer['text'] = os.path.basename(Datei)
    if Key and Datei:
        Verschlüsselbutton['state'] = 'normal'
def Versch():
    datei = open(Datei,'r',encoding='utf-8')
    message = ''
    for zeile in datei:
        message += zeile
    print(Ligma.Raedern(message,'v',100,Key)) #Zum testen erstmal mit 100
def config():
    pass #Mach ich auch später lol



# Enstschlüsseln
def Entschlüsseln():
    '''
    Erstellt das Fenster mit dem Programmteil zum Entschlüsseln
    '''
    for element in Hauptfenster.winfo_children():
        element.destroy()
    tk.Button(Hauptfenster,text='← Zurück',command=Fenster).place(x='25',y='25')
    tk.Button(Hauptfenster,text='Durchsuchen',command=DateiKeyEnt).place(x='100',y='150',anchor='center')
    tk.Button(Hauptfenster,text='Durchsuchen',command=DateiMessageEnt).place(x='300',y='150',anchor='center')
    global Entschlüsselbutton
    Entschlüsselbutton = tk.Button(Hauptfenster,text='Entschlüsseln',state='disabled',command=Entsch)
    Entschlüsselbutton.place(x='200',y='250',anchor='center')
    global LKeyEnt
    LKeyEnt = tk.Label(Hauptfenster,text='Kein Schlüssel ausgewählt',anchor='center')
    LKeyEnt.place(x='100',y='120',width='180',anchor='center')
    global LFileEnt
    LFileEnt = tk.Label(Hauptfenster,text='Keine Nachricht ausgewählt',anchor='center')
    LFileEnt.place(x='300',y='120',width='180',anchor='center')
def DateiKeyEnt():
    '''
    Fragt nach der Schlüsseldatei zum Entschlüsseln und Speichert diese in Key
    '''
    global Key
    Key = filedialog.askopenfilename(filetypes=[("Schlüsseldateien", "*.lig")])
    if Key:
        LKeyEnt['text'] = os.path.basename(Key)
    if Datei and Key:
        Entschlüsselbutton['state'] = 'normal'
def DateiMessageEnt():
    '''
    Fragt nach der Nachrichtdatei zum Entschlüsseln und Speichert diese in Datei
    '''
    global Datei
    Datei = filedialog.askopenfilename(filetypes=[("Verschlüsselte Datei", "*.ball")])
    if Datei:
        LFileEnt['text'] = os.path.basename(Datei)
    if Key and Datei:
        Entschlüsselbutton['state'] = 'normal'
def Entsch():
    datei = open(Datei,'r',encoding='utf-8')
    ball = ''
    for zeile in datei:
        ball += zeile
    print(Ligma.Raedern(ball,'e',0,Key)) #Auf Speichern gerade kein Bock, mach ich später xd

def Open():
    '''
    Dialog zum öffnen einer Datei
    '''
    return filedialog.askopenfilename()


global Hauptfenster
Hauptfenster = tk.Tk()
global FirstRun
FirstRun = True
Fenster()