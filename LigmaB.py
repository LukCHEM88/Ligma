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
    if (Anzahl < 0): #Umkehrung der Variable 'Anzahl', falls diese negativ ist
        Anzahl = -Anzahl
    if (not os.path.exists(Keydatei)) or (not os.path.exists(Zieldatei)) or (Anzahl < 1): #Kontrolle, ob alle Parameter korrekt angegeben wurden
        return False

    Ergebnis = '' #speichern des Inhalts der angegeben Key-Datei in Variable 'Ergebnis'
    try:
        Datei = open(Keydatei, 'r', -1, 'utf-8')
    except:
        return False
    for Zeile in Datei.readlines():
        Ergebnis += Zeile
        if (Zeile[0] == '['):
            temp = len(Zeile)
    Datei.close()

    Ergebnis2 = '' #speichern des Inhalts der angegeben (*.ball)-Datei in Variable 'Ergebnis2'
    try:
        Datei = open(Zieldatei, 'r', -1, 'utf-8')
    except:
        return False
    for Zeile in Datei.readlines():
        Ergebnis2 += Zeile
    Datei.close()

    random.seed(Ergebnis) #Seed festlegen und hinzufügen von zufälligen Zeichen in Variable 'Ergebnis2'
    for i in range(Anzahl):
        Zahl = random.randint(0, len(Ergebnis2))
        Zahl2 = random.randint(0, len(Ergebnis2))
        Ergebnis2 = Ergebnis2[0:Zahl] + Ergebnis2[Zahl2] + Ergebnis2[Zahl:len(Ergebnis2)]

    try: #speichern der modifizierten Key-Datei
        Datei = open(Keydatei, 'w', -1, 'utf-8')
    except:
        return False
    Datei.writelines(Ergebnis[0:temp] + str(Anzahl) + '\n' + Ergebnis[temp::])
    Datei.close()

    try: #speichern der modifizierten (*.ball)-Datei
        Datei = open(Zieldatei, 'w', -1, 'utf-8')
    except:
        return False
    Datei.writelines(Ergebnis2)
    Datei.close()

    return True

def Entsch(Keydatei: str, Zieldatei: str) -> bool:
    """
    Löscht eine bestimmte Anzahl an zufälligen Zeichen in eine Datei, welche mit der Schlüsseldatei bestimmt werden können.
    Keydatei = string/Pfad, welcher zur benötigten Key-Datei führt
    Zieldatei = string/Pfad, welcher zur benötigten (*.ball)-Datei führt
    """
    if (not os.path.exists(Keydatei)) or (not os.path.exists(Zieldatei)): #Kontrolle, ob alle Parameter korrekt angegeben wurden
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
        Datei = open(Zieldatei, 'r', -1, 'utf-8')
    except:
        return False
    for Zeile in Datei.readlines():
        Ergebnis2 += Zeile
    Datei.close()

    random.seed(Ergebnis) #Seed festlegen und entfernen von bestimmten, zuvor zufälligen, Zeichen in Variable 'Ergebnis2'
    Zahl = []
    for i in range(Anzahl)[::-1]:
        Zahl.append(random.randint(0, len(Ergebnis2) - i))
        random.randint(0, len(Ergebnis2) - i)
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
        Datei = open(Zieldatei, 'w', -1, 'utf-8')
    except:
        return False
    Datei.writelines(Ergebnis2)
    Datei.close()
    
    return True


#=====================Beispiele für Implementierung und Tests=====================#
'''
ZS = Versch(10, 'C:\\Python\\Ligma\\Core\\Key.lig', 'C:\\Python\\Ligma\\Core\\test.ball') #siehe Funktionsbeschreibung und angegebene Parameter
print(ZS) #Falls ZS = True, dann wurde die Funktion erfolgreich ausgeführt

ZS = Entsch('C:\\Python\\Ligma\\Core\\Key.lig', 'C:\\Python\\Ligma\\Core\\test.ball') #siehe Funktionsbeschreibung und angegebene Parameter
print(ZS) #Falls ZS = True, dann wurde die Funktion erfolgreich ausgeführt
'''