import numpy as np

koordinate = [('Piran', (0, 0)), ('Koper', (8, 2)),
              ('Ilirska Bistrica', (49, 5)), ('Postojna', (46, 29)),
              ('Nova Gorica', (2, 48)), ('Ajdovščina', (24, 42)),
              ('Idrija', (34, 54)), ('Logatec', (48, 46)),
              ('Cerknica', (60, 31)), ('Vrhnika', (57, 51)),
              ('Žiri', (39, 60)), ('Ljubljana', (68, 61)),
              ('Ribnica', (87, 26)), ('Kočevje', (95, 15)),
              ('Grosuplje', (82, 49)), ('Litija', (95, 61)),
              ('Kranj', (58, 82)), ('Kamnik', (78, 80)),
              ('Škofja Loka', (54, 73)), ('Trbovlje', (112, 71)),
              ('Novo mesto', (119, 32)), ('Krško', (162, 56)),
              ('Celje', (129, 80)), ('Maribor', (156, 117)),
              ('Velenje', (117, 94)), ('Slovenska Bistrica', (150, 97)),
              ('Murska Sobota', (196, 138)), ('Ptuj', (173, 102)),
              ('Ormož', (196, 100)), ('Ljutomer', (199, 112)),
              ('Gornja Radgona', (184, 139)),
              ('Jesenice', (36, 102)),
              ("Kot pri Dramlju", (119, -6))]

# koordinate = [('BotRight', (1, 0)), ('BotLeft', (0, 0)),
#               ('TopRight', (1, 1)), ('TopLeft', (0, 1))]

def get_incline(seznam, xcurrent, ycurrent, mirror):
    k = []
    m = 1
    if mirror: #prezrcali cez izgodisce vse tocke
        xcurrent = -xcurrent
        ycurrent = -ycurrent
        m = -1
    for mesto, xy in seznam:
            x, y = xy
            x = x * m
            y = y * m
            if (x, y) != (xcurrent, ycurrent) and x >= xcurrent:
                try:
                    k.append((mesto, (y - ycurrent) / (x - xcurrent)))  #izracuna naklon vsake tocke
                except ZeroDivisionError:
                    if y - ycurrent >= 0: #devide by zero senanagins
                        k.append((mesto, float('inf'))) 
                    elif ycurrent > y:
                        k.append((mesto, float('inf'))) #prepeci zaciklanje ce sta kraja eden nad drugim
                    else:
                        k.append((mesto, float('-inf')))
    return k

_, xy = zip(*koordinate)
back = False

minx = float('inf')
miny = float('inf')
xcurrent = float('inf')
ycurrent = float('inf')
for mesto, xy in koordinate: #dobi kraj ki je najbolj na levi ce jih je vec izbere spodnjega
    x, y = xy
    if minx >= x:
        if x == minx and ycurrent < y:
            continue
        minx = x 
        xcurrent = x
        ycurrent = y
        begkraj = mesto
    
kraji = []
kraji.append(begkraj)

while True:
    seznamk = get_incline(koordinate, xcurrent, ycurrent, back)
    
    mink = float('inf')
    for mesto, k in seznamk:
        if k <= mink: #najde kraj z namanjsim naklonom
            mink = k
            kraj = mesto

    if kraj in kraji: #preveri ce je kraj ze v seznamu vklopi zrcaljenje cez izhodisce
        back = True
        if kraj == begkraj:
            break
        continue

    for mesto, xy in koordinate: # nastavi koordinate na kraj v katerem smo
        if mesto == kraj:
            xcurrent, ycurrent = xy
            break

    kraji.append(kraj)

print(kraji)