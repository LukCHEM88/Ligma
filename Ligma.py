import random
import os

#=====================Funktionen=====================#

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

def Codieren(Zeichen: str, Anzahl: int, Richtung: int) -> str:
    """
    Nimmt ein Zeichen und schickt dieses durch 'Anzahl' viele Räder in die Richtung 'Richtung'.\n
    Zeichen = String | Anzahl = Integer | Richtung = 0/1
    """
    global Rad
    global ZEinzelt
    global Einzelt
    Zeichen = Umwandlung(Zeichen, Einzelt)
    for RNummer in range(Anzahl):
        if (Richtung == 0):
            Zeichen = ZEinzelt[kuerzen2(Zeichen - Rad[RNummer])]
            Rad[RNummer] = kuerzen(Rad[RNummer] + 1)
        else:
            Rad[Anzahl - RNummer - 1] = kuerzen2(Rad[Anzahl - RNummer - 1] - 1)
            Zeichen = ZEinzelt[kuerzen2(Zeichen + Rad[Anzahl - RNummer - 1])]
    return Einzelt[Zeichen]

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
    global Einzelt
    global ZEinzelt
    global Rad

    if (Zeichenkette == '') or ((Schluesseln != 'e') and (Schluesseln != 'v')) or ((AnzahlR < 1) and (Schluesseln != 'e')) or (Keydatei == ''):
        return '[Error: benötigte(r) Parameter nicht vorhanden]'

    Rad = []
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
            Rad.append(kuerzen(s))

        ZS = ''
        for Zeichen1 in Zeichenkette:
            ZS += Codieren(Zeichen1, AnzahlR, 0)

        for i in range(len(Rad)):
            Rad[i] = kuerzen(Rad[i])
        
        Datei = open(Keydatei, 'w', -1, 'utf-8')
        Datei.write(str(Einzelt) + '\n')
        for i in range(len(Rad)):
            Datei.write(str(Rad[i]) + '\n')
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
                Rad.append(kuerzen(int(line.rstrip())))
        Datei.close()

        ZS = ''
        for Zeichen1 in Zeichenkette[::-1]:
            ZS += Codieren(Zeichen1, AnzahlR, 1)
        return ZS[::-1]

def kuerzen(zuKuerzen):
    while (zuKuerzen < 0):
        zuKuerzen += len(Einzelt)
    while (zuKuerzen > len(Einzelt)):
        zuKuerzen -= len(Einzelt)
    return zuKuerzen

def kuerzen2(zuKuerzen):
    while (zuKuerzen < 0):
        zuKuerzen += len(Einzelt)
    while (zuKuerzen > (len(Einzelt) - 1)):
        zuKuerzen -= len(Einzelt)
    return zuKuerzen

#=====================Beispiele für Implementierung und Tests=====================#

Ergebnis = ''
Datei = open('test.txt', 'r', -1, 'utf-8')
for zeile in Datei.readlines():
    Ergebnis += zeile
Datei.close()

Ergebnis = Raedern(Ergebnis, 'v', 2000, 'Key.lig')
print(Ergebnis)

Datei = open('test.ball', 'w', -1, 'utf-8')
Datei.write(Ergebnis)
Datei.close()

Ergebnis = Raedern(Ergebnis, 'e', 0, 'Key.lig')
print(Ergebnis)