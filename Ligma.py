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
        if (Richtung == 0): #falls verschlüsseln:
            Zeichen = ZEinzelt[kuerzen(Zeichen - Rad[RNummer], 1)] #Zahl, welche in Variable 'Zeichen' gespeichert is wird 'gerädert' in positive Richtung via des Mechanismus der Enigma
            Rad[RNummer] = kuerzen(Rad[RNummer] + 1) #Rad, welches genutzt wurde, wird in positive Richtung weitergedreht
        elif (Richtung == 1): #falls entschlüsseln:
            Rad[Anzahl - RNummer - 1] = kuerzen(Rad[Anzahl - RNummer - 1] - 1, 1) #Zahl, welche in Variable 'Zeichen' gespeichert is wird 'gerädert' in negative Richtung via des Mechanismus der Enigma
            Zeichen = ZEinzelt[kuerzen(Zeichen + Rad[Anzahl - RNummer - 1], 1)] #Rad, welches genutzt wurde, wird in negative Richtung weitergedreht
    return Einzelt[Zeichen]

def Umwandlung(Zeichen: str, gesucht: list) -> int:
    """
    Wandelt ein gegebenes Zeichen in die dementsprechende 'gesucht'-Zahl um.\n
    Zeichen = String, welcher umgewandelt wird\n
    gesucht = Liste, welche nach 'Zeichen' abgesucht wird
    """
    for Nummer in range(len(gesucht)):
        if gesucht[Nummer] == Zeichen:
            Zeichen = Nummer
            break
    return Zeichen

def kuerzen(zuKuerzen: int, was = 0) -> int:
    """
    Verschiebt einen gegebenen Integer-Wert in den vorgegbenen Bereich.
    zuKürzen = Integer, welche verschoben werden muss
    was = Integer, welche angibt wie viel vom vorgegebene Bereich abgezogen werden soll
    """
    while (zuKuerzen < 0):
        zuKuerzen += len(Einzelt)
    while (zuKuerzen > (len(Einzelt) - was)):
        zuKuerzen -= len(Einzelt)
    return zuKuerzen

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

    if (Zeichenkette == '') or ((Schluesseln != 'e') and (Schluesseln != 'v')) or ((AnzahlR < 1) and (Schluesseln != 'e')) or (Keydatei == ''): #Check, ob alle Parameter genügend angegeben sind
        return '[Error: benötigte(r) Parameter nicht vorhanden]'

    Rad = []
    ZEinzelt = []

    if (Schluesseln == 'v'): #Einzelt-Variable definieren und sortieren
        Einzelt = Vereinzeln(Zeichenkette)
        Einzelt.sort()
    elif (Schluesseln == 'e'): #Einzelt-Variable definieren und kontrollieren
        if os.path.exists(Keydatei):
            try:
                Datei = open(Keydatei, 'r', -1, 'utf-8')
            except:
                return '[Error: Keydatei kann nicht geöffnet werden]'
        else:
            return '[Error: Keydatei wurde nicht gefunden]'
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

    if (Schluesseln == 'v'): #Räder hinzufügen, Zeichenkette verschlüsseln, 'Rad' kürzen, Key-Datei speichern (+ Kontrolle) und verschlüsselter Text zurückgeben
        for i in range(AnzahlR):
            s = random.randint(0, AnzahlR)
            Rad.append(kuerzen(s))

        ZS = ''
        for Zeichen1 in Zeichenkette:
            ZS += Codieren(Zeichen1, AnzahlR, 0)

        for i in range(len(Rad)):
            Rad[i] = kuerzen(Rad[i])
        
        try:
            Datei = open(Keydatei, 'w', -1, 'utf-8')
        except:
            return '[Error: Keydatei kann nicht überschrieben/erstellt werden]'
        Datei.write(str(Einzelt) + '\n')
        for i in range(len(Rad)):
            Datei.write(str(Rad[i]) + '\n')
        Datei.close()

        return ZS
    elif (Schluesseln == 'e'): #Räder aus Key-Datei herauslesen und in 'Rad' speichern, Zeichenkette dekodieren und entschlüsselter Text zurückgeben
        Datei = open(Keydatei, 'r', -1, 'utf-8')
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


#=====================Beispiele für Implementierung und Tests=====================#

Ergebnis = ''
Datei = open('C:\\Python\\Ligma\\Core\\test.txt', 'r', -1, 'utf-8') #speichert gesamten Inhalt von 'test.txt' in Variable 'Ergebnis'
for zeile in Datei.readlines():
    Ergebnis += zeile
Datei.close()

Ergebnis = Raedern(Ergebnis, 'v', 2000, 'C:\\Python\\Ligma\\Core\\Key.lig') #siehe Funktionsbeschreibung und angegebene Parameter
print(Ergebnis)

Datei = open('C:\\Python\\Ligma\\Core\\test.ball', 'w', -1, 'utf-8') #speichert zuvor verschlüsselten Text in Datei 'test.ball'
Datei.write(Ergebnis)
Datei.close()

Ergebnis = Raedern(Ergebnis, 'e', 0, 'C:\\Python\\Ligma\\Core\\Key.lig') #siehe Funktionsbeschreibung und angegebene Parameter
print(Ergebnis)