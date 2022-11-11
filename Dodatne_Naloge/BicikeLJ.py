import numpy as np

koordinate = [('Piran', (0, 0)), ('Koper', (8, 2)),
              ('Ilirska Bistrica', (49, 5)), ('Postojna', (46, 29)),
              ('Nova Gorica', (2, 48)), ('Ajdovščina', (24, 42)),
              ('Idrija', (34, 54)), ('Logatec', (48, 46)),
              ('Cerknica', (60, 31)), ('Vrhnika', (37, 51)),
              ('Žiri', (39, 60)), ('Ljubljana', (68, 61)),
              ('Ribnica', (87, 26)), ('Kočevje', (95, 15)),
              ('Grosuplje', (49, 82)), ('Litija', (95, 61)),
              ('Kranj', (58, 82)), ('Kamnik', (78, 80)),
              ('Škofja Loka', (54, 73)), ('Trbovlje', (112, 71)),
              ('Novo mesto', (119, 32)), ('Krško', (162, 56)),
              ('Celje', (129, 80)), ('Maribor', (156, 117)),
              ('Velenje', (117, 94)), ('Slovenska Bistrica', (150, 97)),
              ('Murska Sobota', (196, 138)), ('Ptuj', (173, 102)),
              ('Ormož', (196, 100)), ('Ljutomer', (199, 112)),
              ('Gornja Radgona', (184, 139))]

# koordinate = [('BotLeft', (0, 0)), ('BotRight', (2, 0)),
#               ('TopRight', (1, 1)), ('TopLeft', (0, 1))]
def get_incline(seznam, xcurrent, ycurrent, mirror):
    k = []
    m = 1
    if mirror:
        xcurrent = -xcurrent
        ycurrent = -ycurrent
        m = -1
    for mesto, xy in seznam:
            x, y = xy
            x = x * m
            y = y * m
            if (x, y) != (xcurrent, ycurrent) and x >= xcurrent:
                try:
                    k.append((mesto, (y - ycurrent) / (x - xcurrent)))
                except ZeroDivisionError:
                    if y - ycurrent >= 0:
                        k.append((mesto, float('inf')))
                    elif ycurrent > y:
                        k.append((mesto, float('inf')))
                    else:
                        k.append((mesto, float('-inf')))
    return k

_, xy = zip(*koordinate)
maxx, _ = zip(*xy)
maxx = max(maxx)
back = False

xcurrent, ycurrent = min(xy)

for mesto, xy in koordinate:
    if (xcurrent, ycurrent) == xy:
        begkraj = mesto
        break

kraji = []
kraji.append(begkraj)

while True:
    if not back:
        seznamk = get_incline(koordinate, xcurrent, ycurrent, False)
    else:
        seznamk = get_incline(koordinate, xcurrent, ycurrent, True)

    mink = float('inf')
    for mesto, k1 in seznamk:
        if k1 <= mink:
            mink = k1
            location = mesto

    if location in kraji:
        back = True
        if location == begkraj:
            break
        continue

    for mesto, xy in koordinate:
        if mesto == location:
            xcurrent, ycurrent = xy
            break
    
    if location == begkraj:
        break

    kraji.append(location)
print(kraji)