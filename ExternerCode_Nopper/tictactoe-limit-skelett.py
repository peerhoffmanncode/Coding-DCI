def ausgabe():
    for zeile in range(3):
        for spalte in range(3):
            print(str(feld[zeile][spalte]),
                  end=" ")
        print("")
    print("")
    
u = "-"

feld = [[u, u, u],
        [u, u, u],
        [u, u, u]]
    
# Auswertung
# liefert 0, wenn O gewonnen hat
# liefert 2, wenn X gewonnen hat
# liefert 1, wenn es unentschieden ausging
# liefert -1, wenn es noch nicht klar ist.
def auswertung():
    for s in (0, 2):
        for x in range(3):
            if feld[x][0] == s and feld[x][1] == s and feld[x][2] == s:
                return s
        for y in range(3):
            if feld[0][y] == s and feld[1][y] == s and feld[2][y] == s:
                return s
        if feld[0][0] == s and feld[1][1] == s and feld[2][2] == s:
            return s
        if feld[0][2] == s and feld[1][1] == s and feld[2][0] == s:
            return s
    for x in range(3):
        for y in range(3):
            if feld[x][y] == u:
                return -1
    return 1
    
def max():
    if auswertung() != -1:
        return auswertung()
    maximalwert = -999
    for x in range(3):
        for y in range(3):
            if feld[x][y] == u:
                feld[x][y] = 2
                wert = min()
                if wert > maximalwert:
                    maximalwert = wert
                feld[x][y] = u
    return maximalwert

def min():
    if auswertung() != -1:
        return auswertung()
    minimalwert = 999
    for x in range(3):
        for y in range(3):
            if feld[x][y] == u:
                feld[x][y] = 0
                wert = max()
                if wert < minimalwert:
                    minimalwert = wert
                feld[x][y] = u
    return minimalwert

minimumX = 0
minimumY = 0

def minWo():
    global minimumX
    global minimumY
    if auswertung() != -1:
        return auswertung()
    minimalwert = 999
    for x in range(3):
        for y in range(3):
            if feld[x][y] == u:
                feld[x][y] = 0
                wert = max()
                if wert < minimalwert:
                    minimalwert = wert
                    minimumX = x
                    minimumY = y
                feld[x][y] = u
    return minimalwert
                
def spiele():
    global feld
    global minimumX
    global minimumY
    feld = [[u, u, u],
            [u, u, u],
            [u, u, u]]
    while (auswertung() == -1):
        ausgabe()
        x = int(input("Dein x: "))
        y = int(input("Dein y: "))
        if (feld[x][y] != u):
            continue
        feld[x][y] = 2
        ausgabe()
        if (auswertung() != -1):
            break
        minWo()
        print("Mein x: " + str(minimumX))
        print("Mein y: " + str(minimumY))
        feld[minimumX][minimumY] = 0
        if auswertung() != -1:
            ausgabe()
            break
