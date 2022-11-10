import unittest
import numpy as np

ovire1 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]

ovire2 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]

ovire3 = [(1, 3, 6), (2, 4, 3),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]

def stevilo_ovir(ovire):
    return len(ovire)

def dolzina_ovir(ovire):
    vs = 0
    for x1, x2, _ in ovire:
        vs += x2 - x1 + 1
    return vs
def sirina(ovire):
    _, x, _ = zip(*ovire)
    return max(x)

def pretvori_vrstico(vrstica):
    x = 1
    seznam = []
    block = False
    vrstica += '.'
    for c in vrstica:
        if c == '#' and not block:
            x1 = x
            block = True
        if block and c == '.':
            seznam.append((x1, x-1))
            block = False
        x += 1
    return seznam

def dodaj_vrstico(bloki, y):
    seznam = []
    for coords in bloki:
        x0, x1 = coords
        seznam.append((x0, x1, y))
    return seznam

def pretvori_zemljevid(zemljevid):
    ovire = []
    y = 1
    for vrstica in zemljevid:
        seznam = pretvori_vrstico(vrstica)
        if seznam != []:
            for coords in dodaj_vrstico(seznam, y):
                ovire.append(coords)
        y += 1
    return ovire

def globina(ovire, x):
    height = 0
    for _, _, y in ovire1:
        if height < y:
            height = y
    
    i = 1
    test = False
    while i < 10:
        for x1, x2, y in ovire:
            if i == y and x1 <= x <= x2:
                return i
        if test: break
        i += 1
    return None

def naj_stolpec(ovire1):
    width = 0
    for _, x, _ in ovire1:
        if width < x:
            width = x
    
    max = (0, 0)
    zmaga = False
    for x in range(1, x + 1):
        i = 1
        test = False
        while i <= 10:
            for x1, x2, y in ovire1:
                if i == y and x1 <= x <= x2:
                    if y > max[1]:
                        max = (x, y)
                    test = True
                    break
                elif i == 10:
                    max = (x, None)
                    test = True
                    zmaga = True
                    break
            i += 1
            if test: break
        if zmaga: break
    return max

def senca(ovire):
    width = 0
    for _, x, _ in ovire:
        if width < x:
            width = x

    seznam = []
    i = 1
    while i <= width:
        if globina(ovire, i) is None:
            seznam.append(True)
        else:
            seznam.append(False)
        i += 1
    return seznam
    

class Test(unittest.TestCase):
    def test_stevilo_ovir(self):
        self.assertEqual(7, stevilo_ovir(ovire1))
        self.assertEqual(6, stevilo_ovir(ovire2))
        self.assertEqual(0, stevilo_ovir([]))

    def test_dolzina_ovir(self):
        self.assertEqual(19, dolzina_ovir(ovire1))
        self.assertEqual(15, dolzina_ovir(ovire2))
        self.assertEqual(0, dolzina_ovir([]))

    def test_sirina(self):
        self.assertEqual(10, sirina(ovire1))
        self.assertEqual(9, sirina(ovire1[:-2]))
        self.assertEqual(6, sirina(ovire1[:-3]))
        self.assertEqual(3, sirina(ovire1[:1]))

    def test_pretvori_vrstico(self):
        self.assertEqual([(3, 5)], pretvori_vrstico("..###."))
        self.assertEqual([(3, 5), (7, 7)], pretvori_vrstico("..###.#."))
        self.assertEqual([(1, 2), (5, 7), (9, 9)], pretvori_vrstico("##..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#"))
        self.assertEqual([], pretvori_vrstico("..."))
        self.assertEqual([], pretvori_vrstico(".."))
        self.assertEqual([], pretvori_vrstico("."))

    def test_dodaj_vrstico(self):
        self.assertEqual([(3, 4, 3), (6, 8, 3), (11, 11, 3)], dodaj_vrstico([(3, 4), (6, 8), (11, 11)], 3))

    def test_pretvori_zemljevid(self):
        zemljevid = [
            "......",
            "..##..",
            ".##.#.",
            "...###",
            "###.##",
        ]
        self.assertEqual([(3, 4, 2), (2, 3, 3), (5, 5, 3), (4, 6, 4), (1, 3, 5), (5, 6, 5)], pretvori_zemljevid(zemljevid))

        global pretvori_vrstico
        pretvori = pretvori_vrstico
        try:
            def pretvori_vrstico(vrstica):
                return [(i, i) for i, c in enumerate(vrstica) if c == "#"]
            self.assertEqual([(2, 2, 2), (3, 3, 2), (1, 1, 3), (2, 2, 3), (4, 4, 3), (3, 3, 4), (4, 4, 4),
                              (5, 5, 4), (0, 0, 5), (1, 1, 5), (2, 2, 5), (4, 4, 5), (5, 5, 5)],
                             pretvori_zemljevid(zemljevid),
                             "Funkcija pretvori_zemljevid naj kar lepo uporabi pretvori_vrstico")
        finally:
            pretvori_vrstico = pretvori

        global dodaj_vrstico
        dodaj = dodaj_vrstico
        try:
            def dodaj_vrstico(ovire, vrstica):
                return [(*o, 2 * vrstica) for o in ovire]

            self.assertEqual([(3, 4, 4), (2, 3, 6), (5, 5, 6), (4, 6, 8), (1, 3, 10), (5, 6, 10)],
                             pretvori_zemljevid(zemljevid),
                             "Funkcija pretvori_zemljevid naj kar lepo uporabi dodaj_vrstico")
        finally:
            dodaj_vrstico = dodaj

    def test_globina(self):
        self.assertEqual(3, globina(ovire1, 3))
        self.assertEqual(5, globina(ovire1, 6))
        self.assertEqual(7, globina(ovire2, 6))
        self.assertIsNone(globina(ovire3, 6))

    def test_naj_stolpec(self):
        self.assertEqual((5, 7), naj_stolpec(ovire1))
        self.assertEqual((7, None), naj_stolpec(ovire2))
        self.assertEqual((5, None), naj_stolpec(ovire3))

    def test_senca(self):
        self.assertEqual([False] * 10, senca(ovire1))
        self.assertEqual([False, False, False, False, False, False, True, True, False, False], senca(ovire2))
        self.assertEqual([False, False, False, False, True, True, True, True, False, False], senca(ovire3))
        self.assertEqual([False] * 6, senca(ovire2[:-3]))
        self.assertEqual([False] * 3, senca(ovire3[:1]))


if __name__ == "__main__":
    unittest.main()