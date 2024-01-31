# Import benötigter Module
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os
import Ligma
import platform

# Funktionen
def Fenster():
    '''
    Erstellt ein Fenster mit Willkommen und Buttons zu den anderen Teilen des Programms
    '''
    for element in Hauptfenster.winfo_children():
        element.destroy()
    Hauptfenster.title('Ligma')
    if platform.system() == 'Windows':
        if os.path.exists('Icon_Ligma.ico'):
            Hauptfenster.iconbitmap('Icon_Ligma.ico')
    tk.Label(Hauptfenster,text='Willkommen bei Ligma™\n\nDie schnellste und sicherste Verschlüsselungssoftware').place(x='200',y='75',anchor='center')
    tk.Label(Hauptfenster,text='© 2024 Aperture Laboratories').place(x='200',y='250',anchor='center')
    tk.Button(Hauptfenster,text='Verschlüsseln',command=Verschlüsseln).place(x='300',y='150',anchor='center')
    tk.Button(Hauptfenster,text='Entschlüsseln',command=Entschlüsseln).place(x='100',y='150',anchor='center')
    global FirstRun
    if FirstRun:
        Hauptfenster.geometry('400x300')
        Hauptfenster.resizable('False','False')
        FirstRun = False
        Hauptfenster.mainloop()

# Funktionen, die mit dem Verschlüsseln zu tun haben
def Verschlüsseln():
    '''
    Erstellt das Fenster mit dem Programmteil zum Verschlüsseln
    '''
    for element in Hauptfenster.winfo_children():
        element.destroy()
    Hauptfenster.title('Ligma - Verschlüsseln')
    tk.Button(Hauptfenster,text='← Zurück',command=Fenster).place(x='25',y='25')
    tk.Button(Hauptfenster,text='Speichern',command=DateiKeyVer).place(x='100',y='150',anchor='center')
    tk.Button(Hauptfenster,text='Durchsuchen',command=DateiMessageVer).place(x='300',y='150',anchor='center')
    global Verschlüsselbutton
    Verschlüsselbutton = tk.Button(Hauptfenster,text='Verschlüsseln',state='disabled',command=Versch)
    Verschlüsselbutton.place(x='200',y='250',anchor='center')
    global LKeyVer
    LKeyVer = tk.Label(Hauptfenster,text='Kein Schlüssel gespeichert',anchor='center')
    LKeyVer.place(x='100',y='120',width='180',anchor='center')
    global LFileVer
    LFileVer = tk.Label(Hauptfenster,text='Keine Nachricht ausgewählt',anchor='center')
    LFileVer.place(x='300',y='120',width='180',anchor='center')
def DateiKeyVer():
    '''
    Fragt nach Speicherort der Schlüsseldatei
    '''
    global Keypfad
    Keytmp = filedialog.asksaveasfilename(defaultextension='.lig',filetypes=[("Schlüsseldateien", "*.lig")])
    if Keytmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
        Keypfad = Keytmp
        LKeyVer['text'] = os.path.basename(Keypfad) # Zeigt ausgewählte Datei an
    if DateiVerpfad and Keypfad:
        Verschlüsselbutton['state'] = 'normal' # Aktiviert Versch, wenn beide Dateien ausgewählt wurden
def DateiMessageVer():
    '''
    Fragt nach der Nachrichtdatei zum Verschlüsseln und Speichert diese in Dateipfad
    '''
    global DateiVerpfad
    Dateitmp = filedialog.askopenfilename(filetypes=[("Textdatei", "*.txt")])
    if Dateitmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
        DateiVerpfad = Dateitmp
        LFileVer['text'] = os.path.basename(DateiVerpfad) # Zeigt ausgewählte Datei an
    if Keypfad and DateiVerpfad:
        Verschlüsselbutton['state'] = 'normal' # Aktiviert Versch, wenn beide Dateien ausgewählt wurden
def Versch():
    '''
    Wird aktiv, wenn eine Schlüsseldatei und eine Nachrichtdatei ausgewählt wurde
    Verschlüsselt die Datei
    '''
    datei = open(DateiVerpfad,'r',encoding='utf-8')
    message = ''
    for zeile in datei:
        message += zeile
    datei.close()
    Anz = simpledialog.askinteger('Verschlüsseln','Stärke der Verschlüsselung eingeben: ',initialvalue=50,minvalue=1)
    if Anz: # Failsave, wenn der Nutzer bei der Integereingabe auf Cancel drückt
        Text = Ligma.Raedern(message,'v',Anz,Keypfad)
        if Text == '[Error: Keydatei wurde nicht gefunden]':
            messagebox.showerror('Verschlüsseln', 'Error: Keydatei wurde nicht gefunden')
        elif Text == '[Error: benötigte(r) Parameter nicht vorhanden]':
            messagebox.showerror('Verschlüsseln', 'Error: benötigte(r) Parameter nicht vorhanden')
        else:
            Savepfad = filedialog.asksaveasfilename(defaultextension='.ball',filetypes=[('Verschlüsselte Dateien', '*.ball')])
            if Savepfad:
                datei = open(Savepfad,'w',encoding='utf-8')
                datei.write(Text)
                datei.close()

# Funktionen, die mit dem Enstschlüsseln zu tun haben
def Entschlüsseln():
    '''
    Erstellt das Fenster mit dem Programmteil zum Entschlüsseln
    '''
    for element in Hauptfenster.winfo_children():
        element.destroy()
    Hauptfenster.title('Ligma - Entschlüsseln')
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
    Fragt nach einer Schlüsseldatei zum Entschlüsseln und Speichert diese in Keypfad
    '''
    global Keypfad
    Keytmp = filedialog.askopenfilename(filetypes=[("Schlüsseldateien", "*.lig")])
    if Keytmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
        Keypfad = Keytmp
        LKeyEnt['text'] = os.path.basename(Keypfad) # Zeigt ausgewählte Datei an
    if DateiEntpfad and Keypfad: # Aktiviert Entsch, wenn beide Dateien ausgewählt wurden
        Entschlüsselbutton['state'] = 'normal'
def DateiMessageEnt():
    '''
    Fragt nach einer Verschlüsselten Datei und Speichert deren Pfad in Dateipfad
    '''
    global DateiEntpfad
    Dateitmp = filedialog.askopenfilename(filetypes=[("Verschlüsselte Datei", "*.ball")])
    if Dateitmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
        DateiEntpfad = Dateitmp
        LFileEnt['text'] = os.path.basename(DateiEntpfad) # Zeigt ausgewählte Datei an
    if Keypfad and DateiEntpfad: # Aktiviert Entsch, wenn beide Dateien ausgewählt wurden
        Entschlüsselbutton['state'] = 'normal'
def Entsch():
    '''
    Wird aktiv, wenn eine Schlüsseldatei und eine Verschlüsselte Datei ausgewählt wurde
    Entschlüsselt die Datei mit dem Schlüssel
    '''
    datei = open(DateiEntpfad,'r',encoding='utf-8')
    ball = ''
    for zeile in datei:
        ball += zeile
    Text = Ligma.Raedern(ball,'e',0,Keypfad)
    if Text == '[Error: Keydatei wurde nicht gefunden]':
        messagebox.showerror('Entschlüsseln', 'Error: Keydatei wurde nicht gefunden')
    elif Text == '[Error: (*.lig)-Datei und (*.ball)-Datei nicht Kompatibel]':
        messagebox.showerror('Entschlüsseln', 'Error: (*.lig)-Datei und (*.ball)-Datei nicht Kompatibel')
    elif Text == '[Error: benötigte(r) Parameter nicht vorhanden]':
        messagebox.showerror('Entschlüsseln', 'Error: benötigte(r) Parameter nicht vorhanden')
    else:
        Savepfad = filedialog.asksaveasfilename(defaultextension='.txt',filetypes=[('Textdateien', '*.txt')])
        if Savepfad:
            datei = open(Savepfad,'w',encoding='utf-8')
            datei.write(Text)
            datei.close()

# Code zum initialisieren
global Hauptfenster
Hauptfenster = tk.Tk()
global FirstRun
FirstRun = True
Fenster()