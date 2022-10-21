prepovedani = [tuple(int(x) for x in vrstica.split("-")) for vrstica in open("intervali.txt")]
dovoljena = 0

# imam dovolj pomnilnika :)

spodnja, zgornja = prepovedani[0]
for min, max in prepovedani:
    if min < spodnja:
        spodnja = min
    if max > zgornja:
        zgornja = max
print(spodnja,zgornja)

i = spodnja
while i <= zgornja:
    test = True
    for min, max in prepovedani:
        if(min <= i <= max):
            i = max
            test = False
            break
    if test:
        dovoljena +=1
    i += 1

print(dovoljena)