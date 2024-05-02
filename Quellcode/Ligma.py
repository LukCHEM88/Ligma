import random, os, platform, time, darkdetect, threading
import tkinter as tk
from tkinter import ttk, messagebox

#=====================Klassen/Funktionen=====================#

class Primaer(): #TODO: Keydatei verbessern --> Indexe von Zahlen, nicht Zahlen selbst speichern!
    def Codieren(Zeichen: str, Richtung: int) -> str:
        """
        Nimmt ein Zeichen 'Zeichen' und schickt dieses durch alle vorhandenen Räder in die Richtung 'Richtung'.\n
        Zeichen = Zeichen(str), welches (ent-)codiert werden soll\n
        Richtung = Integer(int), welche angibt, ob entschlüsselt oder verschlüsselt wird (0 = entsch.; 1 = versch.)
        """
        global Verschiebung #Einfügen aller globaler Variablen, welche genutzt werden
        global Rad
        global Einzelt
        global Settings

        for Nummer in range(len(Einzelt)): #Wandelt die Variable 'Zeichen' in eine Zahl mittels des Index der Liste 'Einzelt' um
            if Einzelt[Nummer] == Zeichen:
                Zeichen = Nummer
                break

        if (Richtung == 1): #Entschlüsseln
            if (Settings[0] == True):
                Progressbar.setinfo('Zeichen ' + str(ZNummer) + ' von ' + str(ZLaenge) + ' wird entschlüsselt...') #Aktualisierung von Progressbar
            for RNummer in range(len(Rad)): #Zahl wird durch alle Räder entschlüsselt
                Zeichen = (Rad[RNummer][Zeichen] - Verschiebung) % len(Einzelt) #'Zeichen' wird zu Wert des Index 'Zeichen' in einer Liste in der Liste 'Rad' umgewandelt
            Verschiebung = (Verschiebung - 1) % len(Einzelt) #Verschiebung wird in negative Richtung zurück gedreht
        elif (Richtung == 0): #Verschlüsseln
            if (Settings[0] == True):
                Progressbar.setinfo('Zeichen ' + str(ZNummer) + ' von ' + str(ZLaenge) + ' wird verschlüsselt...') #Aktualisierung von Progressbar
            for RNummer in range(len(Rad)): #Zahl wird durch alle Räder verschlüsselt
                Zeichen = Rad[RNummer][(Zeichen + Verschiebung) % len(Einzelt)] #'Zeichen' wird zu Wert des Index 'Zeichen' in einer Liste in der Liste 'Rad' umgewandelt
            Verschiebung = (Verschiebung + 1) % len(Einzelt) #Verschiebung wird in positive Richtung weitergedreht
        return Einzelt[Zeichen]

    def Zufall(Liste: list) -> list:
        """
        Ordnet eine gegebene Liste (relativ) zufällig an.
        """
        for Nummer in range(len(Liste) * 2): #Schleife, welche doppelt so oft wie die zufällig zu sortierende Liste lang ist, sich widerholt
            temp = random.randint(0, len(Liste) - 1) #auswählen und zwichenspeichern zweier Zufallszahlen, welche innerhalb des Index der Liste liegt
            temp2 = random.randint(0, len(Liste) - 1)
            temp3 = Liste[temp] #tauschen der 2 Zahlen von den zufällig ausgewählten Indexen
            Liste[temp] = Liste[temp2]
            Liste[temp2] = temp3
        return Liste

    def Raedern(Zeichenkette = '', Schluesseln = '', AnzahlR = 0, Keydatei = '', Einstellungen = []) -> str:
        """
        Zeichenkette = String(str), der ver-/entschlüsselt werden soll\n
        Schlüsseln = String(str) >> "v/e" --> v = verschlüsseln; e = entschlüsseln\n
        AnzahlR = Anzahl(int) an Rädern, welche beim verschlüsseln genutzt werden sollen\n
        Keydatei = Pfad(str), welcher zum Speicherort der Keydatei führt\n
        Einstellungen = Liste(list) mit Optionen zur Anpassung des Ladebildschirms\n
        für Einstellungen:\n
        --> Aufbau: [Boolean, Integer, String]\n
        --> Inhalt: [Ladebildschirm an/aus,\n
                    {durchgehende Updates --> 1,\n
                    Update jede Sekunde --> 2,\n
                    Update aller 10% --> 3},\n
                    Helligkeit('Dunkel'/'Hell'/'System')]\n
        """
        global Einzelt #Einfügen aller globaler Variablen, welche genutzt werden
        global ZEinzelt
        global Verschiebung
        global Rad
        global ZNummer
        global ZLaenge
        global timer
        global update
        global Settings

        if (Zeichenkette == '') or ((Schluesseln != 'e') and (Schluesseln != 'v')) or ((AnzahlR < 1) and (Schluesseln != 'e')) or (Keydatei == '') or (Einstellungen == []): #Check, ob alle Parameter genügend angegeben sind
            return [False, '[Error: benötigte(r) Parameter nicht vorhanden]']

        Verschiebung = 0 #Initialisierung von benötigten Variablen
        timer = 0
        update = 0
        ZLaenge = len(Zeichenkette)
        ZEinzelt = []
        Rad = []
        Settings = Einstellungen

        if (Settings[1] == 2):
            Thread = threading.Thread(target = Progressbar.update, args = ())

        Einzelt = []
        for Element in Zeichenkette: #Schreibt alle in der gegebenen Zeichenkette vorkommenden verschiedenen Zeichen in die Liste 'Einzelt'.
            if not Element in Einzelt:
                Einzelt.append(Element)
        Einzelt.sort()

        if (Schluesseln == 'e'): #Einzelt-Variable definieren und kontrollieren + Kontrolle, ob Key- und (*.ball)-Datei übereinstimmen können
            if os.path.exists(Keydatei):
                try:
                    Datei = open(Keydatei, 'r', -1, 'utf-8')
                except: 
                    return [False, '[Error: Keydatei kann nicht geöffnet werden]']
            else:
                return [False, '[Error: Keydatei wurde nicht gefunden]']
            Kontrolle = Einzelt.copy()
            Einzelt = eval(Datei.readline())
            Datei.close()

            for Zeichen in Kontrolle:
                temp = False
                for Zeichen1 in Einzelt:
                    if (Zeichen1 == Zeichen):
                        temp = True
                        break
                if (temp == False):
                    return [False, '[Error: (*.lig)-Datei und (*.ball)-Datei nicht kompatibel]']

        for i in range(len(Einzelt)):
                ZEinzelt.append(i)

        if (Schluesseln == 'v'):
            if (Settings[0] == True): #erstellen der Progressbar (falls in Einstellungen aktiviert) und starten eines Threads (falls 'jede Sekunde aktualisieren' in Einstellungen eingestellt)
                Progressbar.erstellen()
                if (Settings[1] == 2):
                    update = 1
                    Thread.start()
                Progressbar.setinfo('Verschlüsselung wird initiiert...')
            
            for i in range(AnzahlR): #Räder hinzufügen und Zahlen zufällig anordnen
                Rad.append(ZEinzelt.copy())
                Rad[i] = Primaer.Zufall(Rad[i])

            ZS = '' #initialisieren der Variablen für Verschlüsselung
            ZNummer = 0
            Zaehler = 0
            Aktual = 100 / ZLaenge
            ProgStat = 0
            time1 = time.time()
            for Zeichen1 in Zeichenkette: #Verschlüsselung von Zeichenkette 'Zeichenkette', verschlüsselte Version wird in Zeichenkette 'ZS' gespeichert
                ZNummer += 1
                ZS += Primaer.Codieren(Zeichen1, 0)
                
                Zaehler += Aktual
                if (ProgStat != int(Zaehler)) and (Settings[0] == True):
                    ProgStat = int(Zaehler)
                    time2 = time.time()
                    timer = int(((time2 - time1) / int(Zaehler)) * (100 - int(Zaehler)))
                    if ((Settings[1] == 3) and (int(Zaehler) % 10 == 0)) or (Settings[1] != 3): #setzt Progressbar bei bestimmten Konditionen
                        Progressbar.setprogress(int(Zaehler))

            if (Settings[0] == True): #Schließen von Progressbar
                if (Settings[1] == 2): #Schließen von extra Thread
                    update = 0
                    Thread.join()

                Progressbar.setprogress(100)
                Progressbar.setinfo('Die Datei wurde erfolgreich verschlüsselt.')
                ProgWindow.update()
                time.sleep(0.1)
                Progressbar.fertig()

            Verschiebung = Verschiebung % len(Einzelt)

            try: #speichern der verschlüsselten Datei
                Datei = open(Keydatei, 'w', -1, 'utf-8')
            except:
                return [False, '[Error: Keydatei kann nicht überschrieben/erstellt werden]']
            Datei.write(str(Einzelt) + '\n')
            for i in range(len(Rad)):
                Datei.write(str(Rad[i]) + '\n')
            Datei.write(str(Verschiebung))
            Datei.close()

            return [True, ZS]
        elif (Schluesseln == 'e'):
            if (Settings[0] == True): #erstellen der Progressbar (falls in Einstellungen aktiviert) und starten eines Threads (falls 'jede Sekunde aktualisieren' in Einstellungen eingestellt)
                Progressbar.erstellen()
                if (Settings[1] == 2):
                    update = 1
                    Thread.start()
                Progressbar.setinfo('Entschlüsselung wird initiiert......')
                
            Datei = open(Keydatei, 'r', -1, 'utf-8') #Räder aus Key-Datei herauslesen und in 'Rad' speichern
            temp = -1
            for line in Datei.readlines():
                if (line[0] == '[') and (line[1] != "'"):
                    Rad.append(eval(line))
                elif (line[0] != '['):
                    Verschiebung = int(line.rstrip()) % len(Einzelt) - 1
                    temp += 1
            Datei.close()

            if (temp > 0): #Kontrolle, ob Datei noch sekundärverschlüsselt
                return [False, '[Error: Datei noch Sekundaerverschluesselt]']
            
            Rad_temp = [] #Umschreiben der Variable 'Rad', damit abgerufene einer Zahl den benötigten Index (bei der sie im Original liegt) bei Entschlüsselung ausgibt
            for i in Rad[0]:
                Rad_temp.append(0)
            for i in range(len(Rad)):
                for l in range(len(Rad[i])):
                    Rad_temp[Rad[i][l]] = l
                Rad[i] = Rad_temp.copy()

            Rad = Rad[::-1]

            ZS = '' #initialisieren der Variablen für Entschlüsselung
            ZNummer = 0
            Zaehler = 0
            Aktual = 100 / ZLaenge
            ProgStat = 0
            time1 = time.time()
            for Zeichen1 in Zeichenkette[::-1]: #Entschlüsselung von Zeichenkette 'Zeichenkette', verschlüsselte Version wird in Zeichenkette 'ZS' gespeichert
                ZNummer += 1
                ZS += Primaer.Codieren(Zeichen1, 1)
                
                Zaehler += Aktual
                if (ProgStat != int(Zaehler)) and (Settings[0] == True):
                    ProgStat = int(Zaehler)
                    time2 = time.time()
                    timer = int(((time2 - time1) / int(Zaehler)) * (100 - int(Zaehler)))
                    if ((Settings[1] == 3) and (int(Zaehler) % 10 == 0)) or (Settings[1] != 3): #setzt Progressbar bei bestimmten Konditionen
                        Progressbar.setprogress(int(Zaehler))

            if (Settings[0] == True): #Schließen von Progressbar
                if (Settings[1] == 2): #Schließen von extra Thread
                    update = 0
                    Thread.join()

                Progressbar.setprogress(100)
                Progressbar.setinfo('Die Datei wurde erfolgreich entschlüsselt.')
                ProgWindow.update()
                time.sleep(0.1)
                Progressbar.fertig()

            return [True, ZS[::-1]]

class Sekundaer(Primaer):
    def Versch(Anzahl: int, Keydatei: str, Balldatei: str) -> bool:
        """
        Schreibt eine bestimmte Anzahl an zufälligen Zeichen in eine Datei, welche durch die Schlüsseldatei wieder rückgängig gemacht werden kann.\n
        Anzahl = Anzahl(int) der zufälligen Zeichen angibt\n
        Keydatei = Pfad(str), welcher zur benötigten Key-Datei führt\n
        Zieldatei = Pfad(str), welcher zur benötigten (*.ball)-Datei führt
        """
        if (Anzahl < 0): #Umkehrung der Variable 'Anzahl', falls diese negativ ist
            Anzahl = -Anzahl
        if (not os.path.exists(Keydatei)) or (not os.path.exists(Balldatei)) or (Anzahl < 1): #Kontrolle, ob alle Parameter korrekt angegeben wurden
            return False

        Ergebnis = '' #speichern des Inhalts der angegeben Key-Datei in Variable 'Ergebnis'
        try:
            Datei = open(Keydatei, 'r', -1, 'utf-8')
        except:
            return False
        repeat = -1
        for Zeile in Datei.readlines():
            Ergebnis += Zeile
            if (Zeile[0] != '[') and (repeat < 0):
                temp = len(Ergebnis) - len(Zeile)
                repeat += 1
        Datei.close()

        Ergebnis2 = '' #speichern des Inhalts der angegeben (*.ball)-Datei in Variable 'Ergebnis2'
        try:
            Datei = open(Balldatei, 'r', -1, 'utf-8')
        except:
            return False
        for Zeile in Datei.readlines():
            Ergebnis2 += Zeile
        Datei.close()

        random.seed(Ergebnis, 2) #Seed festlegen und hinzufügen von zufälligen Zeichen in Variable 'Ergebnis2'

        for i in range(Anzahl):
            Zahl = random.randint(0, len(Ergebnis2) - 1)
            Zahl2 = random.randint(0, len(Ergebnis2) - 1)
            Ergebnis2 = Ergebnis2[0:Zahl] + Ergebnis2[Zahl2] + Ergebnis2[Zahl:len(Ergebnis2)]

        try: #speichern der modifizierten Key-Datei
            Datei = open(Keydatei, 'w', -1, 'utf-8')
        except:
            return False
        Datei.writelines(Ergebnis[0:temp] + str(Anzahl) + '\n' + Ergebnis[temp::])
        Datei.close()

        try: #speichern der modifizierten (*.ball)-Datei
            Datei = open(Balldatei, 'w', -1, 'utf-8')
        except:
            return False
        Datei.writelines(Ergebnis2)
        Datei.close()

        return True

    def Entsch(Keydatei: str, Balldatei: str) -> bool:
        """
        Löscht eine bestimmte Anzahl an zufälligen Zeichen in eine Datei, welche mit der Schlüsseldatei bestimmt werden können.\n
        Keydatei = Pfad(str), welcher zur benötigten Key-Datei führt\n
        Zieldatei = Pfad(str), welcher zur benötigten (*.ball)-Datei führt
        """
        if (not os.path.exists(Keydatei)) or (not os.path.exists(Balldatei)): #Kontrolle, ob alle Parameter korrekt angegeben wurden
            return False

        Ergebnis2 = '' #Initialisierung von Variablen
        Anzahl_Sek = -1
        Inhalt_Keydatei = []

        try: #speichern des Inhalts der angegeben Key-Datei in Liste 'Inhalt_Keydatei' und herausspeichern der Anzahl von Sekundärverschlüsselungen in Variable 'Anzahl_Sek'
            Datei = open(Keydatei, 'r', -1, 'utf-8')
        except:
            return False
        for Zeile in Datei.readlines():
            Inhalt_Keydatei.append(Zeile)
            if (Zeile[0] != '['):
                        Anzahl_Sek += 1    
        Datei.close()

        if (Anzahl_Sek < 1): #Beendung des Programms, wenn keine Sekundärverschlüsselung vorhanden ist
            return True

        try: #speichern des Inhalts der angegeben (*.ball)-Datei in Variable 'Ergebnis2'
            Datei = open(Balldatei, 'r', -1, 'utf-8')
        except:
            return False
        for Zeile in Datei.readlines():
            Ergebnis2 += Zeile
        Datei.close()

        for i2 in range(Anzahl_Sek): #Widerholung von Entschlüsselung, bis alle Sekundärverschlüsselungen entfernt sind

            temp2 = [] #speichern der Anzahl der Zeichen, welche in derzeitigem Entschlüsselungszyklus entfernt werden müssen in Variable 'Anzahl_Zei' und Aktualisierung der Liste 'Inhalt_Keydatei' und Variable 'Ergebnis' auf derzeitigen Entschlüsselungszyklus
            Anzahl_Zei = -1
            Ergebnis = ''
            for Zeile in Inhalt_Keydatei:
                if (Zeile[0] != '[') and (Anzahl_Zei == -1):
                    Anzahl_Zei = int(Zeile)
                    if (Anzahl_Zei < 1):
                        return False
                else:
                    Ergebnis += Zeile
                    temp2.append(Zeile)
            Inhalt_Keydatei = temp2

            random.seed(Ergebnis, 2) #Seed festlegen und entfernen von bestimmten, zuvor zufälligen, Zeichen in Variable 'Ergebnis2'

            Zahl = [] #Entschlüsselung (Rückgängig-Machung von Verschlüsselungsverfahlen (dieselben Angaben, aber alles Rückwärts (klingt einfach, ist kompliziert)))
            for i in range(Anzahl_Zei)[::-1]:
                Zahl.append(random.randint(0, len(Ergebnis2) - 2 - i))
                random.randint(0, len(Ergebnis2) - 2 - i)
            Zahl = Zahl[::-1]
            for Zahli in Zahl:
                Ergebnis2 = Ergebnis2[0:Zahli] + Ergebnis2[Zahli + 1:len(Ergebnis2)]

        try: #speichern der modifizierten Key-Datei
            Datei = open(Keydatei, 'w', -1, 'utf-8')
        except:
            return False
        Datei.writelines(Ergebnis)
        Datei.close()

        try: #speichern der modifizierten (*.ball)-Datei
            Datei = open(Balldatei, 'w', -1, 'utf-8')
        except:
            return False
        Datei.writelines(Ergebnis2)
        Datei.close()

        return True

class Progressbar(Primaer):
    def erstellen() -> None:
        """
        erstellt ein Fenster, welches einen Fortschrittsbalken mit kleinen extras anzeigt
        """
        global ProgWindow
        global ProgBar
        global ProgLabel
        global InfoLabel
        global WindowAliveCheck
        global Settings

        ProgWindow = tk.Tk()
        ProgWindow.title('Ligma')
        ProgWindow.resizable('False', 'False')
        ProgWindow.geometry('300x100')

        if (platform.system() == 'Windows'): #Wenn Ligma auf Windows ausgeführt wird, wird versucht das Icon zu öffnen
            if os.path.exists('Icon_Ligma.ico'):
                ProgWindow.iconbitmap('Icon_Ligma.ico')

        ProgBar = ttk.Progressbar(ProgWindow, orient = 'horizontal', length = 200, mode = 'determinate') #Objekte werden generiert und plaziert
        ProgBar.place(x = '150', y = '50', anchor = 'center')
        ProgLabel = tk.Label(ProgWindow, text = '0%')
        ProgLabel.place(x = '150', y = '25', anchor = 'center')
        InfoLabel = tk.Label(ProgWindow, text = 'Initialisierung...')
        InfoLabel.place(x = '150', y = '75', anchor = 'center')

        if (darkdetect.isDark() and (Settings[2] != 'Hell')) or (Settings[2] == 'Dunkel'): # Darkmode wird eingestellt
            # TODO: Window Border
            ProgWindow.configure(bg = '#323232')
            ProgWindow.configure(highlightbackground = '#323232')
            #style = ttk.Style()
            #style.configure("my.Horizontal.TProgressbar", background = "#323232")
            #ProgBar.configure(style = 'my.Horizontal.TProgressbar')
            # FIXME: Hintergrund PB Mac
            ProgLabel.configure(bg = '#323232')
            ProgLabel.configure(fg = 'white')
            InfoLabel.configure(bg = '#323232')
            InfoLabel.configure(fg = 'white')
        
        WindowAliveCheck = True
        ProgWindow.update()

    def setprogress(Fortschritt: int) -> None:
        """
        setzt den Wert des Fortschrittsbalkens via der Variable 'Fortschritt'
        Fortschritt: Integer(int), welche den Fortschritt in Prozent angibt
        """
        global WindowAliveCheck
        global timer
        global Settings
        Minuten = timer // 60 #rechnet Minuten und Sekunden aus
        Sekunden = timer - (Minuten * 60)
        try:
            ProgBar['value'] = Fortschritt #Progressbar wird geupdated auf derzeitigen Fortschritt
            ProgLabel['text'] = str(Fortschritt) + '% (' + str(Minuten) + 'm ' + str(Sekunden) + 's)' #vermutete Zeit bis Fertigstellung von ver- / entschlüsselung wird mit Fortschritt in Prozent angezeigt
            if (Settings[1] == 3):
                ProgWindow.update()
        except:
            Progressbar.FensterGeschlossen()

    def setinfo(Text: str) -> None:
        """
        setzt den Infotext des Fensters auf 'Text' und updated das Fenster in bestimmten Einstellungen
        Text: String(str), welcher auf das Label 'InfoLabel' plaziert wird
        """
        global WindowAliveCheck
        global Settings
        global update
        try:
            InfoLabel['text'] = Text
            if (Settings[1] == 1): #wird nur in Einstellung '1' (update bei jeder Zeichen ver- oder entschlüsselung) aufgerufen - updated das Fenster
                ProgWindow.update()
        except:
            Progressbar.FensterGeschlossen()

        if (update == 2): #wird nur in Einstellung '2' (update jede Sekunde) aufgerufen - updated das Fenster
            update = 1
            ProgWindow.update()

    def fertig() -> None:
        """
        versucht das Fenster zu schließen
        """
        global WindowAliveCheck
        try:
            ProgWindow.destroy()
        except:
            Progressbar.FensterGeschlossen()

    def update() -> None:
        """
        Wird in einem Thread ausgeführt und verändert die Variable 'update' alle jede Sekunde.
        """
        global update
        while (update > 0): #setzt den Wert der Variable 'update' auf integer '2' jede Sekunde, wird nur in threading ausgeführt und kann mit 'update = 0' deaktiviert werden
            update = 2
            time.sleep(1)

    def FensterGeschlossen() -> None:
        """
        falls das Fenster bereits geschlossen wurde, wird diese Nachricht sich einmal aufrufen
        """
        if WindowAliveCheck:
                messagebox.showinfo('Ligma', 'Sie haben die Fortschrittsleiste geschlossen.\nLigma wird im Hintergrund weiterarbeiten.')
                WindowAliveCheck = False