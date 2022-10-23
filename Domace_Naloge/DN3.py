ovire = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
            (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]

def Obvezna():
    x = 6

    i = 1
    test = False
    while i < 10:
        for x1, x2, y in ovire:
            if i == y and x1 <= x <= x2:
                print(i)
                test = True
                break
        if test: break
        i += 1

def Dodatna():
    width = 0
    for _, x, _ in ovire:
        if width < x:
            width = x
    
    max = (0, 0)
    zmaga = False
    for x in range(1, x + 1):
        i = 1
        test = False
        while i <= 10:
            for x1, x2, y in ovire:
                if i == y and x1 <= x <= x2:
                    if y > max[1]:
                        max = (x, y)
                    test = True
                    break
                elif i == 10:
                    max = (x, "Zmaga!")
                    test = True
                    zmaga = True
                    break
            i += 1
            if test: break
        if zmaga: break
    print(max)
            
print("Obvezna:")
Obvezna()
print("Dodatne:")
Dodatna()