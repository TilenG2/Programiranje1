import unittest
import numpy as np
def vrstica(s):
    ovire = []
    y, _, coords = s.partition(":")
    coords = coords.split(", ")
    y = int(y)
    for x in coords:
        x0, x1 = x.split("-")
        x0, x1 = int(x0), int(x1)
        ovire.append((x0, x1, y))
    return ovire

def preberi(s):
    seznam = []
    s = s.splitlines()
    for vrsta in s:
        vrsta = vrstica(vrsta)
        for coords in vrsta:
            seznam.append(coords)
    return seznam

def intervali(xs):
    seznam = []
    for coords in xs:
        x0, x1 = coords
        seznam.append("-".join([str(x0), str(x1)]))
    return seznam

def zapisi_vrstico(y, xs):
    return str(y) + ": " + ", ".join(intervali(xs))

ovire = [(5, 6, 4),
          (90, 100, 13), (5, 8, 13), (9, 11, 13),
          (9, 11, 5), (19, 20, 5), (30, 34, 5),
          (9, 11, 4),
          (22, 25, 13), (17, 19, 13)]
        
def zapisi(ovire):
    _, _, maxy = zip(*ovire)
    maxy = max(maxy)
    seznam = np.empty(shape=maxy , dtype=list)
    i = 0
    while i < maxy:
        seznam[i]=[]
        i += 1
    for coords in ovire:
        x0, x1, y = coords
        seznam[y-1].append((x0, x1))
    strZapis=""
    i = 1
    for coords in seznam:
        if coords != []:
            coords = sorted(coords)
            strZapis += str(i) + ": " + ", ".join(intervali(coords)) +"\n"
        i += 1
    return strZapis.rstrip("\n")

class Obvezna(unittest.TestCase):
    def test_vrstica(self):
        self.assertEqual([(1, 3, 4), (5, 11, 4), (15, 33, 4)], vrstica("4: 1-3, 5-11, 15-33"))
        self.assertEqual([(989, 1300, 1234)], vrstica("1234: 989-1300"))

    def test_preberi(self):
        self.assertEqual([(5, 6, 4),
                          (90, 100, 13), (5, 8, 13), (9, 11, 13),
                          (9, 11, 5), (19, 20, 5), (30, 34, 5),
                          (9, 11, 4),
                          (22, 25, 13), (17, 19, 13)], preberi(
"""4: 5-6
13: 90-100, 5-8, 9-11
5: 9-11, 19-20, 30-34
4: 9-11
13:  22-25, 17-19
"""))

    def test_intervali(self):
        self.assertEqual(["6-10", "12-16", "20-22", "98-102"], intervali([(6, 10), (12, 16), (20, 22), (98, 102)]))

    def test_zapisi_vrstico(self):
        self.assertEqual("5: 6-10, 12-16", zapisi_vrstico(5, [(6, 10), (12, 16)]).rstrip("\n"))
        self.assertEqual("8: 6-10, 12-16, 20-22, 98-102", zapisi_vrstico(8, [(6, 10), (12, 16), (20, 22), (98, 102)]).rstrip("\n"))
        self.assertEqual("8: 6-10, 12-16, 20-22, 98-102", zapisi_vrstico(8, [(6, 10), (12, 16), (20, 22), (98, 102)]).rstrip("\n"))


class Dodatna(unittest.TestCase):
    def test_zapisi(self):
        ovire = [(5, 6, 4),
          (90, 100, 13), (5, 8, 13), (9, 11, 13),
          (9, 11, 5), (19, 20, 5), (30, 34, 5),
          (9, 11, 4),
          (22, 25, 13), (17, 19, 13)]
        kopija_ovir = ovire.copy()
        self.assertEqual("""4: 5-6, 9-11
5: 9-11, 19-20, 30-34
13: 5-8, 9-11, 17-19, 22-25, 90-100""", zapisi(ovire).rstrip("\n"))
        self.assertEqual(ovire, kopija_ovir)


if __name__ == "__main__":
    unittest.main()