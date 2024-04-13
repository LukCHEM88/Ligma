# Import benötigter Module
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, font
import os, platform, darkdetect, Ligma

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
            if Error:
                messagebox.showerror('Einstellungen', 'Einstellungen konnten nicht gespeichert werden.\n' + Error)
                Error = False
        except:
            pass

        for element in Hauptfenster.winfo_children(): # GUI Elemente von anderen Funktionen werden entfernt
            element.destroy()
        Hauptfenster.title('Ligma')

        LabelWillkommen = tk.Label(Hauptfenster, text='Willkommen bei Ligma™\n\nDie schnellste und sicherste Verschlüsselungssoftware') # Platzieren der GUI
        LabelWillkommen.place(x='200', y='75', anchor='center')
        LabelCopyright = tk.Label(Hauptfenster, text='Version 5.0\n\n© 2024 MANN Industries')
        LabelCopyright.place(x='200', y='235', anchor='center')
        ButtonVer = tk.Button(Hauptfenster, text='Verschlüsseln', command=Fenster.Verschlüsseln)
        ButtonVer.place(x='300', y='150', anchor='center')
        ButtonEnt = tk.Button(Hauptfenster, text='Entschlüsseln', command=Fenster.Entschlüsseln)
        ButtonEnt.place(x='100', y='150', anchor='center')
        EinstButton = tk.Button(Hauptfenster, text='⚙',command=Fenster.Einstellungen)
        EinstButton.place(x='25', y='25')

        global Settings
        if Settings[0] == 'Dunkel' or Settings[0] == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
            # TODO: Window Border
            Hauptfenster.configure(bg='#323232')
            Hauptfenster.configure(highlightbackground='#323232')
            LabelWillkommen.configure(bg='#323232')
            LabelCopyright.configure(bg='#323232')
            LabelWillkommen.configure(fg='white')
            LabelCopyright.configure(fg='white')
            ButtonVer.configure(highlightbackground='#323232')
            ButtonEnt.configure(highlightbackground='#323232')
            EinstButton.configure(highlightbackground='#323232')
        else:
            Hauptfenster.configure(bg='#ECECEC')
            Hauptfenster.configure(highlightbackground='#ECECEC')
            ButtonVer.configure(highlightbackground='#ECECEC')
            ButtonEnt.configure(highlightbackground='#ECECEC')
            LabelWillkommen.configure(bg='#ECECEC')
            LabelCopyright.configure(bg='#ECECEC')
            LabelWillkommen.configure(fg='black')
            LabelCopyright.configure(fg='black')
            EinstButton.configure(highlightbackground='#ECECEC')

        global FirstRun
        if FirstRun: # Prüfung, damit die Initialisierung des Fenster nur einmal ausgeführt wird
            Hauptfenster.geometry('400x300')
            Hauptfenster.resizable('False', 'False')
            if (platform.system() == 'Windows'): # Wenn Ligma auf Windows ausgeführt wird, wird versucht das Icon zu öffnen
                if os.path.exists('Icon_Ligma.ico'):
                    Hauptfenster.iconbitmap('Icon_Ligma.ico')
            FirstRun = False
            Hauptfenster.mainloop()

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
        if Settings[0] == 'Dunkel' or Settings[0] == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
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
        else:
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
        
        Buttonback = tk.Button(Hauptfenster, text='← Zurück', command=Fenster.Hauptmenü)
        Buttonback.place(x='25', y='25') # GUI wird platziert
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
        if Settings[0] == 'Dunkel' or Settings[0] == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
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
        else:
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
        for element in Hauptfenster.winfo_children(): # GUI Elemente von anderen Funktionen werden entfernt
            element.destroy()
        Hauptfenster.title('Ligma - Einstellungen')

        global Settings

        Buttonback = tk.Button(Hauptfenster, text='← Zurück', command=Fenster.Hauptmenü)
        Buttonback.place(x='25', y='25')
        LErsch = tk.Label(Hauptfenster,text='Erscheinungsbild')
        LErsch.place(x='120', y='90', anchor='center')
        BErsch = tk.Button(Hauptfenster,text=Settings[0],command=Einstellungen.Erscheinungsbild)
        BErsch.place(x='300', y='90', anchor='center')
        LProg = tk.Label(Hauptfenster,text='Fortschrittsleiste')
        LProg.place(x='120', y='130', anchor='center')
        BProg = tk.Button(Hauptfenster,text=Settings[1],command=Einstellungen.ProgStat)
        BProg.place(x='300', y='130', anchor='center')
        LÖV = tk.Label(Hauptfenster,text='Nach Verschlüsseln öffnen')
        LÖV.place(x='120', y='170', anchor='center')
        BÖV = tk.Button(Hauptfenster,text=Settings[2],command=Einstellungen.OpenVer)
        BÖV.place(x='300', y='170', anchor='center')
        LÖE = tk.Label(Hauptfenster,text='Nach Entschlüsseln öffnen')
        LÖE.place(x='120', y='210', anchor='center')
        BÖE = tk.Button(Hauptfenster,text=Settings[3],command=Einstellungen.OpenEnt)
        BÖE.place(x='300', y='210', anchor='center')
        Default = tk.Button(Hauptfenster,text='Standart Wiederherstellen',command=Einstellungen.Defaultbutton)
        Default.place(x='120', y='260', anchor='center')
        Info = tk.Button(Hauptfenster,text='Info',command=Fenster.Info)
        Info.place(x='300', y='260', anchor='center')

        if Settings[0] == 'Dunkel' or Settings[0] == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
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
        else:
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
1% → Die Fortschrittsleiste wird aktualisiert wenn je 1% des Dokuments ver-/entschlüsselt wurden.
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
Aus → Die App öffnet nichts.''', anchor='w', justify='left')
            Label.place(x='20', y='0')
            if Settings[0] == 'Dunkel' or Settings[0] == 'System' and darkdetect.isDark(): # Darkmode wird eingestellt
                Infofenster.configure(bg='#323232')
                Infofenster.configure(highlightbackground='#323232')
                Label.configure(bg='#323232')
                Label.configure(fg='white')

class Einstellungen:
    '''
    Für die Einstellungen benötigte Funktionen
    '''
    def Default():
        '''
        Stadart wiederherstellen

        Erklärung für Variable Settings:
        [Erscheinungsbild, Status Progressbar, Datei nach Verschlüsseln öffnen, Datei nach Entschlüsseln öffnen]
        '''
        global Settings
        Settings = ['System', 'Ein', 'Fragen', 'Fragen (Datei)']

        Einstellungen.Speichern()

    def Defaultbutton():
        Einstellungen.Default()
        Fenster.Einstellungen()
            
    def Laden():
        '''
        Einstellungen aus Datei laden
        '''
        global Error
        save = True
        if platform.system() == 'Darwin':
            if not os.path.exists(os.path.expanduser("~/Library/Application Support/Ligma/Einstellungen.txt")):
                Einstellungen.Default()
                return None
            else:
                try:
                    datei = open(os.path.expanduser("~/Library/Application Support/Ligma/Einstellungen.txt"), 'r', encoding='utf-8')
                except:
                    Error = 'Einstellungen.txt konnte nicht geöffnet werden'
                    save = False
        elif platform.system() == 'Windows':
            if not os.path.exists(os.path.join(os.environ['APPDATA'],'Ligma')):
                Einstellungen.Default()
                return None
            else:
                try:
                    datei = open(os.path.join(os.environ['APPDATA'],'Ligma\\Einstellungen.txt'), 'r', encoding='utf-8')
                except:
                    Error = 'Einstellungen.txt konnte nicht geöffnet werden'
                    save = False
        else:
            Einstellungen.Default()
            return None

        global Settings
        Settings = [None,None,None,None]
        if save:
            for i in range(4):
                datei.readline()
                Settings[i] = datei.readline().rstrip('\n')
            datei.close()
        Einstellungen.Check()

    def Speichern():
        '''
        Einstellungen in Datei speichern
        '''
        save = True
        global Error
        if platform.system() == 'Darwin':
            if not os.path.exists(os.path.expanduser("~/Library/Application Support/Ligma")):
                try:
                    os.mkdir(os.path.expanduser("~/Library/Application Support/Ligma"))
                except:
                    save = False
                    Error = '[Error: Verzeichnis Ligma konnte nicht erstellt werden]'
            try:
                datei = open(os.path.expanduser("~/Library/Application Support/Ligma/Einstellungen.txt"), 'w', encoding='utf-8')
            except:
                save = False
                Error = '[Error: Einstellungen.txt konnte nicht erstelllt werden]'
        elif platform.system() == 'Windows':
            if not os.path.exists(os.path.join(os.environ['APPDATA'],'Ligma')):
                try:
                    os.mkdir(os.path.join(os.environ['APPDATA'],'Ligma'))
                    print(os.path.join(os.environ['APPDATA'],'Ligma'))
                except:
                    save = False
                    Error = '[Error: Verzeichnis Ligma konnte nicht erstellt werden]'
            try:
                datei = open(os.path.join(os.environ['APPDATA'],'Ligma\\Einstellungen.txt'), 'w', encoding='utf-8')
            except:
                save = False
                Error = '[Error: Einstellungen.txt konnte nicht erstelllt werden]'
        else:
            save = False
            Error = '[Error: Betriebssystem nicht unterstützt/erkannt]'
            
        if save:
            datei.write('Erscheinungsbild (System/Hell/Dunkel)\n' + Settings[0] + '\nProgressbar (Ein/1%/10%/Aus)\n' + Settings[1] + '\nNach Verschlüsseln öffnen (Fragen/Ordner/Aus)\n' + Settings[2] + '\nNach Entschlüsseln öffnen (Fragen (Datei)/Fragen (Ordner)/Datei/Ordner/Aus)\n' + Settings[3])
            datei.close()
            
    def Check():
        '''
        Überprüft, ob in der Datei Unsinn steht und berichtigt gegebenenfalls
        '''
        if not (Settings[0] == 'Hell' or Settings[0] == 'Dunkel'):
            Settings[0] = 'System'
        if not (Settings[1] == '1%' or Settings[1] == '10%' or Settings[1] == 'Aus'):
            Settings[1] = 'Ein'
        if not (Settings[2] == 'Datei' or Settings[2] == 'Ordner' or Settings[2] == 'Aus'):
            Settings[2] = 'Fragen'
        if not (Settings[3] == 'Fragen (Ordner)' or Settings[3] == 'Datei' or Settings[3] == 'Ordner' or Settings[3] == 'Aus'):
            Settings[3] = 'Fragen (Datei)'
        Einstellungen.Speichern()

    def Erscheinungsbild():
        '''
        Anpassen des Erscheinugsbildes
        '''
        global Settings
        
        if Settings[0] == 'System':
            Settings[0] = 'Hell'
        elif Settings[0] == 'Hell':
            Settings[0] = 'Dunkel'
        else:
            Settings[0] = 'System'
        Einstellungen.Speichern()
        Fenster.Einstellungen()
        
    def ProgStat():
        '''
        Anpassen des Status der Fortschritssleiste
        '''
        global Settings
        
        if Settings[1] == 'Ein':
            Settings[1] = '1%'
        elif Settings[1] == '1%':
            Settings[1] = '10%'
        elif Settings[1] == '10%':
            Settings[1] = 'Aus'
        else:
            Settings[1] = 'Ein'
        Einstellungen.Speichern()
        Fenster.Einstellungen()
                    
    def OpenVer():
        '''
        Anpassen von nach Verschlüsseln öffnen
        '''
        global Settings
        
        if Settings[2] == 'Fragen':
            Settings[2] = 'Ordner'
        elif Settings[2] == 'Ordner':
            Settings[2] = 'Aus'
        else:
            Settings[2] = 'Fragen'
        Einstellungen.Speichern()
        Fenster.Einstellungen()

    def OpenEnt():
        '''
        Anpassen von nach Entschlüsseln öffnen
        '''
        global Settings
        
        if Settings[3] == 'Fragen (Datei)':
            Settings[3] = 'Fragen (Ordner)'
        elif Settings[3] == 'Fragen (Ordner)':
            Settings[3] = 'Datei'
        elif Settings[3] == 'Datei':
            Settings[3] = 'Ordner'
        elif Settings[3] == 'Ordner':
            Settings[3] = 'Aus'
        else:
            Settings[3] = 'Fragen (Datei)'
        Einstellungen.Speichern()
        Fenster.Einstellungen()


#=============================Verschlüsseln-Funktionen=============================#

class Verschlüsseln:
    '''
    Für die Verschlüsselung benötigte Funktionen
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
                Verschlüsselbutton['state'] = 'normal' # Aktiviert Versch, wenn beide Dateien ausgewählt wurden
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
                Verschlüsselbutton['state'] = 'normal' # Aktiviert Versch, wenn beide Dateien ausgewählt wurden
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

        if Settings[1] == 'Ein':
            LigmaEinstellungen = [True, True, True]
        elif Settings[1] == '1%':
            LigmaEinstellungen = [True, False, True]
        elif Settings[1] == '10%':
            LigmaEinstellungen = [True, False, False]
        elif Settings[1] == 'Aus':
            LigmaEinstellungen = [False, False, False]
        LigmaEinstellungen.append(Settings[0])

        Anz = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Stärke der Verschlüsselung ein: ', initialvalue=50, minvalue=1) # Frage nach Stärke der Verschlüsselung
        if Anz: # Failsave, wenn der Nutzer bei der Integereingabe auf Cancel drückt
            Text = Ligma.Primaer.Raedern(message, 'v', Anz, Keypfad, LigmaEinstellungen) # Nutzereingaben werden an Ligma weitergegeben zum Verschüsseln

            if Text[0]: # Fals Ligma ein Fehler zurückgibt wird dieser angezeigt. Sonst wird gespeichert
                Savepfad = filedialog.asksaveasfilename(defaultextension='.ball', filetypes=[('Verschlüsselte Dateien', '*.ball')]) # Frage nach Speicherort der verschlüsselten Datei
                if Savepfad: # Failsave, fals Nutzer auf Cancel drückt
                    datei = open(Savepfad, 'w', encoding='utf-8')
                    datei.write(Text[1]) # Speichern
                    datei.close()
                    
                    message = len(message)
                    Anz2 = False
                    Anz2 = simpledialog.askinteger('Verschlüsseln', 'Bitte geben sie die Menge der per Sekundärverschlüsselung hinzugefügten Zeichen ein: ', initialvalue=message//10, minvalue=0) # Frage nach Stärke der Sekundäverschlüsselung. Standartmäßig 10%.
                    if not Anz2:
                        Anz2 = 0
                    Ligma.Sekundaer.Versch(Anz2,Keypfad,Savepfad) # Nutzereingaben werden an LigmaB weitergegeben zum Sekundärverschüsseln
                    messagebox.showinfo('Entschlüsseln', 'Sekundärverschlüsselung abgeschlossen.')
                    if Settings[2] == 'Ordner':
                        if platform.system() == 'Windows':
                            os.startfile(Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)))
                        elif platform.system() == 'Darwin':
                            os.system('open "{}"'.format(Savepfad.rstrip(os.path.basename(Savepfad))))
                        else:
                            messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
                    elif Settings[2] == 'Fragen':
                        if messagebox.askokcancel('Verschlüsseln', 'Möchten Sie den Ordner ' + Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)) + ' öffnen?'):
                            if platform.system() == 'Windows':
                                os.startfile(Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)))
                            elif platform.system() == 'Darwin':
                                os.system('open "{}"'.format(Savepfad.rstrip(os.path.basename(Savepfad))))
                            else:
                                messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
            else:
                messagebox.showerror('Entschlüsseln', Text[1])

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
            if DateiEntpfad and Keypfad: # Aktiviert Entsch, wenn beide Dateien ausgewählt wurden
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
            if Keypfad and DateiEntpfad: # Aktiviert Entsch, wenn beide Dateien ausgewählt wurden
                Entschlüsselbutton['state'] = 'normal'
        except NameError:
            pass

    def Start():
        """
        Wird aktiv, wenn eine Schlüsseldatei und eine Verschlüsselte Datei ausgewählt wurde.
        Entschlüsselt die Datei mit Ligma und LigmaB.
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

        Ligma.Sekundaer.Entsch(Keypfad, DateiEntpfad) # Entschlüsselt die Datei mit Ligma

        datei = open(DateiEntpfad, 'r', encoding='utf-8') # Verschlüsselte Datei wird eingelesen und in ball gespeichert
        ball = ''
        for zeile in datei:
            ball += zeile
        datei.close()

        if Settings[1] == 'Ein':
            LigmaEinstellungen = [True, True, True]
        elif Settings[1] == '1%':
            LigmaEinstellungen = [True, False, True]
        elif Settings[1] == '10%':
            LigmaEinstellungen = [True, False, False]
        elif Settings[1] == 'Aus':
            LigmaEinstellungen = [False, False, False]
        LigmaEinstellungen.append(Settings[0])

        Text = Ligma.Primaer.Raedern(ball, 'e', 0, Keypfad, LigmaEinstellungen) # ball wird entschlüsselt
        if Text[0]: # Fals Ligma ein Fehler zurückgibt wird dieser angezeigt. Sonst wird gespeichert
            Savepfad = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Textdateien', '*.txt')]) # Fragt nach Speicherort
            if Savepfad: # Failsave, fals Cancel
                datei = open(Savepfad, 'w', encoding='utf-8') # Speichert
                datei.write(Text[1])
                datei.close()
                if Settings[3] == 'Ordner':
                    if platform.system() == 'Windows':
                        os.startfile(Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)))
                    elif platform.system() == 'Darwin':
                        os.system('open "{}"'.format(Savepfad.rstrip(os.path.basename(Savepfad))))
                    else:
                        messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
                elif Settings[3] == 'Datei':
                    if platform.system() == 'Windows':
                        os.startfile(Savepfad.replace('/','\\'))
                    elif platform.system() == 'Darwin':
                        os.system('open "{}"'.format(Savepfad))
                    else:
                        messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
                elif Settings[3] == 'Fragen (Datei)':
                    if messagebox.askokcancel('Verschlüsseln', 'Möchten Sie die Datei ' + os.path.basename(Savepfad) + ' öffnen?'):
                        if platform.system() == 'Windows':
                            os.startfile(Savepfad.replace('/','\\'))
                        elif platform.system() == 'Darwin':
                            os.system('open "{}"'.format(Savepfad))
                        else:
                            messagebox.showerror('Verschlüsseln', 'Betriebssystem nicht unterstützt')
                elif Settings[3] == 'Fragen (Ordner)':
                    if messagebox.askokcancel('Verschlüsseln', 'Möchten Sie den Ordner ' + Savepfad.rstrip(os.path.basename(Savepfad)) + ' öffnen?'):
                        if platform.system() == 'Windows':
                            os.startfile(Savepfad.replace('/','\\').rstrip(os.path.basename(Savepfad)))
                        elif platform.system() == 'Darwin':
                            os.system('open "{}"'.format(Savepfad.rstrip(os.path.basename(Savepfad))))
                        else:
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
Einstellungen.Laden()
Fenster.Hauptmenü()