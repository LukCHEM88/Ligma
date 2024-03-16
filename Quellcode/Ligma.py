import random, os, platform, time, darkdetect
import tkinter as tk
from tkinter import ttk, messagebox

#=====================Klassen/Funktionen=====================#

class Primaer():
    def Codieren(Zeichen: str, Richtung: int) -> str:
        """
        Nimmt ein Zeichen und schickt dieses durch 'Anzahl' viele Räder in die Richtung 'Richtung'.\n
        Zeichen = Zeichen(str), welches (ent-)codiert werden soll\n
        Richtung = Bit(int), welches angibt, ob entschlüsselt oder verschlüsselt wird (0 = entsch.; 1 = versch.)
        """
        global Verschiebung
        global Rad
        global Einzelt

        for Nummer in range(len(Einzelt)): #Wandelt die Variable 'Zeichen' in eine Zahl mittels des Index der Liste 'Einzelt' um
            if Einzelt[Nummer] == Zeichen:
                Zeichen = Nummer
                break

        if (Richtung == 1):
            Progressbar.setinfo('Zeichen ' + str(ZNummer) + ' von ' + str(ZLaenge) + ' wird entschlüsselt...')
            for RNummer in range(len(Rad)):
                for i in range(len(Einzelt)):
                    if Rad[RNummer][i] == Zeichen:
                        Zeichen = (i - Verschiebung) % len(Einzelt)
                        break
            Verschiebung = (Verschiebung - 1) % len(Einzelt)
        elif (Richtung == 0):
            Progressbar.setinfo('Zeichen ' + str(ZNummer) + ' von ' + str(ZLaenge) + ' wird verschlüsselt...')
            for RNummer in range(len(Rad)):
                Zeichen = Rad[RNummer][(Zeichen + Verschiebung) % len(Einzelt)] #Zahl, welche in Variable 'Zeichen' gespeichert is wird 'gerädert' in positive Richtung via des Mechanismus der Enigma
            Verschiebung = (Verschiebung + 1) % len(Einzelt) #Rad, welches genutzt wurde, wird in positive Richtung weitergedreht
        return Einzelt[Zeichen]

    def Zufall(Liste: list) -> list:
        """
        Ordnet eine gegebene Liste (relativ) zufällig an.
        """
        for Nummer in range(len(Liste) * 2):
            temp = random.randint(0, len(Liste) - 1)
            temp2 = random.randint(0, len(Liste) - 1)
            temp3 = Liste[temp]
            Liste[temp] = Liste[temp2]
            Liste[temp2] = temp3
        return Liste

    def Raedern(Zeichenkette = '', Schluesseln = '', AnzahlR = 0, Keydatei = '') -> str:
        """
        Zeichenkette = String, der ver-/entschlüsselt werden soll \n
        Schlüsseln = v/e --> v = verschlüsseln; e = entschlüsseln \n
        AnzahlR = Anzahl an Rädern, welche beim verschlüsseln genutzt werden sollen \n
        Keydatei1 = Pfad, welcher zum Speicherort der Keydatei führt
        """
        global Einzelt
        global ZEinzelt
        global Verschiebung
        global Rad
        global ZNummer
        global ZLaenge

        if (Zeichenkette == '') or ((Schluesseln != 'e') and (Schluesseln != 'v')) or ((AnzahlR < 1) and (Schluesseln != 'e')) or (Keydatei == ''): #Check, ob alle Parameter genügend angegeben sind
            return [False, '[Error: benötigte(r) Parameter nicht vorhanden]']

        Verschiebung = 0
        ZLaenge = len(Zeichenkette)
        ZEinzelt = []
        Rad = []

        Einzelt = []
        for Element in Zeichenkette: #Schreibt alle in der gegebenen Zeichenkette vorkommenden verschiedenen Zeichen in die Liste 'Einzelt'.
            if not Element in Einzelt:
                Einzelt.append(Element)
        Einzelt.sort()

        if (Schluesseln == 'e'): #Einzelt-Variable definieren und kontrollieren
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

        if (Schluesseln == 'v'): #Räder hinzufügen, Zeichenkette verschlüsseln, 'Rad' kürzen, Key-Datei speichern (+ Kontrolle) und verschlüsselter Text zurückgeben
            for i in range(AnzahlR):
                Rad.append(ZEinzelt.copy())
                Rad[i] = Primaer.Zufall(Rad[i])

            Progressbar.erstellen()

            ZS = ''
            Zaehler = 0
            Aktual = 100 / ZLaenge
            for Zeichen1 in Zeichenkette:
                ZNummer = Zeichen1
                ZS += Primaer.Codieren(Zeichen1, 0)
                Zaehler += Aktual
                Progressbar.setprogress(int(Zaehler))

            Verschiebung = Verschiebung % len(Einzelt)

            try:
                Datei = open(Keydatei, 'w', -1, 'utf-8')
            except:
                return [False, '[Error: Keydatei kann nicht überschrieben/erstellt werden]']
            Datei.write(str(Einzelt) + '\n')
            for i in range(len(Rad)):
                Datei.write(str(Rad[i]) + '\n')
            Datei.write(str(Verschiebung))
            Datei.close()

            Progressbar.setinfo('Die Datei wurde erfolgreich verschlüsselt.')
            time.sleep(0.1)
            Progressbar.fertig()

            return [True, ZS]
        elif (Schluesseln == 'e'): #Räder aus Key-Datei herauslesen und in 'Rad' speichern, Zeichenkette dekodieren und entschlüsselter Text zurückgeben
            Datei = open(Keydatei, 'r', -1, 'utf-8')
            temp = -1
            for line in Datei.readlines():
                if (line[0] == '[') and (line[1] != "'"):
                    Rad.append(eval(line))
                elif (line[0] != '['):
                    Verschiebung = int(line.rstrip()) % len(Einzelt) - 1
                    temp += 1
            Datei.close()

            if (temp > 0):
                return [False, '[Error: Datei noch Sekundaerverschluesselt]']

            Rad = Rad[::-1]

            Progressbar.erstellen()

            ZS = ''
            Zaehler = 0
            Aktual = 100 / ZLaenge
            for Zeichen1 in Zeichenkette[::-1]:
                ZNummer = Zeichen1
                ZS += Primaer.Codieren(Zeichen1, 1)
                Zaehler += Aktual
                Progressbar.setprogress(int(Zaehler))
            
            Progressbar.setinfo('Die Datei wurde erfolgreich entschlüsselt.')
            time.sleep(0.1)
            Progressbar.fertig()

            return [True, ZS[::-1]]

class Sekundaer(Primaer):
    def EntschAll(Keydatei: str, Balldatei: str) -> bool:
        """
        Entfernt alle Sekundärverschlüsselungen auf einer angegebenen (*.ball)-Datei\n
        Keydatei = Pfad(str), welcher zur benötigten Key-Datei führt\n
        Zieldatei = Pfad(str), welcher zur benötigten (*.ball)-Datei führt
        """
        if (os.path.exists(Balldatei) and os.path.exists(Keydatei)):
            temp = -1
            try:
                Datei = open(Keydatei, 'r', -1, 'utf-8')
            except:
                return [False, '[Error: Keydatei konnte nicht geoeffnet werden]']
            for Zeile in Datei.readlines():
                    if (Zeile[0] != '['):
                        temp += 1
            Datei.close()

            for i in range(temp):
                Sekundaer.Entsch(Keydatei, Balldatei)
        else:
            return [False, '[Error: benötigte(r) Parameter falsch oder nicht vorhanden]']

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

        Ergebnis = '' #speichern des Inhalts der angegeben Key-Datei in Variable 'Ergebnis' und herausspeichern der Variable 'Anzahl' aus Key-Datei
        Anzahl = -1
        try:
            Datei = open(Keydatei, 'r', -1, 'utf-8')
        except:
            return False
        for Zeile in Datei.readlines():
            if (Zeile[0] != '[') and (Anzahl == -1):
                Anzahl = int(Zeile)
                if (Anzahl < 1):
                    return False
            else:
                Ergebnis += Zeile
        Datei.close()

        Ergebnis2 = '' #speichern des Inhalts der angegeben (*.ball)-Datei in Variable 'Ergebnis2'
        try:
            Datei = open(Balldatei, 'r', -1, 'utf-8')
        except:
            return False
        for Zeile in Datei.readlines():
            Ergebnis2 += Zeile
        Datei.close()

        random.seed(Ergebnis, 2) #Seed festlegen und entfernen von bestimmten, zuvor zufälligen, Zeichen in Variable 'Ergebnis2'

        Zahl = []
        for i in range(Anzahl)[::-1]:
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

class Progressbar():
    def erstellen():
        """
        Erstellt ein Fenster, welches die einen Fortschrittsbalken zeigt.
        """
        global ProgWindow
        global ProgBar
        global ProgLabel
        global InfoLabel
        global WindowAliveCheck

        ProgWindow = tk.Tk()
        ProgWindow.title('Datei wird verschlüsselt...')
        ProgWindow.resizable('False', 'False')
        ProgWindow.geometry('300x100')
        if (platform.system() == 'Windows'): # Wenn Ligma auf Windows ausgeführt wird, wird versucht das Icon zu öffnen
            if os.path.exists('Icon_Ligma.ico'):
                ProgWindow.iconbitmap('Icon_Ligma.ico')

        ProgBar = ttk.Progressbar(ProgWindow, orient = 'horizontal', length = 200, mode = 'determinate')
        ProgBar.place(x = '150', y = '50', anchor = 'center')
        ProgLabel = tk.Label(ProgWindow, text = '0%')
        ProgLabel.place(x = '150', y = '25', anchor = 'center')
        InfoLabel = tk.Label(ProgWindow, text = 'Initialisierung...')
        InfoLabel.place(x = '150', y = '75', anchor = 'center')

        if darkdetect.isDark(): # Darkmode wird eingestellt
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

    def setprogress(x):
        """
        Setzt den Wert des Fortschrittsbalkens
        """
        global WindowAliveCheck
        try:
            ProgBar['value'] = x
            ProgLabel['text'] = str(x) + '%'
        except:
            if WindowAliveCheck:
                messagebox.showinfo('Ligma', 'Sie haben die Fortschrittsleiste geschlossen.\nLigma wird im Hintergrund weiterarbeiten.')
                WindowAliveCheck = False

    def setinfo(x):
        """
        Setzt den Info Text
        """
        global WindowAliveCheck
        try:
            InfoLabel['text'] = x
            ProgWindow.update()
        except:
            if WindowAliveCheck:
                messagebox.showinfo('Ligma', 'Sie haben die Fortschrittsleiste geschlossen.\nLigma wird im Hintergrund weiterarbeiten.')
                WindowAliveCheck = False

    def fertig():
        """
        Schliesst das Fenster
        """
        global WindowAliveCheck
        try:
            ProgWindow.destroy()
        except:
            if WindowAliveCheck:
                messagebox.showinfo('Ligma', 'Sie haben die Fortschrittsleiste geschlossen.\nLigma wird im Hintergrund weiterarbeiten.')
                WindowAliveCheck = False


#=====================Beispiele für Implementierung und Tests=====================#
'''
Ergebnis3 = ''
Datei = open('C:\\Python\\Ligma\\Core\\test.txt', 'r', -1, 'utf-8') #speichert gesamten Inhalt von 'test.txt' in Variable 'Ergebnis'
for zeile in Datei.readlines():
    Ergebnis3 += zeile
Datei.close()

Ergebnis3 = Primaer.Raedern(Ergebnis3, 'v', 2000, 'C:\\Python\\Ligma\\Core\\Key.lig') #siehe Funktionsbeschreibung und angegebene Parameter
print(Ergebnis3)

Datei = open('C:\\Python\\Ligma\\Core\\test.ball', 'w', -1, 'utf-8') #speichert zuvor verschlüsselten Text in Datei 'test.ball'
Datei.write(Ergebnis3)
Datei.close()

Sekundaer.Versch(27, 'C:\\Python\\Ligma\\Core\\Key.lig', 'C:\\Python\\Ligma\\Core\\test.ball') #Hinzufügen einer Sekundärverschlüsselung zum Testen
Sekundaer.Versch(28, 'C:\\Python\\Ligma\\Core\\Key.lig', 'C:\\Python\\Ligma\\Core\\test.ball') #Hinzufügen einer Sekundärverschlüsselung zum Testen
Sekundaer.Versch(985, 'C:\\Python\\Ligma\\Core\\Key.lig', 'C:\\Python\\Ligma\\Core\\test.ball') #Hinzufügen einer Sekundärverschlüsselung zum Testen
Sekundaer.EntschAll('C:\\Python\\Ligma\\Core\\Key.lig', 'C:\\Python\\Ligma\\Core\\test.ball') #Entfernung der Sekundärverschlüsselung

Ergebnis3 = ''
Datei = open('C:\\Python\\Ligma\\Core\\test.ball', 'r', -1, 'utf-8') #speichert gesamten Inhalt von 'test.ball' in Variable 'Ergebnis'
for zeile in Datei.readlines():
    Ergebnis3 += zeile
Datei.close()

Ergebnis3 = Primaer.Raedern(Ergebnis3, 'e', 0, 'C:\\Python\\Ligma\\Core\\Key.lig') #siehe Funktionsbeschreibung und angegebene Parameter
print(Ergebnis3)
'''