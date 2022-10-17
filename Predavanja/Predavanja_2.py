from re import I


tuple = (1, 2, 3, 4, 5) # terka ne moremo spremenit
seznam = [1, 2, 4, 5] # seznam array lahko spreminjamo Java(Array list)
print(len(seznam))

oseba = ["Ana", 74,  True] # OR ("Ana", 74,  True)
ime, teza, je_zenska = oseba;
print(ime, teza, je_zenska)

a, b, c, d, e, f = "abcdef"
print(a, b, c, d, e, f)

x = 1
y = 2
y, x = x, y # zamenaja x in y

# fib
a = b = 1
i = 1
while i < 10:
    print(a)
    b , a = a, a + b
    i += 1


def splittext(neki):
    idx = neki.find(".")
    osnova = neki[:idx]
    koncnica = neki [idx:]
    return osnova, koncnica #varca 1 terko (osnova, koncnica)

ono, tisto = splittext("aha")

prva, druga, *ostalo, zadnja = [1, 2, 3, 4, 5, 6, 7, 8] #spremenljivka _ te ne zanima *_
prva, druga, *_, zadnja = [1, 2, 3, 4, 5, 6, 7, 8]

#
for i in seznam:
    print(i)

for crka in "Benjamin":
    print(crka)

imena = []
ocene = []
student = [("Mitja", 10), ("Sandi", 6), ("Makuc", 9), ("Tilen", 8)]
for ime, ocena in student:
    imena.append(ime)
    ocene.append(ocena)
    print(ime ,":", ocena)

print(list(zip(imena, ocene)))

print(list(range(10))) # range blefira
print(list(range(87, 92)))

for _ in range(10):
    print("*", end='')
print()

print(seznam)
print(seznam[-1], "seznam[-1]")
print("Benjamin"[2:5])
print("Benjamin"[:5])
print("Benjamin"[3:])
print("Benjamin"[-3:])
print("Benjamin"[:-3]) 
# s[:n] prvih n elementov
# s[-n:] zadnjih n
# s[:-n] brez zadnjih n
# s[n:] brez prvih n
# s[m:n] od (vlkjuvno) m do (izkljucno) n

pal = "pericarezeracirep"
print(pal[::-1] == pal) #palindrom reverse string

s = [1, 2, 3, 5, 4, 6, 7, 8]

for prej, nasl in zip(s, s[1:]):
    if prej > nasl:
        print("narobe", prej, nasl)