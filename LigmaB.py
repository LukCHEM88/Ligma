import random
import os

#=====================Funktionen=====================#

def Versch(Anzahl: int, Keydatei: str, Zieldatei: str) -> bool:
    """
    Schreibt eine bestimmte Anzahl an zufälligen Zeichen in eine Datei, welche durch die Schlüsseldatei wieder rückgängig gemacht werden kann.
    Anzahl = integer, welche die Anzahl der zufälligen Zeichen angibt
    Keydatei = string/Pfad, welcher zur benötigten Key-Datei führt
    Zieldatei = string/Pfad, welcher zur benötigten (*.ball)-Datei führt
    """
    if (Anzahl < 0):
        Anzahl = -Anzahl
    if (not os.path.exists(Keydatei)) or (not os.path.exists(Zieldatei)) or (Anzahl < 1):
        return False

    Ergebnis = ''
    Datei = open(Keydatei, 'r', -1, 'utf-8')
    for Zeile in Datei.readlines():
        Ergebnis += Zeile
        if (Zeile[0] == '['):
            temp = len(Zeile)
    Datei.close()

    Ergebnis2 = ''
    Datei = open(Zieldatei, 'r', -1, 'utf-8')
    for Zeile in Datei.readlines():
        Ergebnis2 += Zeile
    Datei.close()

    random.seed(Ergebnis)
    for i in range(Anzahl):
        Zahl = random.randint(0, len(Ergebnis2))
        Zahl2 = random.randint(0, len(Ergebnis2))
        Ergebnis2 = Ergebnis2[0:Zahl] + Ergebnis2[Zahl2] + Ergebnis2[Zahl:len(Ergebnis2)]

    Datei = open(Keydatei, 'w', -1, 'utf-8')
    Datei.writelines(Ergebnis[0:temp] + str(Anzahl) + '\n' + Ergebnis[temp::])
    Datei.close()

    Datei = open(Zieldatei, 'w', -1, 'utf-8')
    Datei.writelines(Ergebnis2)
    Datei.close()

    return True

def Entsch(Keydatei: str, Zieldatei: str) -> bool:
    """
    Löscht eine bestimmte Anzahl an zufälligen Zeichen in eine Datei, welche mit der Schlüsseldatei bestimmt werden können.
    Keydatei = string/Pfad, welcher zur benötigten Key-Datei führt
    Zieldatei = string/Pfad, welcher zur benötigten (*.ball)-Datei führt
    """
    if (not os.path.exists(Keydatei)) or (not os.path.exists(Zieldatei)):
        return False
    
    Ergebnis = ''
    Anzahl = -1
    Datei = open(Keydatei, 'r', -1, 'utf-8')
    for Zeile in Datei.readlines():
        if (Zeile[0] != '[') and (Anzahl == -1):
            Anzahl = int(Zeile)
            if (Anzahl < 1):
                return False
        else:
            Ergebnis += Zeile
    Datei.close()

    Ergebnis2 = ''
    Datei = open(Zieldatei, 'r', -1, 'utf-8')
    for Zeile in Datei.readlines():
        Ergebnis2 += Zeile
    Datei.close()

    random.seed(Ergebnis)
    Zahl = []
    for i in range(Anzahl)[::-1]:
        Zahl.append(random.randint(0, len(Ergebnis2) - i))
        random.randint(0, len(Ergebnis2) - i)
    Zahl = Zahl[::-1]
    for Zahli in Zahl:
        Ergebnis2 = Ergebnis2[0:Zahli] + Ergebnis2[Zahli + 1:len(Ergebnis2)]

    Datei = open(Keydatei, 'w', -1, 'utf-8')
    Datei.writelines(Ergebnis)
    Datei.close()

    Datei = open(Zieldatei, 'w', -1, 'utf-8')
    Datei.writelines(Ergebnis2)
    Datei.close()
    
    return True


#=====================Beispiele für Implementierung und Tests=====================#
'''
ZS = Versch(10, 'Key.lig', 'test.ball')
print(ZS) #Falls ZS = True, dann wurde die Funktion erfolgreich ausgeführt

ZS = Entsch('Key.lig', 'test.ball')
print(ZS) #Falls ZS = True, dann wurde die Funktion erfolgreich ausgeführt
'''