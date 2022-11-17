prastevila = [2, 3, 5]
i = 5
while i < 100000000000000000000000000000000000000:
    i += 1
    test = False
    for x in prastevila:
        if i % x == 0:
            test = True
            break 
    if test:
        continue
    prastevila.append(i)

    if not ((i + 1) % 6 == 0 or (i - 1) % 6 == 0):
        print("protiprimer", i)
#print(prastevila)
    