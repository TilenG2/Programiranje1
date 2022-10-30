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
        print(c, x, y)
        if c == '#' and not block:
            x1 = x
            y1 = y
            block = True
        if block and c == '.':
            block = False
        x += 1
    y += 1
print(ovire)