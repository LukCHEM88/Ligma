import random
import os
import LigmaB

#=====================Funktionen=====================#

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

def Raedern(Zeichenkette = '', Schluesseln = '', AnzahlR = 0, Keydatei = '', Balldatei = '') -> str:
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

    #Zeichenkettetmp = ''
    #datei = open(Zeichenkette, 'r', encoding='utf-8')
    #for zeile in datei:
    #    Zeichenkettetmp += zeile
    #Zeichenkette = Zeichenkettetmp
    #datei.close()

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
            Rad[i] = Zufall(Rad[i])

        ZS = ''
        for Zeichen1 in Zeichenkette:
            ZS += Codieren(Zeichen1, 0)

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
            if (Balldatei != ''):
                try:
                    temp2 = ''
                    Datei = open(Balldatei, 'r', -1, 'utf-8') #speichert gesamten Inhalt der (*.ball)-Datei in Variable 'temp2'
                    for zeile in Datei.readlines():
                        temp2 += zeile
                    Datei.close()
                except:
                    return '[Error: (*.ball)-Datei konnte nicht geoeffnet werden]'
                
                try:
                    for i in range(temp):
                        LigmaB.Entsch(Keydatei, Balldatei)
                except:
                    return '[Error: LigmaB konnte nicht korrekt angesteuert werden]'
                
                try:
                    temp = ''
                    Datei = open('Testdateien/Nachricht.ball', 'r', -1, 'utf-8') #speichert gesamten Inhalt von 'test.txt' in Variable 'Ergebnis'
                    for zeile in Datei.readlines():
                        temp += zeile
                    Datei.close()
                    Zeichenkette = temp
                except:
                    return '[Error: Deine Mudda'
            else:
                return '[Error: (*.ball)-Datei muss durch aktive Sekundaerverschluesselung angegeben werden]'

        Rad = Rad[::-1]

        ZS = ''
        for Zeichen1 in Zeichenkette[::-1]:
            ZS += Codieren(Zeichen1, 1)
        return ZS[::-1]


#=====================Beispiele für Implementierung und Tests=====================#
Ergebnis = ''
Datei = open('Testdateien/Text.txt', 'r', -1, 'utf-8') #speichert gesamten Inhalt von 'test.txt' in Variable 'Ergebnis'
for zeile in Datei.readlines():
    Ergebnis += zeile
Datei.close()

Ergebnis = Raedern(Ergebnis, 'v', 200, 'Testdateien/Key.lig') #siehe Funktionsbeschreibung und angegebene Parameter
print(Ergebnis)

Datei = open('Testdateien/Nachricht.ball', 'w', -1, 'utf-8') #speichert zuvor verschlüsselten Text in Datei 'test.ball'
Datei.write(Ergebnis)
Datei.close()

LigmaB.Versch(5, 'Testdateien/Key.lig', 'Testdateien/Nachricht.ball')
LigmaB.Versch(5, 'Testdateien/Key.lig', 'Testdateien/Nachricht.ball')
LigmaB.Versch(7, 'Testdateien/Key.lig', 'Testdateien/Nachricht.ball')
LigmaB.Versch(8, 'Testdateien/Key.lig', 'Testdateien/Nachricht.ball')

Ergebnis = ''
Datei = open('Testdateien/Nachricht.ball', 'r', -1, 'utf-8') #speichert gesamten Inhalt von 'test.txt' in Variable 'Ergebnis'
for zeile in Datei.readlines():
    Ergebnis += zeile
Datei.close()

Ergebnis = Raedern(Ergebnis, 'e', 0, 'Testdateien/Key.lig', 'Testdateien/Nachricht.ball') #siehe Funktionsbeschreibung und angegebene Parameter
print(Ergebnis)