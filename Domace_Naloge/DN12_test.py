
from cmath import inf
import unittest
from unittest.mock import patch

class Steza:
    def __init__(self, sirina, visina, ovire):
        self.sirina = sirina
        self.visina = visina
        self.ovire = ovire
    
    def zaprto(self, x, y):
        return any(y == yOvire and x0Ovire <= x <= x1Ovire for yOvire, x0Ovire, x1Ovire in self.ovire)
    
    def konec(self, x, y, smer):
        dx, dy = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}[smer]
        while 1 <= x + dx <= self.sirina and 1 <= y + dy <= self.visina:
            x += dx
            y += dy
            if self.zaprto(x, y):
                x -= dx
                y -= dy
                break
        return x, y

class Kolesar:
    def __init__(self, x, y, steza):
        self.x = x
        self.y = y
        self.steza = steza
        self.prevozenaPot = 0
    
    def pozicija(self):
        return (self.x, self.y)

    def premik(self, smer):
        tempX, tempY = self.x, self.y
        self.x, self.y = self.steza.konec(self.x, self.y, smer)
        self.prevozenaPot += abs(tempX - self.x) + abs(tempY - self.y)
    
    def prevozeno(self):
        return self.prevozenaPot

class AvtonomniKolesar(Kolesar):
    def __init__(self, x, y, steza, nacrt):
        super().__init__(x, y, steza)
        self.nacrt = nacrt
        self.premikDol = True
    
    def premik(self):
        if self.premikDol:
            self.premikDol = False
            smer = "v"
        else:
            self.premikDol = True
            smer, *_ = self.nacrt
            self.nacrt = self.nacrt[1:] + smer
        super().premik(smer)

class VzvratniKolesar(Kolesar):
    def __init__(self, x, y, steza):
        super().__init__(x, y, steza)
        self.memory = [((self.x, self.y), self.prevozenaPot)]
        
    def premik(self, smer):
        self.memory.append(((self.x, self.y), self.prevozenaPot))
        super().premik(smer)
        
    def nazaj(self):
        (self.x, self.y), self.prevozenaPot = self.memory[0] if len(self.memory) == 1 else self.memory.pop()
    
class PametniKolesar(VzvratniKolesar):
    def __init__(self, x, y, steza):
        super().__init__(x, y, steza)

    def nacrt(self):
        def nacrtRek(self, pot):
            startX, startY = self.x, self.y
            if self.y == self.steza.visina:
                return [(self.prevozenaPot, pot)]
            super().premik("v")
            if((startX, startY) == (self.x, self.y)):
                super().nazaj()
            else:
                temp = nacrtRek(self, pot+"v")
                super().nazaj()
                return temp
            moznosti = []
            if pot[-1:] != "<":
                super().premik(">")
                if((startX, startY) == (self.x, self.y)):
                    super().nazaj()
                else:
                    for moznaPot in nacrtRek(self, pot+">"):
                        moznosti.append(moznaPot)
                    super().nazaj()
            if pot[-1:] != ">":
                super().premik("<")
                if((startX, startY) == (self.x, self.y)):
                    super().nazaj()
                else:
                    for moznaPot in nacrtRek(self, pot+"<"):
                        moznosti.append(moznaPot)
                    super().nazaj()
            return moznosti
        
        moznosti = []
        super().premik("v")
        for moznaPot in nacrtRek(self, "v"):
            moznosti.append(moznaPot)
        super().nazaj()
        super().premik(">")
        for moznaPot in nacrtRek(self, ">"):
            moznosti.append(moznaPot)
        super().nazaj()
        super().premik("<")
        for moznaPot in nacrtRek(self, "<"):
            moznosti.append(moznaPot)
        super().nazaj()
        maxDolzina = inf
        maxPot = inf 
        koncnaPot = (None, "")
        for dolzina, zemljevid in moznosti:
            if maxDolzina >= dolzina:
                if maxPot < len(zemljevid): continue
                maxPot = len(zemljevid)
                koncnaPot = (dolzina, zemljevid)
                maxDolzina = dolzina
        return koncnaPot
        
class TestBase(unittest.TestCase):
    ovire = [(1, 1, 3), (1, 5, 6), (1, 8, 8), (1, 10, 10),
             (2, 5, 6), (2, 13, 16),
             (4, 9, 11), (4, 13, 14),
             (5, 1, 3), (5, 15, 17),
             (6, 5, 6), (6, 8, 9),
             (7, 12, 13),
             (8, 10, 10),
             (9, 1, 2), (9, 14, 16),
             (10, 4, 4), (10, 12, 12),
             (11, 17, 17),
             (12, 13, 15),
             (13, 1, 5), (13, 7, 11), (13, 17, 17),
             (14, 16, 16),
             (15, 3, 4), (15, 10, 11),
             (16, 15, 15),
             (17, 2, 3), (17, 5, 9), (17, 11, 13), (17, 16, 16)]

    ovire2 = [(1, 1, 3), (1, 5, 6), (1, 8, 8), (1, 10, 10),
             (2, 5, 6),
             (4, 9, 11),
             (5, 1, 3),
             (6, 5, 6), (6, 8, 9),
             ]


class Test06(TestBase):
    def test_zaprto(self):
        steza = Steza(17, 19, self.ovire)
        self.assertTrue(steza.zaprto(10, 1))
        self.assertTrue(steza.zaprto(9, 4))
        self.assertTrue(steza.zaprto(10, 4))
        self.assertTrue(steza.zaprto(11, 4))
        self.assertTrue(steza.zaprto(8, 6))
        self.assertTrue(steza.zaprto(9, 6))

        self.assertFalse(steza.zaprto(7, 1))
        self.assertFalse(steza.zaprto(9, 1))
        self.assertFalse(steza.zaprto(8, 4))
        self.assertFalse(steza.zaprto(12, 4))

    def test_konec(self):
        steza = Steza(18, 20, self.ovire)
        self.assertEqual((9, 7), steza.konec(9, 10, "^"))
        self.assertEqual((9, 12), steza.konec(9, 10, "v"))
        self.assertEqual((11, 10), steza.konec(9, 10, ">"))
        self.assertEqual((5, 10), steza.konec(9, 10, "<"))

        self.assertEqual((7, 1), steza.konec(7, 10, "^"))
        self.assertEqual((18, 15), steza.konec(14, 15, ">"))
        self.assertEqual((14, 20), steza.konec(14, 15, "v"))
        self.assertEqual((1, 11), steza.konec(16, 11, "<"))

        self.assertEqual((16, 11), steza.konec(16, 11, ">"))
        self.assertEqual((14, 13), steza.konec(14, 13, "^"))
        self.assertEqual((14, 11), steza.konec(14, 11, "v"))
        self.assertEqual((12, 13), steza.konec(12, 13, "<"))


class Test07(TestBase):
    def test_prevozeno(self):
        steza = Steza(19, 17, self.ovire)
        kolesar = Kolesar(11, 1, steza)

        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(16, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.premik("^")
        self.assertEqual((1, 2), kolesar.pozicija())
        self.assertEqual(29, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((4, 2), kolesar.pozicija())
        self.assertEqual(32, kolesar.prevozeno())
        kolesar.premik("^")
        self.assertEqual((4, 1), kolesar.pozicija())
        self.assertEqual(33, kolesar.prevozeno())



        steza2 = Steza(13, 15, self.ovire2)
        kolesar = Kolesar(4, 2, steza2)
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((4, 15), kolesar.pozicija())
        self.assertEqual(13, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((13, 15), kolesar.pozicija())
        self.assertEqual(22, kolesar.prevozeno())

    def test_uporaba_steza(self):
        steza = Steza(19, 17, self.ovire)
        kolesar = Kolesar(11, 1, steza)

        steza.konec = lambda *_, **__: (15, 1)

        kolesar.premik(">")
        self.assertEqual((15, 1), kolesar.pozicija(), "Kolesar.premik naj kliče Steza.konec!")
        self.assertEqual(4, kolesar.prevozeno(), "Kolesar.premik naj kliče Steza.konec!")


class Test08(TestBase):
    def test_avtonomni(self):
        kolesar = AvtonomniKolesar(12, 1, Steza(17, 18, self.ovire), "><<>><>")
        self.assertEqual((12, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((12, 6), kolesar.pozicija())
        self.assertEqual(5, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 6), kolesar.pozicija())
        self.assertEqual(10, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((17, 10), kolesar.pozicija())
        self.assertEqual(14, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((13, 10), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((13, 11), kolesar.pozicija())
        self.assertEqual(19, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 11), kolesar.pozicija())
        self.assertEqual(31, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 12), kolesar.pozicija())
        self.assertEqual(32, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((12, 12), kolesar.pozicija())
        self.assertEqual(43, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((12, 16), kolesar.pozicija())
        self.assertEqual(47, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((14, 16), kolesar.pozicija())
        self.assertEqual(49, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((14, 18), kolesar.pozicija())
        self.assertEqual(51, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(64, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(64, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 18), kolesar.pozicija())
        self.assertEqual(80, kolesar.prevozeno())



        kolesar = AvtonomniKolesar(12, 1, Steza(17, 18, self.ovire), "><<")
        self.assertEqual((12, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((12, 6), kolesar.pozicija())
        self.assertEqual(5, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 6), kolesar.pozicija())
        self.assertEqual(10, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((17, 10), kolesar.pozicija())
        self.assertEqual(14, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((13, 10), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((13, 11), kolesar.pozicija())
        self.assertEqual(19, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 11), kolesar.pozicija())
        self.assertEqual(31, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 12), kolesar.pozicija())
        self.assertEqual(32, kolesar.prevozeno())
        kolesar.premik()  # > (ponavljanje!)
        self.assertEqual((12, 12), kolesar.pozicija())
        self.assertEqual(43, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((12, 16), kolesar.pozicija())
        self.assertEqual(47, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 16), kolesar.pozicija())
        self.assertEqual(58, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(60, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(60, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((1, 18), kolesar.pozicija())
        self.assertEqual(60, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 18), kolesar.pozicija())
        self.assertEqual(76, kolesar.prevozeno())



        kolesar = AvtonomniKolesar(13, 1, Steza(17, 18, self.ovire), "><")
        self.assertEqual((13, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik()  # v - ne gre nikamor!
        self.assertEqual((13, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 1), kolesar.pozicija())
        self.assertEqual(4, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((17, 4), kolesar.pozicija())
        self.assertEqual(7, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((15, 4), kolesar.pozicija())
        self.assertEqual(9, kolesar.prevozeno())
        kolesar.premik()  # v - ne gre nikamor!
        self.assertEqual((15, 4), kolesar.pozicija())
        self.assertEqual(9, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 4), kolesar.pozicija())
        self.assertEqual(11, kolesar.prevozeno())
        kolesar.premik()  # v
        self.assertEqual((17, 4), kolesar.pozicija())
        self.assertEqual(11, kolesar.prevozeno())
        kolesar.premik()  # <
        self.assertEqual((15, 4), kolesar.pozicija())
        self.assertEqual(13, kolesar.prevozeno())
        kolesar.premik()  # v - ne gre nikamor!
        self.assertEqual((15, 4), kolesar.pozicija())
        self.assertEqual(13, kolesar.prevozeno())
        kolesar.premik()  # >
        self.assertEqual((17, 4), kolesar.pozicija())
        self.assertEqual(15, kolesar.prevozeno())

    @patch.object(Kolesar, "premik")
    def test_klic_super(self, premik):
        self.assertIsNot(Kolesar.premik, AvtonomniKolesar.premik, "AvtonomniKolesar nima svoje metode premik?")
        kolesar = AvtonomniKolesar(12, 1, Steza(17, 18, self.ovire), "><<>><>")
        kolesar.premik()  # v
        self.assertEqual(1, premik.call_count, "AvtonomniKolesar mora (enkrat) klicati podedovani premik!")


class Test09(TestBase):
    def test_prevozeno(self):
        steza = Steza(19, 17, self.ovire)
        kolesar = VzvratniKolesar(11, 1, steza)

        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(16, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik("v")
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.premik("<")
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.premik("^")
        self.assertEqual((1, 2), kolesar.pozicija())
        self.assertEqual(29, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((1, 3), kolesar.pozicija())
        self.assertEqual(28, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((11, 3), kolesar.pozicija())
        self.assertEqual(18, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 3), kolesar.pozicija())
        self.assertEqual(26, kolesar.prevozeno())



        steza = Steza(19, 17, self.ovire)
        kolesar = VzvratniKolesar(11, 1, steza)

        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.premik(">")
        self.assertEqual((19, 1), kolesar.pozicija())
        self.assertEqual(8, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())
        kolesar.nazaj()
        self.assertEqual((11, 1), kolesar.pozicija())
        self.assertEqual(0, kolesar.prevozeno())

    @patch.object(Kolesar, "premik")
    def test_klic_super(self, premik):
        kolesar = VzvratniKolesar(12, 1, Steza(17, 18, self.ovire))
        kolesar.premik("v")
        self.assertEqual(1, premik.call_count, "VzvratniKolesar mora (enkrat) klicati podedovani premik!")


class Test10(TestBase):
    def test_pametni_kolesar(self):
        kolesar = PametniKolesar(12, 1, Steza(17, 18, self.ovire))
        self.assertEqual((23, 'v<v>v>v>v'), kolesar.nacrt())
        self.assertEqual((12, 1), kolesar.pozicija())

        kolesar = PametniKolesar(11, 1, Steza(17, 18, self.ovire))
        self.assertEqual((46, 'v<v>v>v<v>v>v'), kolesar.nacrt())
        self.assertEqual((11, 1), kolesar.pozicija())

        kolesar = PametniKolesar(16, 3, Steza(17, 18, self.ovire))
        self.assertEqual((49, '<v>v>v<v>v>v'), kolesar.nacrt())

        kolesar = PametniKolesar(1, 2, Steza(17, 18, self.ovire))
        self.assertEqual((31, '>v<v>v>v'), kolesar.nacrt())

        kolesar = PametniKolesar(4, 14, Steza(17, 18, self.ovire))
        self.assertEqual((7, '<v'), kolesar.nacrt())


if __name__ == "__main__":
    unittest.main()