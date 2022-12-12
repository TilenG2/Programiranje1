
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

zemljevid = {
    (A, B): "gravel trava",
    (A, V): "pešci lonci",
    (B, C): "bolt lonci",
    (B, V): "",
    (C, R): "stopnice pešci lonci",
    (D, F): "stopnice pešci",
    (D, R): "pešci",
    (E, I): "trava lonci",
    (F, G): "trava črepinje",
    (G, H): "črepinje pešci",
    (G, I): "avtocesta",
    (H, J): "robnik bolt",
    (I, M): "avtocesta",
    (I, P): "gravel",
    (I, R): "stopnice robnik",
    (J, K): "",
    (J, L): "gravel bolt",
    (K, M): "stopnice bolt",
    (L, M): "robnik pešci",
    (M, N): "rodeo",
    (N, P): "gravel",
    (O, P): "gravel",
    (P, S): "",
    (R, U): "trava pešci",
    (R, V): "pešci lonci",
    (S, T): "robnik trava",
    (T, U): "gravel trava",
    (U, V): "robnik lonci trava"
}

zemljevid = {k: set(v.split()) for k, v in zemljevid.items()} | {k[::-1]: set(v.split()) for k, v in zemljevid.items()}


mali_zemljevid = {(A, B): "robnik bolt",  # 3
                  (A, C): "bolt rodeo pešci",  # 8
                  (C, D): ""}  # 0

mali_zemljevid = {k: set(v.split()) for k, v in mali_zemljevid.items()} | {k[::-1]: set(v.split()) for k, v in mali_zemljevid.items()}

tockovanje = {
    "črepinje": 1,
    "robnik": 1,
    "lonci": 1,
    "gravel": 2,
    "bolt": 2,
    "rodeo": 2,
    "trava": 3,
    "pešci": 4,
    "stopnice": 6,
    "avtocesta": 10
}

def vrednost_povezave(povezava, zemljevid):
    return sum(tockovanje[vescina] for vescina in zemljevid[povezava])

def dosegljive_n(tocka, zemljevid, meja):

    def doseg(tockameja, zemljevid, banned):
        tocka, meja = tockameja
        dosegljivetocke = set(tocka) # originalna točka t bo vedno dosegljiva

        tocke = ((x1, x2) for x1, x2 in zemljevid if x1 == tocka) 

        for x1, x2 in tocke:
            zahtevnost = vrednost_povezave((x1, x2), zemljevid) # dobi zahtevnost povezave
            if meja - zahtevnost >= 0 and x2 not in banned: #pogleda ce imamo se dovolj "nagradnih točk" in da se slučajno ne vrnemo po isti poti nazaj
                dosegljivetocke = dosegljivetocke | doseg((x2, meja - zahtevnost), zemljevid, banned | set(tocka)) #ponovno kliče funkcijo 

        return dosegljivetocke #vrnemo vse dosegljive tocke za tocko t

    return doseg((tocka, meja), zemljevid, set()) #prvi klic na zacetku nimamo prepovedanih tock zato je tam None

print({S, P, O, N, I}, dosegljive_n(P, zemljevid, 2))
print({T, S, P, O, I, M, N}, dosegljive_n(P, zemljevid, 4))
print({T, S, P, O, I, E, M, N}, dosegljive_n(P, zemljevid, 6))
print({T, S, P, O, I, E, M, N}, dosegljive_n(P, zemljevid, 8))
print({T, S, P, O, I, E, M, N, L, U, R}, dosegljive_n(P, zemljevid, 9))
print({S, P}, dosegljive_n(P, zemljevid, 0))
print({S, P}, dosegljive_n(P, zemljevid, 1))
print({H, J, L, K, M, N, I, G, R, D, F, V, A, B, C, U, E, S, T, P, O}, dosegljive_n(A, zemljevid, 1000))

# dosegljive_n(A, zemljevid, 1000)