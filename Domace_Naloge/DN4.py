import numpy as np

zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]
ovire = []
x1, y1 = 0, 0
block = False
y = 1
for vrstica in zemljevid:
    x = 1
    vrstica += '.'
    for c in vrstica:
        if c == '#' and not block:
            x1 = x
            y1 = y
            block = True
        if block and c == '.':
            ovire.append((x1, x-1, y))
            block = False
        x += 1
    y += 1

maxx, maxy = 0, 0
_, x, y = zip(*ovire)
maxx = max(x)
maxy = max(y)

zemljevid2 = np.empty(shape=(maxy, maxx), dtype='str')
zemljevid2.fill('.')
for x1, x2, y1 in ovire:
    zemljevid2[y1-1:y1, x1-1:x2] = "#"

for array in zemljevid2: # je mogoče kak bol optimaln način za prevtorit v string?
    vrstica = ""
    for c in array:
        vrstica += c
    print(vrstica)
