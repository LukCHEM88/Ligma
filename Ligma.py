import copy
Zeichenkette = 'Aiuign'

#=====================Funktionen=====================#

def RadDreh(Nummer, Richtung):
    """
    Dreht eine Liste entweder nach vorne oder nach hinten.
    Nummer = Integer, welche die Nummer des zu drehenden Rads angibt | Richtung = 1 --> Verschlüsseln | Richtung = 2 --> Entschlüsseln
    """
    temp = ''
    laenge = len(Rad[Nummer]) - 1
    if (Richtung == 0):
        for Nummer2 in range(len(Rad[Nummer])):
            temp2 = Rad[Nummer][Nummer2]
            if (temp != ''):
                Rad[Nummer][Nummer2] = temp
            else:
                Rad[Nummer][Nummer2] = Rad[Nummer][laenge]
            temp = temp2
    elif (Richtung == 1):
        for Nummer2 in range(len(Rad[Nummer])):
            temp2 = Rad[Nummer][laenge - Nummer2]
            if (temp != ''):
                Rad[Nummer][laenge - Nummer2] = temp
            else:
                Rad[Nummer][laenge - Nummer2] = Rad[Nummer][0]
            temp = temp2

def Vereinzeln(ZKette):
    """
    Schreibt alle in einer gegebenen Zeichenkette vorkommenden verschiedenen Zeichen in eine Liste.
    ZKette = Zeichenkette, welche genutzt werden soll
    """
    Liste = []
    for Element in ZKette:
        if not Element in Liste:
            Liste.append(Element)
    return Liste

def RadHinzu(Inhalt, Startposition):
    """
    Erstellt ein weiteres Rad, welches eine Liste ist, in der Liste 'Rad'.
    Inhalt = Liste, welche als Rad hinzugefügt werden soll | Startposition = Integer, welcher besagt wie weit das Rad verschoben werden soll
    """
    Rad.append(copy.deepcopy(Inhalt))
    if (Startposition > (len(Inhalt) // 2)):
        for i in range(len(Inhalt) - Startposition):
            RadDreh(len(Rad) - 1, 1)
    else:
        for i in range(Startposition):
            RadDreh(len(Rad) - 1, 0)

#---Was nicht funktioniert(warum auch immer)---#
Rad = []
Inhalt1 = Vereinzeln(Zeichenkette)
print(Inhalt1)
RadHinzu(Inhalt1, 0)
RadHinzu(Inhalt1, 4)
RadHinzu(Inhalt1, 3)
RadHinzu(Inhalt1, 2)
for i in Rad:
    print(i)
print(Inhalt1)

#---Was irgendwie jetzt funktioniert(warum auch immer)---#
Rad = []
RadHinzu(Vereinzeln(Zeichenkette), 0)
RadHinzu(Vereinzeln(Zeichenkette), 4)
RadHinzu(Vereinzeln(Zeichenkette), 3)
RadHinzu(Vereinzeln(Zeichenkette), 2)
for i in Rad:
    print(i)
print(Inhalt1)