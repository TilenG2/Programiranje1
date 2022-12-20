class Rumba:
    neki = 12 # ststic variable
    def __init__(self):
        self.x = self.y = 0

    def naprej(self, razdalija, smer):
        dx, dy = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}[smer]
        self.x += dx * razdalija
        self.y += dy * razdalija
    
    def nazaj(self, razdalija, smer):
        self.naprej(-razdalija, smer)

    def kje_si(self):
        return self.x, self.y




class KompasRumba(Rumba):
    def __init__(self):
        super().__init__()
        self.smer = 0

    def obrni_desno(self):
        self.smer = (self.smer + 1) % 4
    
    def obrni_levo(self):
        self.smer = (self.smer - 1) % 4

    def naprej(self, razdalija, smer = None):
        if smer is None:
            smer = "^>v<"[self.smer]
        super().naprej(razdalija, smer)
    
    def nazaj(self, razdalija, smer = None):
        super().nazaj(razdalija, smer)



ana = Rumba()
# ana.x = ana.y = 0
berta = KompasRumba()
# berta.x = berta.y = 0

berta.naprej(5, ">")
berta.obrni_levo()

berta.naprej(1)

print(berta.kje_si())