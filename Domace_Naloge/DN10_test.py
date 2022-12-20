import os
import warnings
from random import randint
from datetime import datetime
import unittest
from collections import defaultdict

def zapisi_ovire(ime_datoteke, ovire):
    f = open(ime_datoteke, "w")
    for row, ovire_list in ovire.items():
        row = f"{row:03}:"
        for (a, b) in ovire_list:
            row += f"{a:>4}-{b:<4}"
        f.write(row+"\n")

def preberi_ovire(ime_datoteke):
    key = x = None
    ovire_dict, ovire_list = [], []
    for vrstica in open(ime_datoteke):
        vrstica = vrstica.strip()
        if vrstica == "":
            ovire_dict.append((key, ovire_list))
            key = None
            ovire_list = []
            continue
        vrstica = int(vrstica)
        if key is None:
            key = vrstica
            continue
        if x is None:
            x = vrstica
            continue
        ovire_list.append((x, vrstica))
        x = None
    ovire_dict.append((key, ovire_list))
    return dict(ovire_dict)


class TestZapis(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

        self.ovire = {4: [(5, 6), (9, 11)],
                      5: [(9, 11), (19, 20), (30, 34)],
                      13: [(5, 8), (9, 11), (17, 19), (22, 25), (90, 100)]}

        self.ovire2 = self.ovire | {randint(100, 200): [(1, 2)]}
        with open("ovire.txt", "wt") as f:
            lf = "\n"
            f.write("\n\n".join(fr"{y}{lf}{lf.join(fr'{x0}{lf}{x1}' for x0, x1 in xs)}" for y, xs in self.ovire2.items()))

    def test_01_obvezna_zapisi_ovire(self):
        ime_datoteke = f"ovire{datetime.now().strftime('%m-%d-%H-%M-%S')}.txt"
        zapisi_ovire(ime_datoteke, self.ovire)
        with open(ime_datoteke) as f:
            self.assertEqual("""
004:   5-6      9-11
005:   9-11    19-20    30-34
013:   5-8      9-11    17-19    22-25    90-100
""".strip("\n"), "\n".join(map(str.rstrip, f)))

        self.ovire[101] = self.ovire[5]
        zapisi_ovire(ime_datoteke, self.ovire)
        with open(ime_datoteke) as f:
            self.assertEqual("""
004:   5-6      9-11
005:   9-11    19-20    30-34
013:   5-8      9-11    17-19    22-25    90-100
101:   9-11    19-20    30-34
""".strip("\n"), "\n".join(map(str.rstrip, f)))

        os.remove(ime_datoteke)

    def test_02_dodatna_preberi_ovire(self):
        self.assertEqual(preberi_ovire("ovire.txt"), self.ovire2)


if __name__ == "__main__":
    unittest.main()
