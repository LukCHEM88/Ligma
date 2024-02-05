# Import benötigter Module
from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
import os, platform

class Window(Tk):
    def __init__(self) -> None:
        global Keypfad

        self = Tk()
        self.title('Ligma')

        if (platform.system() == 'Windows'): # Wenn Ligma auf Windows ausgeführt wird, wird versucht das Icon zu öffnen
            if os.path.exists(os.path.expanduser('~\\Ligma\\Icon_Ligma.ico')):
                self.iconbitmap(os.path.expanduser('~\\Ligma\\Icon_Ligma.ico'))
            elif os.path.exists('Icon_Ligma.ico'):
                self.iconbitmap('Icon_Ligma.ico')

    def Main(self):
            #print(type(self.master))
            self.title('Ligma')

            tk.Label(self, text='Willkommen bei Ligma™\n\nDie schnellste und sicherste Verschlüsselungssoftware').place(x='200', y='75', anchor='center')
            tk.Label(self, text='© 2024/25 MANN Industries').place(x='200', y='250', anchor='center')
            tk.Button(self, text='Verschlüsseln', command=Verschlüsseln).place(x='300', y='150', anchor='center')
            tk.Button(self, text='Entschlüsseln', command=Entschlüsseln).place(x='100', y='150', anchor='center')
    
            self.mainloop()

    def Ver(self):
            self.title('Ligma - Verschlüsseln')

            tk.Button(self, text='← Zurück', command=Main).place(x='25', y='25')
            tk.Button(self, text='Erstellen', command=DateiKeyVer).place(x='100', y='150', anchor='center')
            tk.Button(self, text='Durchsuchen', command=DateiMessageVer).place(x='300', y='150', anchor='center')
    
            global Verschlüsselbutton
            Verschlüsselbutton = tk.Button(self, text='Verschlüsseln', state='disabled', command=Versch)
            Verschlüsselbutton.place(x='200', y='250', anchor='center')

            global LKeyVer
            LKeyVer = tk.Label(self, text='Kein Schlüssel ausgewählt', anchor='center')
            LKeyVer.place(x='100', y='120', width='180', anchor='center')
    
            global LFileVer
            LFileVer = tk.Label(self, text='Keine Nachricht ausgewählt', anchor='center')
            LFileVer.place(x='300', y='120', width='180', anchor='center')
    
            try:
                if Keypfad:
                    LKeyVer['text'] = os.path.basename(Keypfad)
            except NameError:
                pass

    def Ent(self):
            tk.Button(self, text='← Zurück', command=Main).place(x='25', y='25')
            tk.Button(self, text='Durchsuchen', command=DateiKeyEnt).place(x='100', y='150', anchor='center')
            tk.Button(self, text='Durchsuchen', command=DateiMessageEnt).place(x='300', y='150', anchor='center')
    
            global Entschlüsselbutton
            Entschlüsselbutton = tk.Button(self, text='Entschlüsseln', state='disabled', command=Entsch)
            Entschlüsselbutton.place(x='200', y='250', anchor='center')
    
            global LKeyEnt
            LKeyEnt = tk.Label(self, text='Kein Schlüssel ausgewählt', anchor='center')
            LKeyEnt.place(x='100', y='120', width='180', anchor='center')
    
            global LFileEnt
            LFileEnt = tk.Label(self, text='Keine Nachricht ausgewählt', anchor='center')
            LFileEnt.place(x='300', y='120', width='180', anchor='center')
    
            try:
                if Keypfad:
                    LKeyEnt['text'] = os.path.basename(Keypfad)
            except NameError:
                pass

#=============================Fenster-Funktionen=============================#
def Main():
    Fenster.Main()

def Verschlüsseln():
    Fenster.Ver()

def Entschlüsseln():
    Fenster.Ent()

#=============================Verschlüsseln-Funktionen=============================#
def DateiKeyVer():
    """
    Fragt nach Speicherort der Schlüsseldatei
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
    Fragt nach der Nachrichtdatei zum Verschlüsseln und Speichert diese in Dateipfad
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
    Wird aktiv, wenn eine Schlüsseldatei und eine Nachrichtdatei ausgewählt wurde
    Verschlüsselt die Datei
    """
    datei = open(DateiVerpfad, 'r', encoding='utf-8')
    message = ''
    for zeile in datei:
        message += zeile
    datei.close()
    
    Anz = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Stärke der Verschlüsselung ein: ', initialvalue=50, minvalue=1)
    if Anz: # Failsave, wenn der Nutzer bei der Integereingabe auf Cancel drückt
        Text = Ligma.Raedern(message, 'v', Anz, Keypfad)

        if (Text == '[Error: Keydatei wurde nicht gefunden]'):
            messagebox.showerror('Verschlüsseln', Text)
        elif (Text == '[Error: benötigte(r) Parameter nicht vorhanden]'):
            messagebox.showerror('Verschlüsseln', Text)
        else:
            Savepfad = filedialog.asksaveasfilename(defaultextension='.ball', filetypes=[('Verschlüsselte Dateien', '*.ball')])
            if Savepfad:
                datei = open(Savepfad, 'w', encoding='utf-8')
                datei.write(Text)
                datei.close()
                
                SekAnz = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Anzahl der Sekundärverschlüsselungen an: ', initialvalue=1, minvalue=0)
                message = len(message)
                if SekAnz:
                    for i in range(SekAnz):
                        Anz2 = False
                        while not Anz2:
                            Anz2 = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Stärke der ' + str(i+1) + '. Sekundärverschlüsselung ein: ', initialvalue=message//10, minvalue=1, maxvalue=message//2)
                        message += Anz2
                        LigmaB.Versch(Anz2,Keypfad,Savepfad)

#=============================Enstschlüsseln-Funktionen=============================#
def DateiKeyEnt():
    """
    Fragt nach einer Schlüsseldatei zum Entschlüsseln und Speichert diese in Keypfad
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
    Fragt nach einer Verschlüsselten Datei und Speichert deren Pfad in Dateipfad
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
    Wird aktiv, wenn eine Schlüsseldatei und eine Verschlüsselte Datei ausgewählt wurde
    Entschlüsselt die Datei mit dem Schlüssel
    """
    SekAnz = False
    while not SekAnz:
        SekAnz = simpledialog.askinteger('Entschlüsseln','Bitte geben sie die Anzahl der Sekundärverschlüsselungen ein: ', initialvalue=1, minvalue=0)
        if SekAnz == 0:
            break
    
    for i in range(SekAnz):
        LigmaB.Entsch(Keypfad, DateiEntpfad)
    
    datei = open(DateiEntpfad, 'r', encoding='utf-8')
    ball = ''
    for zeile in datei:
        ball += zeile
    datei.close()

    Text = Ligma.Raedern(ball, 'e', 0, Keypfad)
    if (Text == '[Error: Keydatei wurde nicht gefunden]'):
        messagebox.showerror('Entschlüsseln', Text)
    elif (Text == '[Error: (*.lig)-Datei und (*.ball)-Datei nicht Kompatibel]'):
        messagebox.showerror('Entschlüsseln', Text)
    elif (Text == '[Error: benötigte(r) Parameter nicht vorhanden]'):
        messagebox.showerror('Entschlüsseln', Text)
    
    else:
        Savepfad = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Textdateien', '*.txt')])
        if Savepfad:
            datei = open(Savepfad, 'w', encoding='utf-8')
            datei.write(Text)
            datei.close()

global Fenster
Fenster = Window()
Main()