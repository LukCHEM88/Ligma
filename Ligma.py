import random
import os

#=====================Funktionen=====================#

def RadDreh(Nummer: int, Richtung: int) -> None:
    """
    Dreht eine Liste entweder nach vorne oder nach hinten.\n
    Nummer = Integer, welche die Nummer des zu drehenden Rads angibt | Richtung = 1 --> Verschlüsseln | Richtung = 2 --> Entschlüsseln
    """
    global Rad
    temp = ''
    laenge = len(Rad[Nummer]) - 1
    if (Richtung == 0):
        Verschiebungen[Nummer] = Verschiebungen[Nummer] + 1
        for Nummer2 in range(len(Rad[Nummer])):
            temp2 = Rad[Nummer][Nummer2]
            if (temp != ''):
                Rad[Nummer][Nummer2] = temp
            else:
                Rad[Nummer][Nummer2] = Rad[Nummer][laenge]
            temp = temp2
    elif (Richtung == 1):
        Verschiebungen[Nummer] = Verschiebungen[Nummer] - 1
        for Nummer2 in range(len(Rad[Nummer])):
            temp2 = Rad[Nummer][laenge - Nummer2]
            if (temp != ''):
                Rad[Nummer][laenge - Nummer2] = temp
            else:
                Rad[Nummer][laenge - Nummer2] = Rad[Nummer][0]
            temp = temp2

def Vereinzeln(ZKette: str) -> list:
    """
    Schreibt alle in einer gegebenen Zeichenkette vorkommenden verschiedenen Zeichen in eine Liste.\n
    ZKette = Zeichenkette, welche genutzt werden soll
    """
    Liste = []
    for Element in ZKette:
        if not Element in Liste:
            Liste.append(Element)
    return Liste

def RadHinzu(Startposition: int) -> None:
    """
    Erstellt ein weiteres Rad, welches eine Liste ist, in der Liste 'Rad'.\n
    Startposition = Integer, welcher besagt wie weit das Rad verschoben werden soll
    """
    global ZEinzelt
    global Rad
    Rad.append(ZEinzelt[:])
    if (Startposition > (len(Einzelt) // 2)) and (Startposition < len(Einzelt)):
        for i in range(len(Einzelt) - Startposition):
            RadDreh(len(Rad) - 1, 1)
    else:
        for i in range(Startposition):
            RadDreh(len(Rad) - 1, 0)

def Codieren(Zeichen: str, Anzahl: int, Richtung: int) -> str:
    """
    Nimmt ein Zeichen und schickt dieses durch 'Anzahl' viele Räder in die Richtung 'Richtung'.\n
    Zeichen = String | Anzahl = Integer | Richtung = 0/1
    """
    global Rad
    Zeichen = Umwandlung(Zeichen, Einzelt)
    for RNummer in range(Anzahl):
        if (Richtung == 0):
            Zeichen = Rad[RNummer][int(Zeichen)]
            RadDreh(RNummer, 0)
        else:
            RadDreh(Anzahl - RNummer - 1, 1)
            Zeichen = Umwandlung(Zeichen, Rad[Anzahl - RNummer - 1])
    return Einzelt[int(Zeichen)]

def Umwandlung(Zeichen: str, gesucht: list) -> int:
    """
    Wandelt ein gegebenes Zeichen in die dementsprechende 'gesucht'-Zahl um.\n
    Zeichen = String, welcher umgewandelt wird | gesucht = Liste, welche nach 'Zeichen' abgesucht wird
    """
    for Nummer in range(len(gesucht)):
        if gesucht[Nummer] == Zeichen:
            Zeichen = Nummer
            break
    return Zeichen
        
def Raedern(Zeichenkette = '', Schluesseln = '', AnzahlR = 0, Keydatei = '') -> str:
    """
    Zeichenkette = String, der ver-/entschlüsselt werden soll \n
    Schlüsseln = v/e --> v = verschlüsseln; e = entschlüsseln \n
    AnzahlR = Anzahl an Rädern, welche beim verschlüsseln genutzt werden sollen \n
    Keydatei1 = Pfad, welcher zum Speicherort der Keydatei führt
    """
    global Verschiebungen
    global Einzelt
    global ZEinzelt
    global Rad

    if (Zeichenkette == '') or ((Schluesseln != 'e') and (Schluesseln != 'v')) or ((AnzahlR < 1) and (Schluesseln != 'e')) or (Keydatei == ''):
        return '[Error: benötigte(r) Parameter nicht vorhanden]'

    Rad = []
    Verschiebungen = []
    ZEinzelt = []

    if (Schluesseln == 'v'):
        Einzelt = Vereinzeln(Zeichenkette)
        Einzelt.sort()
    elif (Schluesseln == 'e'):
        Datei = open(Keydatei, 'r', -1, 'utf-8')
        Einzelt = eval(Datei.readline())
        Datei.close()
        Kontrolle = Vereinzeln(Zeichenkette)
        for Zeichen in Kontrolle:
            temp = False
            for Zeichen1 in Einzelt:
                if (Zeichen1 == Zeichen):
                    temp = True
                    break
            if (temp == False):
                return '[Error: (*.lig)-Datei und (*.ball)-Datei nicht Kompatibel]'

    for i in range(len(Einzelt)):
            ZEinzelt.append(i)

    if (Schluesseln == 'v'):
        for i in range(AnzahlR):
            s = random.randint(0, AnzahlR)
            Verschiebungen.append(0)
            RadHinzu(s)

        ZS = ''
        for Zeichen1 in Zeichenkette:
            ZS = ZS + Codieren(Zeichen1, AnzahlR, 0)

        for i in range(len(Verschiebungen)):
            while (Verschiebungen[i] < 0):
                Verschiebungen[i] = Verschiebungen[i] + len(Einzelt)
            while (Verschiebungen[i] > len(Einzelt)):
                Verschiebungen[i] = Verschiebungen[i] - len(Einzelt)
        
        Datei = open(Keydatei, 'w', -1, 'utf-8')
        Datei.write(str(Einzelt) + '\n')
        for i in range(len(Verschiebungen)):
            Datei.write(str(Verschiebungen[i]) + '\n')
        Datei.close()

        return ZS
    elif (Schluesseln == 'e'):
        if os.path.exists(Keydatei):
            Datei = open(Keydatei, 'r', -1, 'utf-8')
        else:
            return '[Error: Keydatei wurde nicht gefunden]'
        AnzahlR = 0
        for line in Datei.readlines():
            if (line[0] != '['):
                AnzahlR += 1
                Verschiebungen.append(0)
                RadHinzu(int(line.rstrip()))
        Datei.close()

        ZS = ''
        for Zeichen1 in Zeichenkette[::-1]:
            ZS = ZS + Codieren(Zeichen1, AnzahlR, 1)
        return ZS[::-1]

#=====================Beispiele für Implementierung und Tests=====================#
'''
Ergebnis = ''
Datei = open('test.txt', 'r', -1, 'utf-8')
for zeile in Datei.readlines():
    Ergebnis = Ergebnis + zeile
Datei.close()

Ergebnis = Raedern(Ergebnis, 'v', 1000, 'Key.lig')
print(Ergebnis)

Datei = open('test.ball', 'w', -1, 'utf-8')
Datei.write(Ergebnis)
Datei.close()

Ergebnis = Raedern(Ergebnis, 'e', 0, 'Key.lig')
print(Ergebnis)
'''