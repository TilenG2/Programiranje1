# funkcije / metode
# funkcija
print(abs(-19))

#metoda
t = [1, 2, 3]
t.append(4)

ime = "       Anannnnnnnnn"
print(ime.strip("n"))
print(ime.lstrip())
ben = "Benjamin"
print(ben.rjust(15))
print("aSdBBB".casefold()) #za primirjanje dveh nizov
ime.index("n") #prvi n
ime.rindex("n") #zadnji n
ime.find("n") #isto kot index le da ce ni vrednosti vrne -1

imena = "Ana Berta     Cilka Dana"
print(imena.split())
print(imena.split(maxsplit=2))
print(imena.split(" "))
print("ana: neki: nja".partition(":")) # vraca 3 nize prej, pocemer splitas, potem
n = """Prvi
Drugi
Tretji
"""
print(n.splitlines())

imena = "Ana Berta Cilka Dana"
tabimena = imena.split()
print(", ".join(tabimena))
# print(", ".join(tabimena[:-1]) + " in " + tabimena[-1:])

s = [1, 2, 3]
t = [4, 5]
s += t
print(s)

s.insert(2, "Benjamin") #SLOOOOOOOOOW
print(s)

s.pop() # popa zadnji element in ga vrne
s.pop(2) # popa element na 2 inexu in ga vrne
del s[2] # s.remove("Benjamin") remove odstrani prvo pojavitev
print(sorted("Benjamin"))
s = [1, 56, 2, 63, 998, 261, 4, 0]
print(s.sort(reverse=True))


def pomnozi(a, k=2):
    return a * k

print(pomnozi(6))
print(pomnozi(6, 3))

def neki(a, b=10, *args, **kwargs):
    print(a)
    print(b) # default vrednost b = 10
    print(args)
    print(kwargs)

neki(9, 12, 2, 45, 52, 34, janze=2, miki=10)

t = (1, 2, 3, 5, 5, 6, 8, 10)
a, b, *_, c = t #dobis a pa b ostalo da v _ zadnji element da pa v c

def map(f, s):
    t = []
    for x in s:
        t.append(f(x))
    return t

print(map(int, "1 + 2 + 3 + 5 + 3 + 2 + 4 + 24".split("+")))

def filter(test, s):
    t = []
    for x in s:
        if test(x):
            t.append(x)
    return t

def je_sod(x):
    return x % 2 == 0

print(filter(je_sod, t))

# map reduce in reduce so ze v pythonu

def f(k):
    def g(x):
        return x * k
    return g

