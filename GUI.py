# Import benötigter Module
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
import os, platform
import Ligma, LigmaB

#=====================Darkmode-Check=====================#
def Darkmode_Check_Windows():
    import ctypes
    try:
        color = ctypes.windll.dwmapi.GetColorizationColor()
        # Wenn der Hintergrundfarbwert dunkel ist, gehe davon aus, dass der Dunkelmodus aktiv ist
        return color & 0x000000FF < 128
    except Exception as e:
        return None
def Darkmode_Check_macOS():
    from subprocess import check_output
    try:
        # Verwende den `defaults`-Befehl, um den aktuellen Modus abzurufen
        result = check_output(["defaults", "read", "-g", "AppleInterfaceStyle"]).decode().strip()
        return result.lower() == "dark"
    except Exception as e:
        return False

if platform.system() == 'Windows':
    #Darkmode = Darkmode_Check_Windows()
    Darkmode = True
if platform.system() == 'Darwin':
    Darkmode = Darkmode_Check_macOS()

print('Darkmode =',Darkmode)

#=============================Funktionen=============================#
def Fenster():
    """
    Erstellt ein Willkommensfenster und Buttons zu den anderen Teilen des Programms.
    """

    if (platform.system() == 'Windows'): # Wenn Ligma auf Windows ausgeführt wird, wird versucht das Icon zu öffnen
        if os.path.exists(os.path.expanduser('~\\Ligma\\Icon_Ligma.ico')):
            Hauptfenster.iconbitmap(os.path.expanduser('~\\Ligma\\Icon_Ligma.ico'))
        elif os.path.exists('Icon_Ligma.ico'):
            Hauptfenster.iconbitmap('Icon_Ligma.ico')

    for element in Hauptfenster.winfo_children(): # GUI Elemente von anderen Funktionen werden entfernt
        element.destroy()
    Hauptfenster.title('Ligma')

    Label1 = tk.Label(Hauptfenster, text='Willkommen bei Ligma™\n\nDie schnellste und sicherste Verschlüsselungssoftware')
    Label1.place(x='200', y='75', anchor='center') # Platzieren der GUI
    Label2 = tk.Label(Hauptfenster, text='© 2024/25 MANN Industries')
    Label2.place(x='200', y='250', anchor='center')
    Button1 = tk.Button(Hauptfenster, text='Verschlüsseln', command=Verschlüsseln)
    Button1.place(x='300', y='150', anchor='center')
    Button2 = tk.Button(Hauptfenster, text='Entschlüsseln', command=Entschlüsseln)
    Button2.place(x='100', y='150', anchor='center')
    
    if Darkmode:
        #style = ttk.Style()
        #style.configure('TFrame', background='black')
        #frame = ttk.Frame(Hauptfenster)
        #frame.pack(side='top', fill='both', expand=True)
        Hauptfenster.configure(bg='black')
        Hauptfenster.configure(highlightbackground='black')
        Label1.configure(bg='black')
        Label2.configure(bg='black')
        Label1.configure(fg='white')
        Label2.configure(fg='white')
        Button1.configure(highlightbackground='black')
        Button2.configure(highlightbackground='black')


    global FirstRun
    if FirstRun: # Prüfung, damit die Initialisierung des Fenster nur einmal ausgeführt wird
        Hauptfenster.geometry('400x300')
        Hauptfenster.resizable('False', 'False')
        FirstRun = False
        Hauptfenster.mainloop()

#=============================Verschlüsseln-Funktionen=============================#
def Verschlüsseln():
    """
    Erstellt das Fenster mit dem Programmteil zum Verschlüsseln.
    """
    for element in Hauptfenster.winfo_children(): # GUI Elemente von anderen Funktionen werden entfernt
        element.destroy()
    Hauptfenster.title('Ligma - Verschlüsseln')

    tk.Button(Hauptfenster, text='← Zurück', command=Fenster).place(x='25', y='25') # Platzieren der GUI
    tk.Button(Hauptfenster, text='Erstellen', command=DateiKeyVer).place(x='100', y='150', anchor='center')
    tk.Button(Hauptfenster, text='Durchsuchen', command=DateiMessageVer).place(x='300', y='150', anchor='center')
    
    global Verschlüsselbutton
    Verschlüsselbutton = tk.Button(Hauptfenster, text='Verschlüsseln', state='disabled', command=Versch) # Button erst deaktiviert, damit die Funktion erst ausgeführt werden kann, wenn Dateien gewählt wurden
    Verschlüsselbutton.place(x='200', y='250', anchor='center')
    
    global LKeyVer
    LKeyVer = tk.Label(Hauptfenster, text='Kein Schlüssel ausgewählt', anchor='center')
    LKeyVer.place(x='100', y='120', width='180', anchor='center')
    
    global LFileVer
    LFileVer = tk.Label(Hauptfenster, text='Keine Nachricht ausgewählt', anchor='center')
    LFileVer.place(x='300', y='120', width='180', anchor='center')
    
    try:
        if Keypfad:
            LKeyVer['text'] = os.path.basename(Keypfad) # Fals aus einer anderen Funktion schonmal ein Key gewählt wurde wird er angezeigt
    except NameError:
        pass

def DateiKeyVer():
    """
    Fragt nach Speicherort der Schlüsseldatei.
    """
    global Keypfad

    Keytmp = filedialog.asksaveasfilename(defaultextension='.lig', filetypes=[('Schlüsseldateien', '*.lig')])
    if Keytmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
        Keypfad = Keytmp
        LKeyVer['text'] = os.path.basename(Keypfad) # Zeigt ausgewählte Datei an
    
    try:
        if DateiVerpfad and Keypfad:
            Verschlüsselbutton['state'] = 'normal' # Aktiviert Versch, wenn beide Dateien ausgewählt wurden
    except NameError:
        pass

def DateiMessageVer():
    """
    Fragt nach der Nachrichtdatei zum Verschlüsseln und Speichert diese in Dateipfad.
    """
    global DateiVerpfad

    Dateitmp = filedialog.askopenfilename(filetypes=[('Textdatei', '*.txt')])
    if Dateitmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
        DateiVerpfad = Dateitmp
        LFileVer['text'] = os.path.basename(DateiVerpfad) # Zeigt ausgewählte Datei an
    
    try:
        if Keypfad and DateiVerpfad:
            Verschlüsselbutton['state'] = 'normal' # Aktiviert Versch, wenn beide Dateien ausgewählt wurden
    except NameError:
        pass

def Versch():
    """
    Wird aktiv, wenn eine Schlüsseldatei und eine Nachrichtdatei ausgewählt wurde.
    Verschlüsselt die Datei mit Ligma und LigmaB.
    """
    datei = open(DateiVerpfad, 'r', encoding='utf-8') # Zu verschlüsselnde Datei wird eingelesen und in message gespeichert
    message = ''
    for zeile in datei:
        message += zeile
    datei.close()
    
    Anz = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Stärke der Verschlüsselung ein: ', initialvalue=50, minvalue=1) # Frage nach Stärke der Verschlüsselung
    if Anz: # Failsave, wenn der Nutzer bei der Integereingabe auf Cancel drückt
        Text = Ligma.Raedern(message, 'v', Anz, Keypfad) # Nutzereingaben werden an Ligma weitergegeben zum Verschüsseln

        if Text == '[Error: Keydatei wurde nicht gefunden]': # Fals Ligma ein Fehler zurückgibt wird dieser angezeigt. Sonst wird gespeichert
            messagebox.showerror('Verschlüsseln', Text)
        elif Text == '[Error: benötigte(r) Parameter nicht vorhanden]':
            messagebox.showerror('Verschlüsseln', Text)
        elif Text == '[Error: Keydatei kann nicht geöffnet werden]':
            messagebox.showerror('Verschlüsseln', '[Error: Keydatei kann nicht geöffnet werden]')
        elif Text == '[Error: Keydatei kann nicht überschrieben/erstellt werden]':
            messagebox.showerror('Verschlüsseln', '[Error: Keydatei kann nicht überschrieben/erstellt werden]')
        else:
            Savepfad = filedialog.asksaveasfilename(defaultextension='.ball', filetypes=[('Verschlüsselte Dateien', '*.ball')]) # Frage nach Speicherort der verschlüsselten Datei
            if Savepfad: # Failsave, fals Nutzer auf Cancel drückt
                datei = open(Savepfad, 'w', encoding='utf-8')
                datei.write(Text) # Speichern
                datei.close()
                
                SekAnz = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Anzahl der Sekundärverschlüsselungen an: ', initialvalue=1, minvalue=0) # Frage nach Menge der Sekundärverschlüsselungen
                message = len(message)
                if SekAnz: # Failsave, fals Cancel
                    for i in range(SekAnz):
                        Anz2 = False
                        while not Anz2: # Failsave, fals Cancel
                            Anz2 = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Stärke der ' + str(i+1) + '. Sekundärverschlüsselung ein: ', initialvalue=message//10, minvalue=1, maxvalue=message//2) # Frage nach Stärke der Sekundäverschlüsselung. Standartmäßig 10%.
                            if not Anz2:
                                messagebox.showerror('Verschlüsseln', 'Sie müssen einen Wert eingeben.') # Nutzer wird informiert, dass er etwas eingeben muss.
                        message += Anz2
                        LigmaB.Versch(Anz2,Keypfad,Savepfad) # Nutzereingaben werden an LigmaB weitergegeben zum Sekundärverschüsseln

#=============================Enstschlüsseln-Funktionen=============================#
def Entschlüsseln():
    """
    Erstellt das Fenster mit dem Programmteil zum Entschlüsseln
    """
    for element in Hauptfenster.winfo_children(): # GUI Elemente von anderen Funktionen werden entfernt
        element.destroy()
    Hauptfenster.title('Ligma - Entschlüsseln')
    
    tk.Button(Hauptfenster, text='← Zurück', command=Fenster).place(x='25', y='25') # GUI wird platziert
    tk.Button(Hauptfenster, text='Durchsuchen', command=DateiKeyEnt).place(x='100', y='150', anchor='center')
    tk.Button(Hauptfenster, text='Durchsuchen', command=DateiMessageEnt).place(x='300', y='150', anchor='center')
    
    global Entschlüsselbutton
    Entschlüsselbutton = tk.Button(Hauptfenster, text='Entschlüsseln', state='disabled', command=Entsch) # Button erst deaktiviert, damit die Funktion erst ausgeführt werden kann, wenn Dateien gewählt wurden
    Entschlüsselbutton.place(x='200', y='250', anchor='center')
    
    global LKeyEnt
    LKeyEnt = tk.Label(Hauptfenster, text='Kein Schlüssel ausgewählt', anchor='center')
    LKeyEnt.place(x='100', y='120', width='180', anchor='center')
    
    global LFileEnt
    LFileEnt = tk.Label(Hauptfenster, text='Keine Nachricht ausgewählt', anchor='center')
    LFileEnt.place(x='300', y='120', width='180', anchor='center')
    
    try:
        if Keypfad:
            LKeyEnt['text'] = os.path.basename(Keypfad) # Fals aus einer anderen Funktion schonmal ein Key gewählt wurde wird er angezeigt
    except NameError:
        pass

def DateiKeyEnt():
    """
    Fragt nach einer Schlüsseldatei zum Entschlüsseln und Speichert diese in Keypfad.
    """
    global Keypfad

    Keytmp = filedialog.askopenfilename(filetypes=[('Schlüsseldateien', '*.lig')])
    if Keytmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
        Keypfad = Keytmp
        LKeyEnt['text'] = os.path.basename(Keypfad) # Zeigt ausgewählte Datei an
    
    try:
        if DateiEntpfad and Keypfad: # Aktiviert Entsch, wenn beide Dateien ausgewählt wurden
            Entschlüsselbutton['state'] = 'normal'
    except NameError:
        pass

def DateiMessageEnt():
    """
    Fragt nach einer Verschlüsselten Datei und Speichert deren Pfad in Dateipfad.
    """
    global DateiEntpfad

    Dateitmp = filedialog.askopenfilename(filetypes=[('Verschlüsselte Datei', '*.ball')])
    if Dateitmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
        DateiEntpfad = Dateitmp
        LFileEnt['text'] = os.path.basename(DateiEntpfad) # Zeigt ausgewählte Datei an
    
    try:
        if Keypfad and DateiEntpfad: # Aktiviert Entsch, wenn beide Dateien ausgewählt wurden
            Entschlüsselbutton['state'] = 'normal'
    except NameError:
        pass

def Entsch():
    """
    Wird aktiv, wenn eine Schlüsseldatei und eine Verschlüsselte Datei ausgewählt wurde.
    Entschlüsselt die Datei mit Ligma und LigmaB.
    """
    datei = open(DateiEntpfad, 'r', encoding='utf-8') # Speichert den Ursprungszustand des Schlüssels und der verschlüsselten Datei zwischen
    NachrichtOriginal = ''
    for element in datei:
        NachrichtOriginal += element
    datei.close()

    datei = open(Keypfad, 'r', encoding='utf-8')
    KeyOriginal = ''
    for element in datei:
        KeyOriginal += element
    datei.close()

    SekAnz = False
    while not SekAnz: # Failsave, fals Cancel
        SekAnz = simpledialog.askinteger('Entschlüsseln','Bitte geben sie die Anzahl der Sekundärverschlüsselungen ein: ', initialvalue=1, minvalue=0) # Fragt nach Anzahl der Sekundärverschlüsselungen
        if SekAnz == 0: # Da 0 als False gewertet wird, muss sie extra behandelt werden
            break
    
    for i in range(SekAnz):
        LigmaB.Entsch(Keypfad, DateiEntpfad) # Sekundärverschlüsselungen werden entfernt
    
    datei = open(DateiEntpfad, 'r', encoding='utf-8') # Verschlüsselte Datei wird eingelesen und in ball gespeichert
    ball = ''
    for zeile in datei:
        ball += zeile
    datei.close()

    Text = Ligma.Raedern(ball, 'e', 0, Keypfad) # ball wird entschlüsselt
    if Text == '[Error: Keydatei wurde nicht gefunden]': # Fals Ligma ein Fehler zurückgibt wird dieser angezeigt. Sonst wird gespeichert
        messagebox.showerror('Entschlüsseln', Text)
    elif Text == '[Error: (*.lig)-Datei und (*.ball)-Datei nicht Kompatibel]':
        messagebox.showerror('Entschlüsseln', Text)
    elif Text == '[Error: benötigte(r) Parameter nicht vorhanden]':
        messagebox.showerror('Entschlüsseln', Text)
    elif Text == '[Error: Keydatei kann nicht geöffnet werden]':
        messagebox.showerror('Verschlüsseln', Text)
    elif Text == '[Error: Keydatei kann nicht überschrieben/erstellt werden]':
        messagebox.showerror('Verschlüsseln', Text)
    
    else:
        Savepfad = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Textdateien', '*.txt')]) # Fragt nach Speicherort
        if Savepfad: # Failsave, fals Cance
            datei = open(Savepfad, 'w', encoding='utf-8') # Speichert
            datei.write(Text)
            datei.close()

    datei = open(DateiEntpfad, 'w', encoding='utf-8') # Stellt den Ursprungszustand des Schlüssels und der verschlüsselten Datei wieder her, um diese wiederverwenden zu können
    datei.write(NachrichtOriginal)
    datei.close()
    datei = open(Keypfad, 'w', encoding='utf-8')
    datei.write(KeyOriginal)
    datei.close()


#=============================Code zum initialisieren=============================#
global Hauptfenster
Hauptfenster = tk.Tk()
FirstRun = True
Fenster()