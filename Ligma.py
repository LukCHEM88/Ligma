import random

#=====================Funktionen=====================#

def RadDreh(Nummer, Richtung):
    """
    Dreht eine Liste entweder nach vorne oder nach hinten.\n
    Nummer = Integer, welche die Nummer des zu drehenden Rads angibt | Richtung = 1 --> Verschlüsseln | Richtung = 2 --> Entschlüsseln
    """
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

def Vereinzeln(ZKette):
    """
    Schreibt alle in einer gegebenen Zeichenkette vorkommenden verschiedenen Zeichen in eine Liste.\n
    ZKette = Zeichenkette, welche genutzt werden soll
    """
    Liste = []
    for Element in ZKette:
        if not Element in Liste:
            Liste.append(Element)
    return Liste

def RadHinzu(Startposition):
    """
    Erstellt ein weiteres Rad, welches eine Liste ist, in der Liste 'Rad'.\n
    Inhalt = Liste, welche als Rad hinzugefügt werden soll | Startposition = Integer, welcher besagt wie weit das Rad verschoben werden soll
    """
    global ZEinzelt
    Rad.append(ZEinzelt[:])
    if (Startposition > (len(Einzelt) // 2)) and (Startposition < len(Einzelt)):
        for i in range(len(Einzelt) - Startposition):
            RadDreh(len(Rad) - 1, 1)
    else:
        for i in range(Startposition):
            RadDreh(len(Rad) - 1, 0)

def Codieren(Zeichen, Anzahl, Richtung):
    """
    Nimmt ein Zeichen und schickt dieses durch 'Anzahl' viele Räder in die Richtung 'Richtung'.\n
    Zeichen = String | Anzahl = Integer | Richtung = 0/1
    """
    Zeichen = Umwandlung(Zeichen, Einzelt)
    for RNummer in range(Anzahl):
        if (Richtung == 0):
            Zeichen = Rad[RNummer][int(Zeichen)]
            RadDreh(RNummer, 0)
        else:
            RadDreh(Anzahl - RNummer - 1, 1)
            Zeichen = Umwandlung(Zeichen, Rad[Anzahl - RNummer - 1])
    return Einzelt[int(Zeichen)]

def Umwandlung(Zeichen, gesucht):
    """
    Wandelt ein gegebenes Zeichen in die dementsprechende 'gesucht'-Zahl um.\n
    Zeichen = String, welcher umgewandelt wird | gesucht = Liste, welche nach 'Zeichen' abgesucht wird
    """
    for Nummer in range(len(gesucht)):
        if gesucht[Nummer] == Zeichen:
            Zeichen = Nummer
            break
    return Zeichen

def KeySpeichern():
    Datei = open('Key.lig', 'w', -1, 'utf-8')
    Datei.write(str(Einzelt) + '\n')
    for i in range(len(Verschiebungen)):
        Datei.write(str(Verschiebungen[i]) + '\n')
    Datei.close()


#=====================Quellcode=====================#

Schluesseln = ''
while (Schluesseln != 'e') and (Schluesseln != 'v'):
    Schluesseln = input('Wollen sie eine Nachricht Ent- oder Verschlüsseln? (e/v) --> ').lower()

Zeichenkette = input('Nachricht: ')
Rad = []
Verschiebungen = []
manuel = ''
if (Schluesseln == 'v'):
    Einzelt = Vereinzeln(Zeichenkette)
    Einzelt.sort()
else:
    while (manuel != 'y') and (manuel != 'n'):
        manuel = input('Wollen sie die bereits vorliegende Keydatei benutzen? (y/n) --> ').lower()
    if (manuel == 'n'):
        Einzelt = eval(input('Bitte geben sie die "Einzelt" Variable an.: '))
    else:
        Datei = open('Key.lig', 'r', -1, 'utf-8')
        Einzelt = eval(Datei.readline())
        Datei.close()
ZEinzelt = []

for i in range(len(Einzelt)):
    ZEinzelt.append(i)

AnzahlR = 0
if (manuel != 'y'):
    while (AnzahlR < 1):
        AnzahlR = int(input('Anzahl Räder: '))

if (manuel != 'y'):
    manuell2 = ''
    while (manuell2 != 'y') and (manuell2 != 'n'):
        manuell2 = input('Wollen sie die Räder manuell eingeben? (y/n) --> ').lower()
    for i in range(AnzahlR):
        if (manuell2 == 'y'):
            s = int(input('Verschiebung von Rad ' + str(i + 1) + ': '))
        else:
            s = random.randint(0, AnzahlR)
        Verschiebungen.append(0)
        RadHinzu(s)
else:
    Datei = open('Key.lig', 'r', -1, 'utf-8')
    AnzahlR = 0
    for line in Datei.readlines():
        if (line[0] != '['):
            AnzahlR += 1
            Verschiebungen.append(0)
            RadHinzu(int(line))
    Datei.close()

if (Schluesseln == 'e'):
    ZS = ''
    for Zeichen1 in Zeichenkette[::-1]:
        ZS = ZS + Codieren(Zeichen1, AnzahlR, 1)
    print(ZS[::-1])
else:
    ZS = ''
    for Zeichen1 in Zeichenkette:
        ZS = ZS + Codieren(Zeichen1, AnzahlR, 0)
    print(ZS + '[Ende]')

    for i in range(len(Verschiebungen)):
        while (Verschiebungen[i] < 0):
            Verschiebungen[i] = Verschiebungen[i] + len(Einzelt)
        while (Verschiebungen[i] > len(Einzelt)):
            Verschiebungen[i] = Verschiebungen[i] - len(Einzelt)

    for i in range(len(Verschiebungen)):
        print('Verschiebung von Rad ' + str(i + 1) + ': ' + str(Verschiebungen[i]))
    print('Einzelt = ' + str(Einzelt))

    KeySpeichern()