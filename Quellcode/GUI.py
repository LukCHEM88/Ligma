#===================Import benötigter Module======================#
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os, platform, darkdetect, Ligma, random

#=============================Klassen=============================#
class Fenster():
    """
    Erstellt die Fenster für die jeweiligen Teile des Programms.
    """
    def Hauptmenü():
        """
        Erstellt ein Willkommensfenster und Buttons zu den anderen Teilen des Programms.
        """
        global Error
        try:
            if Error: # Prüft, ob während der verarbeitung der Einstellungen ein Fehler aufgetreten ist und zeigt diesen ggf. an.
                messagebox.showerror('Einstellungen', 'Einstellungen konnten nicht gespeichert werden.\n' + Error)
                Error = False
        except:
            pass

        for element in Hauptfenster.winfo_children(): # GUI Elemente von anderen Funktionen werden entfernt
            element.destroy()
        Hauptfenster.title('Ligma')

        LabelWillkommen = tk.Label(Hauptfenster, text='Willkommen bei Ligma™\n\nDie schnellste und sicherste Verschlüsselungssoftware') # Platzieren der GUI
        LabelWillkommen.place(x='200', y='75', anchor='center')
        if platform.system() == 'Windows':
            LabelCopyright = tk.Label(Hauptfenster, text='Version 10.1\n\n© 2024 MANN Industries')
            LabelCopyright.place(x='200', y='235', anchor='center')
        ButtonVer = tk.Button(Hauptfenster, text='Verschlüsseln', command=Fenster.Verschlüsseln)
        ButtonVer.place(x='300', y='150', anchor='center')
        ButtonEnt = tk.Button(Hauptfenster, text='Entschlüsseln', command=Fenster.Entschlüsseln)
        ButtonEnt.place(x='100', y='150', anchor='center')
        EinstButton = tk.Button(Hauptfenster, text='⚙',command=Fenster.Einstellungen)
        EinstButton.place(x='25', y='25')

        global Settings
        if Settings.getErscheinungsbild() == 'Dunkel' or Settings.getErscheinungsbild() == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
            # TODO: Window Border
            Hauptfenster.configure(bg='#323232')
            Hauptfenster.configure(highlightbackground='#323232')
            LabelWillkommen.configure(bg='#323232')
            LabelWillkommen.configure(fg='white')
            if platform.system() == 'Windows':
                LabelCopyright.configure(bg='#323232')
                LabelCopyright.configure(fg='white')
            ButtonVer.configure(highlightbackground='#323232')
            ButtonEnt.configure(highlightbackground='#323232')
            EinstButton.configure(highlightbackground='#323232')
        else: # Lightmode wird eingestellt
            Hauptfenster.configure(bg='#ECECEC')
            Hauptfenster.configure(highlightbackground='#ECECEC')
            ButtonVer.configure(highlightbackground='#ECECEC')
            ButtonEnt.configure(highlightbackground='#ECECEC')
            LabelWillkommen.configure(bg='#ECECEC')
            if platform.system() == 'Windows':
                LabelCopyright.configure(bg='#ECECEC')
                LabelCopyright.configure(fg='black')
            LabelWillkommen.configure(fg='black')
            EinstButton.configure(highlightbackground='#ECECEC')

        global FirstRun
        if FirstRun: # Prüfung, damit die Initialisierung des Fenster nur einmal ausgeführt wird
            Hauptfenster.geometry('400x300')
            Hauptfenster.resizable('False', 'False')
            if platform.system() == 'Windows': # Wenn Ligma auf Windows ausgeführt wird, wird versucht das Icon zu öffnen
                if os.path.exists('Icon_Ligma.ico'):
                    Hauptfenster.iconbitmap('Icon_Ligma.ico')
            FirstRun = False
            Hauptfenster.mainloop() # Tkinter wird gestartet

    def Verschlüsseln():
        """
        Erstellt das Fenster mit dem Programmteil zum Verschlüsseln.
        """
        for element in Hauptfenster.winfo_children(): # GUI Elemente von anderen Funktionen werden entfernt
            element.destroy()
        Hauptfenster.title('Ligma - Verschlüsseln')

        Buttonback = tk.Button(Hauptfenster, text='← Zurück', command=Fenster.Hauptmenü) # Platzieren der GUI
        Buttonback.place(x='25', y='25')
        Buttonkeyver = tk.Button(Hauptfenster, text='Erstellen', command=Verschlüsseln.Key)
        Buttonkeyver.place(x='100', y='150', anchor='center')
        Buttonmesver = tk.Button(Hauptfenster, text='Durchsuchen', command=Verschlüsseln.Message)
        Buttonmesver.place(x='300', y='150', anchor='center')
        
        global Verschlüsselbutton
        Verschlüsselbutton = tk.Button(Hauptfenster, text='Verschlüsseln', state='disabled', command=Verschlüsseln.Start) # Button erst deaktiviert, damit die Funktion erst ausgeführt werden kann, wenn Dateien gewählt wurden
        Verschlüsselbutton.place(x='200', y='250', anchor='center')
        global LKeyVer
        LKeyVer = tk.Label(Hauptfenster, text='Kein Schlüssel ausgewählt', anchor='center')
        LKeyVer.place(x='100', y='120', width='180', anchor='center')
        global LFileVer
        LFileVer = tk.Label(Hauptfenster, text='Keine Nachricht ausgewählt', anchor='center')
        LFileVer.place(x='300', y='120', width='180', anchor='center')
        
        global Settings
        if Settings.getErscheinungsbild() == 'Dunkel' or Settings.getErscheinungsbild() == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
            Hauptfenster.configure(bg='#323232')
            Hauptfenster.configure(highlightbackground='#323232')
            Buttonback.configure(highlightbackground='#323232')
            Buttonkeyver.configure(highlightbackground='#323232')
            Buttonmesver.configure(highlightbackground='#323232')
            Verschlüsselbutton.configure(highlightbackground='#323232')
            LKeyVer.configure(bg='#323232')
            LKeyVer.configure(fg='white')
            LFileVer.configure(bg='#323232')
            LFileVer.configure(fg='white')
        else: # Lightmode wird eingestellt
            Hauptfenster.configure(bg='#ECECEC')
            Hauptfenster.configure(highlightbackground='#ECECEC')
            Buttonback.configure(highlightbackground='#ECECEC')
            Buttonkeyver.configure(highlightbackground='#ECECEC')
            Buttonmesver.configure(highlightbackground='#ECECEC')
            Verschlüsselbutton.configure(highlightbackground='#ECECEC')
            LKeyVer.configure(bg='#ECECEC')
            LKeyVer.configure(fg='black')
            LFileVer.configure(bg='#ECECEC')
            LFileVer.configure(fg='black')

        try:
            if Keypfad:
                LKeyVer['text'] = os.path.basename(Keypfad) # Fals aus einer anderen Funktion schonmal ein Key gewählt wurde wird er angezeigt
        except NameError:
            pass

    def Entschlüsseln():
        """
        Erstellt das Fenster mit dem Programmteil zum Entschlüsseln
        """
        for element in Hauptfenster.winfo_children(): # GUI Elemente von anderen Funktionen werden entfernt
            element.destroy()
        Hauptfenster.title('Ligma - Entschlüsseln')
        
        Buttonback = tk.Button(Hauptfenster, text='← Zurück', command=Fenster.Hauptmenü) # GUI wird platziert
        Buttonback.place(x='25', y='25')
        Buttonkeyent = tk.Button(Hauptfenster, text='Durchsuchen', command=Entschlüsseln.Key)
        Buttonkeyent.place(x='100', y='150', anchor='center')
        Buttonmesent = tk.Button(Hauptfenster, text='Durchsuchen', command=Entschlüsseln.Message)
        Buttonmesent.place(x='300', y='150', anchor='center')
        
        global Entschlüsselbutton
        Entschlüsselbutton = tk.Button(Hauptfenster, text='Entschlüsseln', state='disabled', command=Entschlüsseln.Start) # Button erst deaktiviert, damit die Funktion erst ausgeführt werden kann, wenn Dateien gewählt wurden
        Entschlüsselbutton.place(x='200', y='250', anchor='center')
        global LKeyEnt
        LKeyEnt = tk.Label(Hauptfenster, text='Kein Schlüssel ausgewählt', anchor='center')
        LKeyEnt.place(x='100', y='120', width='180', anchor='center')
        global LFileEnt
        LFileEnt = tk.Label(Hauptfenster, text='Keine Nachricht ausgewählt', anchor='center')
        LFileEnt.place(x='300', y='120', width='180', anchor='center')

        global Settings
        if Settings.getErscheinungsbild() == 'Dunkel' or Settings.getErscheinungsbild() == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
            Hauptfenster.configure(bg='#323232')
            Hauptfenster.configure(highlightbackground='#323232')
            Buttonback.configure(highlightbackground='#323232')
            Buttonkeyent.configure(highlightbackground='#323232')
            Buttonmesent.configure(highlightbackground='#323232')
            Entschlüsselbutton.configure(highlightbackground='#323232')
            LKeyEnt.configure(bg='#323232')
            LKeyEnt.configure(fg='white')
            LFileEnt.configure(bg='#323232')
            LFileEnt.configure(fg='white')
        else: # Lightmode wird eingestellt
            Hauptfenster.configure(bg='#ECECEC')
            Hauptfenster.configure(highlightbackground='#ECECEC')
            Buttonback.configure(highlightbackground='#ECECEC')
            Buttonkeyent.configure(highlightbackground='#ECECEC')
            Buttonmesent.configure(highlightbackground='#ECECEC')
            Entschlüsselbutton.configure(highlightbackground='#ECECEC')
            LKeyEnt.configure(bg='#ECECEC')
            LKeyEnt.configure(fg='black')
            LFileEnt.configure(bg='#ECECEC')
            LFileEnt.configure(fg='black')
        
        try:
            if Keypfad:
                LKeyEnt['text'] = os.path.basename(Keypfad) # Fals aus einer anderen Funktion schonmal ein Key gewählt wurde wird er angezeigt
        except NameError:
            pass
    
    def Einstellungen():
        """
        Erstellt das Fenster mit dem Programmteil für die Einstellungen
        """
        for element in Hauptfenster.winfo_children(): # GUI Elemente von anderen Funktionen werden entfernt
            element.destroy()
        Hauptfenster.title('Ligma - Einstellungen')

        global Settings

        Buttonback = tk.Button(Hauptfenster, text='← Zurück', command=Fenster.Hauptmenü) # Platzieren der GUI
        Buttonback.place(x='25', y='25')
        LErsch = tk.Label(Hauptfenster,text='Erscheinungsbild')
        LErsch.place(x='120', y='90', anchor='center')
        BErsch = tk.Button(Hauptfenster,text=Settings.getErscheinungsbild(),command=Settings.Erscheinungsbild)
        BErsch.place(x='300', y='90', anchor='center')
        LProg = tk.Label(Hauptfenster,text='Fortschrittsleiste')
        LProg.place(x='120', y='130', anchor='center')
        BProg = tk.Button(Hauptfenster,text=Settings.getProgStat(),command=Settings.ProgStat)
        BProg.place(x='300', y='130', anchor='center')
        LÖV = tk.Label(Hauptfenster,text='Nach Verschlüsseln öffnen')
        LÖV.place(x='120', y='170', anchor='center')
        BÖV = tk.Button(Hauptfenster,text=Settings.getOpenVer(),command=Settings.OpenVer)
        BÖV.place(x='300', y='170', anchor='center')
        LÖE = tk.Label(Hauptfenster,text='Nach Entschlüsseln öffnen')
        LÖE.place(x='120', y='210', anchor='center')
        BÖE = tk.Button(Hauptfenster,text=Settings.getOpenEnt(),command=Settings.OpenEnt)
        BÖE.place(x='300', y='210', anchor='center')
        Default = tk.Button(Hauptfenster,text='Standard Wiederherstellen',command=Settings.Default)
        Default.place(x='120', y='260', anchor='center')
        Info = tk.Button(Hauptfenster,text='Info',command=Fenster.Info)
        Info.place(x='300', y='260', anchor='center')

        if Settings.getErscheinungsbild() == 'Dunkel' or Settings.getErscheinungsbild() == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
            Hauptfenster.configure(bg='#323232')
            Hauptfenster.configure(highlightbackground='#323232')
            Buttonback.configure(highlightbackground='#323232')
            LErsch.configure(bg='#323232')
            LErsch.configure(fg='white')
            BErsch.configure(highlightbackground='#323232')
            LProg.configure(bg='#323232')
            LProg.configure(fg='white')
            BProg.configure(highlightbackground='#323232')
            LÖV.configure(bg='#323232')
            LÖV.configure(fg='white')
            BÖV.configure(highlightbackground='#323232')
            LÖE.configure(bg='#323232')
            LÖE.configure(fg='white')
            BÖE.configure(highlightbackground='#323232')
            Default.configure(highlightbackground='#323232')
            Info.configure(highlightbackground='#323232')
        else: # Lightmode wird eingestellt
            Hauptfenster.configure(bg='#ECECEC')
            Hauptfenster.configure(highlightbackground='#ECECEC')
            Buttonback.configure(highlightbackground='#ECECEC')
            LErsch.configure(bg='#ECECEC')
            LErsch.configure(fg='black')
            BErsch.configure(highlightbackground='#ECECEC')
            LProg.configure(bg='#ECECEC')
            LProg.configure(fg='black')
            BProg.configure(highlightbackground='#ECECEC')
            LÖV.configure(bg='#ECECEC')
            LÖV.configure(fg='black')
            BÖV.configure(highlightbackground='#ECECEC')
            LÖE.configure(bg='#ECECEC')
            LÖE.configure(fg='black')
            BÖE.configure(highlightbackground='#ECECEC')
            Default.configure(highlightbackground='#ECECEC')
            Info.configure(highlightbackground='#ECECEC')

    def Info():
        """
        Erstellt das Fenster mit den Informationen zu den Einstellungen
        """
        global Infofenster
        try:
            Infofenster.destroy()
        except:
            Infofenster = tk.Tk()
            Infofenster.geometry('1065x400')
            Infofenster.resizable('False', 'False')
            if (platform.system() == 'Windows'): # Wenn Ligma auf Windows ausgeführt wird, wird versucht das Icon zu öffnen
                if os.path.exists('Icon_Ligma.ico'):
                    Infofenster.iconbitmap('Icon_Ligma.ico')
                Infofenster.geometry('920x370')
            Infofenster.title('Information zu den Ligma Einstellungen')
            Label = tk.Label(Infofenster, text='''
Erscheinungsbild: Gibt an, wie die App dargestellt wird.
System → App richtet sich nach dem System.
Hell → App verwendet den hellen Modus.
Dunkel → App verwendet den dunklen Modus.

Fortschrittsleiste: Gibt an, wie häufig die Fortschrittsleiste aktualisiert wird.
Ein → Die Fortschrittsleiste wird bei jedem ver-/entschlüsselten Zeichen aktualisiert. Kann bei langsameren Rechner dazu führen, dass die App sehr lange rechnen muss.
1s → Die Fortschrittsleiste wird aktualisiert wenn je 1 Sekunde vergangen ist.
10% → Die Fortschrittsleiste wird aktualisiert wenn je 10% des Dokuments ver-/entschlüsselt wurden. Für langsamere Rechner empfohlen.
Aus → Die App arbeitet vollständig im Hintergrund. Ligma ist so am schnellsten.

Nach Verschlüsseln öffnen: Gibt an, ob der Ordner, in dem die verschlüsselte Datei gespeichert wurde, geöffnet werden soll.
Fragen → Die App fragt, ob der Ordner geöffnet werden soll.
Ordner → Die App öffnet den Ordner automatisch.
Aus → Die App öffnet den Ordner nicht.

Nach Entschlüsseln öffnen: Gibt an, ob die entschlüsselte Datei oder der Ordner, in dem diese gespeichert wurde, geöffnet werden soll.
Fragen (Datei) → Die App fragt, ob die Datei geöffnet werden soll.
Fragen (Ordner) → Die App fragt, ob der Ordner geöffnet werden soll.
Datei → Die App öffnet die Datei automatisch.
Ordner → Die App öffnet den Ordner automatisch.
Aus → Die App öffnet nichts.''', anchor='w', justify='left') # Platzieren des Info-Labels
            Label.place(x='20', y='0')
            if Settings.getErscheinungsbild() == 'Dunkel' or Settings.getErscheinungsbild() == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
                Infofenster.configure(bg='#323232')
                Infofenster.configure(highlightbackground='#323232')
                Label.configure(bg='#323232')
                Label.configure(fg='white')

class Einstellungen:
    '''
    Für die Einstellungen benötigte Prozeduren
    '''
    def __init__(self):
        '''
        Einstellungen aus Datei laden
        '''
        global Error
        save = True
        if platform.system() == 'Darwin': # macOS
            if not os.path.exists(os.path.expanduser("~/Library/Application Support/Ligma/Einstellungen.txt")): # Wenn die Einstellungen Speicherdatei noch nicht existiert wird sie über Default erstellt
                self.Default(False)
                return None
            else: # Sonst wird die Datei gelesen
                try:
                    datei = open(os.path.expanduser("~/Library/Application Support/Ligma/Einstellungen.txt"), 'r', encoding='utf-8')
                except: # Falls das Öffnen der Datei fehlschlägt wird der Fehler gespeichert
                    Error = 'Einstellungen.txt konnte nicht geöffnet werden'
                    save = False
        elif platform.system() == 'Windows': # Windows
            if not os.path.exists(os.path.join(os.environ['APPDATA'],'Ligma')): # Wenn die Einstellungen Speicherdatei noch nicht existiert wird sie über Default erstellt
                self.Default(False)
                return None
            else: # Sonst wird die Datei gelesen
                try:
                    datei = open(os.path.join(os.environ['APPDATA'],'Ligma\\Einstellungen.txt'), 'r', encoding='utf-8')
                except: # Falls das Öffnen der Datei fehlschlägt wird der Fehler gespeichert
                    Error = 'Einstellungen.txt konnte nicht geöffnet werden'
                    save = False
        else: # Wenn das Betriebssystem nicht erkannt/unterstützt wurde, wird Default ausgeführt
            self.Default(False)
            return None

        Settingstmp = [None,None,None,None]
        fehler = False
        if save: # Wenn während des Öffnens der Datei kein Fehler kam wird sie gelesen
            for i in range(4):
                try:    
                    datei.readline()
                    Settingstmp[i] = datei.readline().rstrip('\n')
                except:
                    fehler = True
            if fehler:
                self.Default()
            datei.close()
        self.__Appaerance = Settingstmp[0]
        self.__Prog = Settingstmp[1]
        self.__Ver = Settingstmp[2]
        self.__Ent = Settingstmp[3]
        self.Check()
    def Default(self, Button = True):
        '''
        Stadard wiederherstellen
        '''
        self.__Appaerance = 'System'
        self.__Prog = 'Ein'
        self.__Ver = 'Fragen'
        self.__Ent = 'Fragen (Datei)'

        self.Speichern()
        if Button: # Wenn die Prozedur über den Standard wiederherstellen Button ausgeführt wurde wird das Fenster aktualisiert
            Fenster.Einstellungen()

    def Speichern(self):
        '''
        Einstellungen in Datei speichern
        '''
        save = True
        global Error
        if platform.system() == 'Darwin': # macOS
            if not os.path.exists(os.path.expanduser("~/Library/Application Support/Ligma")): # Wenn der Ligma Ordner im Applications Support noch nicht existiert wird dieser erstellt
                try:
                    os.mkdir(os.path.expanduser("~/Library/Application Support/Ligma"))
                except: # Falls das Erstellen des Ordners fehlschlägt wird der Fehler gespeichert
                    save = False
                    Error = '[Error: Verzeichnis Ligma konnte nicht erstellt werden]'
            try: # Dann wird versucht die Datei zu erstellen
                datei = open(os.path.expanduser("~/Library/Application Support/Ligma/Einstellungen.txt"), 'w', encoding='utf-8')
            except: # Falls das Erstellen der Datei fehlschlägt wird der Fehler gespeichert
                save = False
                Error = '[Error: Einstellungen.txt konnte nicht erstelllt werden]'
        elif platform.system() == 'Windows': # Windows
            if not os.path.exists(os.path.join(os.environ['APPDATA'],'Ligma')):  # Wenn der Ligma Ordner im AppData noch nicht existiert wird dieser erstellt
                try: # Falls das Erstellen des Ordners fehlschlägt wird der Fehler gespeichert
                    os.mkdir(os.path.join(os.environ['APPDATA'],'Ligma'))
                    print(os.path.join(os.environ['APPDATA'],'Ligma'))
                except: # Falls das Erstellen des Ordners fehlschlägt wird der Fehler gespeichert
                    save = False
                    Error = '[Error: Verzeichnis Ligma konnte nicht erstellt werden]'
            try: # Dann wird versucht die Datei zu erstellen
                datei = open(os.path.join(os.environ['APPDATA'],'Ligma\\Einstellungen.txt'), 'w', encoding='utf-8')
            except: # Falls das Erstellen der Datei fehlschlägt wird der Fehler gespeichert
                save = False
                Error = '[Error: Einstellungen.txt konnte nicht erstelllt werden]'
        else: # Falls das Betriebssystem nicht erkannt/unterstützt wurde, wird der Fehler gespeichert
            save = False
            Error = '[Error: Betriebssystem nicht unterstützt/erkannt]'
            
        if save: # Wenn während des Erstellens der Datei kein Fehler kam wird sie gelesen
            datei.write('Erscheinungsbild (System/Hell/Dunkel)\n' + self.__Appaerance + '\nProgressbar (Ein/1s/10%/Aus)\n' + self.__Prog + '\nNach Verschlüsseln öffnen (Fragen/Ordner/Aus)\n' + self.__Ver + '\nNach Entschlüsseln öffnen (Fragen (Datei)/Fragen (Ordner)/Datei/Ordner/Aus)\n' + self.__Ent)
            datei.close()
            
    def Check(self):
        '''
        Überprüft, ob in der Datei Unsinn steht und berichtigt gegebenenfalls
        '''
        if not (self.__Appaerance == 'Hell' or self.__Appaerance == 'Dunkel'):
            self.__Appaerance = 'System'
        if not (self.__Prog == '1s' or self.__Prog == '10%' or self.__Prog == 'Aus'):
            self.__Prog = 'Ein'
        if not (self.__Ver == 'Datei' or self.__Ver == 'Ordner' or self.__Ver == 'Aus'):
            self.__Ver = 'Fragen'
        if not (self.__Ent == 'Fragen (Ordner)' or self.__Ent == 'Datei' or self.__Ent == 'Ordner' or self.__Ent == 'Aus'):
            self.__Ent = 'Fragen (Datei)'
        self.Speichern()

    def Erscheinungsbild(self):
        '''
        Anpassen des Erscheinugsbildes
        '''
        if self.__Appaerance == 'System':
            self.__Appaerance = 'Hell'
        elif self.__Appaerance == 'Hell':
            self.__Appaerance = 'Dunkel'
        else:
            self.__Appaerance = 'System'
        self.Speichern()
        Fenster.Einstellungen()
        
    def ProgStat(self):
        '''
        Anpassen des Status der Fortschritssleiste
        '''
        if self.__Prog == 'Ein':
            self.__Prog = '1s'
        elif self.__Prog == '1s':
            self.__Prog = '10%'
        elif self.__Prog == '10%':
            self.__Prog = 'Aus'
        else:
            self.__Prog = 'Ein'
        self.Speichern()
        Fenster.Einstellungen()
                    
    def OpenVer(self):
        '''
        Anpassen von nach Verschlüsseln öffnen
        '''
        if self.__Ver == 'Fragen':
            self.__Ver = 'Ordner'
        elif self.__Ver == 'Ordner':
            self.__Ver = 'Aus'
        else:
            self.__Ver = 'Fragen'
        self.Speichern()
        Fenster.Einstellungen()

    def OpenEnt(self):
        '''
        Anpassen von nach Entschlüsseln öffnen
        '''
        if self.__Ent == 'Fragen (Datei)':
            self.__Ent = 'Fragen (Ordner)'
        elif self.__Ent == 'Fragen (Ordner)':
            self.__Ent = 'Datei'
        elif self.__Ent == 'Datei':
            self.__Ent = 'Ordner'
        elif self.__Ent == 'Ordner':
            self.__Ent = 'Aus'
        else:
            self.__Ent = 'Fragen (Datei)'
        self.Speichern()
        Fenster.Einstellungen()

    def getErscheinungsbild(self):
        return self.__Appaerance
    def getProgStat(self):
        return self.__Prog
    def getOpenVer(self):
        return self.__Ver
    def getOpenEnt(self):
        return self.__Ent
    
class LigmaEinstellungen(Einstellungen):
    '''
    Einstellungen für das Ligma-Programm
    '''
    def __init__(self):
        super().__init__()
    def getProgStat(self):
        tmp = super().getProgStat()
        if tmp == 'Ein': # Einstellungen werden für Ligma.py formatiert
            return [True, 1]
        elif tmp == '1s':
            return [True, 2]
        elif tmp == '10%':
            return [True, 3]
        elif tmp == 'Aus':
            return [False, 3]



#=============================Verschlüsseln-Funktionen=============================#

class Verschlüsseln:
    '''
    Für die Verschlüsselung benötigte Prozeduren
    '''
    def Key():
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
                Verschlüsselbutton['state'] = 'normal' # Aktiviert Start, wenn beide Dateien ausgewählt wurden
        except NameError:
            pass

    def Message():
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
                Verschlüsselbutton['state'] = 'normal' # Aktiviert Start, wenn beide Dateien ausgewählt wurden
        except NameError:
            pass

    def Start():
        """
        Wird aktiv, wenn eine Schlüsseldatei und eine Nachrichtdatei ausgewählt wurde.
        Verschlüsselt die Datei mit Ligma.
        """
        global Settings
        datei = open(DateiVerpfad, 'r', encoding='utf-8') # Zu verschlüsselnde Datei wird eingelesen und in message gespeichert
        message = ''
        for zeile in datei:
            message += zeile
        datei.close()

        LigmaSettingstmp = LigmaEinstellungen() 
        LigmaSettings = LigmaSettingstmp.getProgStat()
        LigmaSettings.append(LigmaSettingstmp.getErscheinungsbild())

        Anz = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Stärke der Verschlüsselung ein: ', initialvalue=50, minvalue=1) # Frage nach Stärke der Verschlüsselung
        if Anz: # Failsave, wenn der Nutzer bei der Integereingabe auf Cancel drückt
            Text = Ligma.Primaer.Raedern(message, 'v', Anz, Keypfad, LigmaSettings) # Nutzereingaben werden an Ligma weitergegeben zum Verschüsseln

            if Text[0]: # Fals Ligma ein Fehler zurückgibt wird dieser angezeigt. Sonst wird gespeichert
                Savepfad = filedialog.asksaveasfilename(defaultextension='.ball', filetypes=[('Verschlüsselte Dateien', '*.ball')]) # Frage nach Speicherort der verschlüsselten Datei
                if Savepfad: # Failsave, fals Nutzer auf Cancel drückt
                    datei = open(Savepfad, 'w', encoding='utf-8')
                    datei.write(Text[1]) # Speichern
                    datei.close()
                    
                    message = len(message) # länge der message wird gespeichert, um den vorgeschlagenen Wert für die Menge der durch Sekundärverschlüsselung hinzugefügten Zeichen mit message//10 berechnen zu können
                    Anz2 = False
                    Anz2 = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Menge der per Sekundärverschlüsselung hinzugefügten Zeichen ein: ', initialvalue=message//10, minvalue=0) # Frage nach Stärke der Sekundäverschlüsselung. Standartmäßig 10%.
                    if not Anz2:
                        Anz2 = 0
                    Anz3 = Anz2
                    while (Anz3 > 0): # Nutzereingaben werden zufällig aufgeteilt an Ligma weitergegeben zum Sekundärverschüsseln
                        Zufallszahl = random.randint(Anz2 // 20, Anz2)
                        if (Anz3 > Zufallszahl):
                            Ligma.Sekundaer.Versch(Zufallszahl, Keypfad, Savepfad)
                            Anz3 -= Zufallszahl
                        else:
                            Ligma.Sekundaer.Versch(Anz3, Keypfad, Savepfad)
                            Anz3 = 0
                    messagebox.showinfo('Verschlüsseln', 'Sekundärverschlüsselung abgeschlossen.')
                    if Settings.getOpenVer() == 'Ordner': # Wenn das automatische Öffnen des Ordners eingestellt ist wird dieser geöffnet
                        if platform.system() == 'Windows':
                            os.startfile(Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)))
                        elif platform.system() == 'Darwin':
                            os.system('open "{}"'.format(Savepfad.rstrip(os.path.basename(Savepfad))))
                        else: # Wenn das Betriebssystem nicht erkannt/unterstützt wurde, wird ein Fehler angezeigt
                            messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
                    elif Settings.getOpenVer() == 'Fragen': # Wenn Fragen eingestellt ist, wird gefragt, ob der Ordner geöffnet werden soll
                        if messagebox.askokcancel('Verschlüsseln', 'Möchten Sie den Ordner ' + Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)) + ' öffnen?'):
                            if platform.system() == 'Windows':
                                os.startfile(Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)))
                            elif platform.system() == 'Darwin':
                                os.system('open "{}"'.format(Savepfad.rstrip(os.path.basename(Savepfad))))
                            else: # Wenn das Betriebssystem nicht erkannt/unterstützt wurde, wird ein Fehler angezeigt
                                messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
            else:
                messagebox.showerror('Verschlüsseln', Text[1])

#=============================Enstschlüsseln-Funktionen=============================#
                
class Entschlüsseln:
    def Key():
        """
        Fragt nach einer Schlüsseldatei zum Entschlüsseln und Speichert diese in Keypfad.
        """
        global Keypfad

        Keytmp = filedialog.askopenfilename(filetypes=[('Schlüsseldateien', '*.lig')])
        if Keytmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
            Keypfad = Keytmp
            LKeyEnt['text'] = os.path.basename(Keypfad) # Zeigt ausgewählte Datei an
        
        try:
            if DateiEntpfad and Keypfad: # Aktiviert Start, wenn beide Dateien ausgewählt wurden
                Entschlüsselbutton['state'] = 'normal'
        except NameError:
            pass

    def Message():
        """
        Fragt nach einer Verschlüsselten Datei und Speichert deren Pfad in Dateipfad.
        """
        global DateiEntpfad

        Dateitmp = filedialog.askopenfilename(filetypes=[('Verschlüsselte Datei', '*.ball')])
        if Dateitmp: # Failsave, wenn der Nutzer bei der Dateiauswahl auf Cancel drückt
            DateiEntpfad = Dateitmp
            LFileEnt['text'] = os.path.basename(DateiEntpfad) # Zeigt ausgewählte Datei an
        
        try:
            if Keypfad and DateiEntpfad: # Aktiviert Start, wenn beide Dateien ausgewählt wurden
                Entschlüsselbutton['state'] = 'normal'
        except NameError:
            pass

    def Start():
        """
        Wird aktiv, wenn eine Schlüsseldatei und eine Verschlüsselte Datei ausgewählt wurde.
        Entschlüsselt die Datei mit Ligma.
        """
        global Settings

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

        Ligma.Sekundaer.Entsch(Keypfad, DateiEntpfad) # Entschlüsselt die Sekundärverschlüsselung der Datei mit Ligma

        datei = open(DateiEntpfad, 'r', encoding='utf-8') # Verschlüsselte Datei wird eingelesen und in ball gespeichert
        ball = ''
        for zeile in datei:
            ball += zeile
        datei.close()

        LigmaSettingstmp = LigmaEinstellungen() 
        LigmaSettings = LigmaSettingstmp.getProgStat()
        LigmaSettings.append(LigmaSettingstmp.getErscheinungsbild())

        Text = Ligma.Primaer.Raedern(ball, 'e', 0, Keypfad, LigmaSettings) # Datei wird entschlüsselt
        if Text[0]: # Fals Ligma ein Fehler zurückgibt wird dieser angezeigt. Sonst wird gespeichert
            Savepfad = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Textdateien', '*.txt')]) # Fragt nach Speicherort
            if Savepfad: # Failsave, fals Cancel
                datei = open(Savepfad, 'w', encoding='utf-8') # Speichert
                datei.write(Text[1])
                datei.close()
                if Settings.getOpenEnt() == 'Ordner': # Wenn das automatische Öffnen des Ordners eingestellt ist wird dieser geöffnet
                    if platform.system() == 'Windows':
                        os.startfile(Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)))
                    elif platform.system() == 'Darwin':
                        os.system('open "{}"'.format(Savepfad.rstrip(os.path.basename(Savepfad))))
                    else: # Wenn das Betriebssystem nicht erkannt/unterstützt wurde, wird ein Fehler angezeigt
                        messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
                elif Settings.getOpenEnt() == 'Datei': # Wenn das automatische Öffnen der Datei eingestellt ist wird dieser geöffnet
                    if platform.system() == 'Windows':
                        os.startfile(Savepfad.replace('/','\\'))
                    elif platform.system() == 'Darwin':
                        os.system('open "{}"'.format(Savepfad))
                    else: # Wenn das Betriebssystem nicht erkannt/unterstützt wurde, wird ein Fehler angezeigt
                        messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
                elif Settings.getOpenEnt() == 'Fragen (Datei)': # Wenn Fragen eingestellt ist, wird gefragt, ob die Datei geöffnet werden soll
                    if messagebox.askokcancel('Verschlüsseln', 'Möchten Sie die Datei ' + os.path.basename(Savepfad) + ' öffnen?'):
                        if platform.system() == 'Windows':
                            os.startfile(Savepfad.replace('/','\\'))
                        elif platform.system() == 'Darwin':
                            os.system('open "{}"'.format(Savepfad))
                        else: # Wenn das Betriebssystem nicht erkannt/unterstützt wurde, wird ein Fehler angezeigt
                            messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
                elif Settings.getOpenEnt() == 'Fragen (Ordner)': # Wenn Fragen eingestellt ist, wird gefragt, ob der Ordner geöffnet werden soll
                    if messagebox.askokcancel('Verschlüsseln', 'Möchten Sie den Ordner ' + Savepfad.rstrip(os.path.basename(Savepfad)) + ' öffnen?'):
                        if platform.system() == 'Windows':
                            os.startfile(Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)))
                        elif platform.system() == 'Darwin':
                            os.system('open "{}"'.format(Savepfad.rstrip(os.path.basename(Savepfad))))
                        else: # Wenn das Betriebssystem nicht erkannt/unterstützt wurde, wird ein Fehler angezeigt
                            messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
        else:
            messagebox.showerror('Entschlüsseln', Text[1])

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
Settings = Einstellungen()
Fenster.Hauptmenü()