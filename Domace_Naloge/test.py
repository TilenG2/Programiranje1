
def pretvori_vrstico(vrstica):
    vritev = []
    for i in range(len(vrstica), 0, -1):
        for ind in indeksi(vrstica, "#" * i):
            if ind + 1 not in indeksi(vrstica, "#" * i) and ind - 1 not in indeksi(vrstica, "#" * i):
                vritev.append((ind + 1, ind + i))
    return sorted(vritev)

def indeksi(s, subs):
    return sorted(list({s.find(subs, i) for i in range(0, len(s)) if s.find(subs, i) != -1 }))
    
print(pretvori_vrstico("..##"))