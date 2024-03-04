import random
import os

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
            for RNummer in range(len(Rad)):
                for i in range(len(Einzelt)):
                    if Rad[RNummer][i] == Zeichen:
                        Zeichen = (i - Verschiebung) % len(Einzelt)
                        break
            Verschiebung = (Verschiebung - 1) % len(Einzelt)
        elif (Richtung == 0):
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

        if (Zeichenkette == '') or ((Schluesseln != 'e') and (Schluesseln != 'v')) or ((AnzahlR < 1) and (Schluesseln != 'e')) or (Keydatei == ''): #Check, ob alle Parameter genügend angegeben sind
            return '[Error: benötigte(r) Parameter nicht vorhanden]'

        Verschiebung = 0
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
                    return '[Error: Keydatei kann nicht geöffnet werden]'
            else:
                return '[Error: Keydatei wurde nicht gefunden]'
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
                    return '[Error: (*.lig)-Datei und (*.ball)-Datei nicht kompatibel]'

        for i in range(len(Einzelt)):
                ZEinzelt.append(i)

        if (Schluesseln == 'v'): #Räder hinzufügen, Zeichenkette verschlüsseln, 'Rad' kürzen, Key-Datei speichern (+ Kontrolle) und verschlüsselter Text zurückgeben
            for i in range(AnzahlR):
                Rad.append(ZEinzelt.copy())
                Rad[i] = Primaer.Zufall(Rad[i])

            ZS = ''
            for Zeichen1 in Zeichenkette:
                ZS += Primaer.Codieren(Zeichen1, 0)

            Verschiebung = Verschiebung % len(Einzelt)

            try:
                Datei = open(Keydatei, 'w', -1, 'utf-8')
            except:
                return '[Error: Keydatei kann nicht überschrieben/erstellt werden]'
            Datei.write(str(Einzelt) + '\n')
            for i in range(len(Rad)):
                Datei.write(str(Rad[i]) + '\n')
            Datei.write(str(Verschiebung))
            Datei.close()

            return ZS
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
                return '[Error: Datei noch Sekundaerverschluesselt]'

            Rad = Rad[::-1]

            ZS = ''
            for Zeichen1 in Zeichenkette[::-1]:
                ZS += Primaer.Codieren(Zeichen1, 1)
            return ZS[::-1]

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
        for Zeile in Datei.readlines():
            Ergebnis += Zeile
            if (Zeile[0] != '['):
                temp = len(Ergebnis) - len(Zeile)
        Datei.close()

        Ergebnis2 = '' #speichern des Inhalts der angegeben (*.ball)-Datei in Variable 'Ergebnis2'
        try:
            Datei = open(Balldatei, 'r', -1, 'utf-8')
        except:
            return False
        for Zeile in Datei.readlines():
            Ergebnis2 += Zeile
        Datei.close()

        random.seed(Ergebnis) #Seed festlegen und hinzufügen von zufälligen Zeichen in Variable 'Ergebnis2'
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
        Keydatei = string/Pfad, welcher zur benötigten Key-Datei führt\n
        Zieldatei = string/Pfad, welcher zur benötigten (*.ball)-Datei führt
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

        random.seed(Ergebnis) #Seed festlegen und entfernen von bestimmten, zuvor zufälligen, Zeichen in Variable 'Ergebnis2'
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


#=====================Beispiele für Implementierung und Tests=====================#
'''
Ergebnis = ''
Datei = open('C:\\Python\\Ligma\\Core\\test.txt', 'r', -1, 'utf-8') #speichert gesamten Inhalt von 'test.txt' in Variable 'Ergebnis'
for zeile in Datei.readlines():
    Ergebnis += zeile
Datei.close()

Ergebnis = Primaer.Raedern(Ergebnis, 'v', 2000, 'C:\\Python\\Ligma\\Core\\Key.lig') #siehe Funktionsbeschreibung und angegebene Parameter
print(Ergebnis)

Datei = open('C:\\Python\\Ligma\\Core\\test.ball', 'w', -1, 'utf-8') #speichert zuvor verschlüsselten Text in Datei 'test.ball'
Datei.write(Ergebnis)
Datei.close()

Sekundaer.Versch(27, 'C:\\Python\\Ligma\\Core\\Key.lig', 'C:\\Python\\Ligma\\Core\\test.ball') #Hinzufügen einer Sekundärverschlüsselung zum Testen

print(Sekundaer.Entsch('C:\\Python\\Ligma\\Core\\Key.lig', 'C:\\Python\\Ligma\\Core\\test.ball')) #Entfernung der Sekundärverschlüsselung

Ergebnis = ''
Datei = open('C:\\Python\\Ligma\\Core\\test.ball', 'r', -1, 'utf-8') #speichert gesamten Inhalt von 'test.ball' in Variable 'Ergebnis'
for zeile in Datei.readlines():
    Ergebnis += zeile
Datei.close()

Ergebnis = Primaer.Raedern(Ergebnis, 'e', 0, 'C:\\Python\\Ligma\\Core\\Key.lig') #siehe Funktionsbeschreibung und angegebene Parameter
print(Ergebnis)
'''