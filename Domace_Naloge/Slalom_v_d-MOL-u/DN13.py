import random
import risar
from PyQt5.QtMultimedia import QSound


maxX = risar.maxX
maxY = risar.maxY
ovire = []
nagrade = []
absolute_path = ""
# absolute_path = "/home/tileng/Documents/GitHub/Programiranje1/Domace_Naloge/Slalom_v_d-MOL-u/"

img_kolesar = absolute_path + "kolesar.png"
music = QSound(absolute_path + "arcade.wav")
collect = QSound(absolute_path + "jump.wav")
end = QSound(absolute_path + "explosion.wav")

nagrade_options = {"flowers.png": (1, (40, 36)),
                   "bottle.png": (1, (30, 30)),
                   "stones.png": (2, (40, 31)),
                   "grass.png": (3, (43, 23)),
                   "walker.png": (4, (30, 67)),
                   "scooter.png": (2, (40, 32))}

music.setLoops(QSound.Infinite)
music.play()

kolesar = risar.slika(maxX / 2 - 20 , maxY - 92 - 40, img_kolesar)

score = 0
score_board = risar.besedilo(10, 0, str(score), velikost=40)

zivljenja = 3
lives = risar.besedilo(maxX-40,0,str(zivljenja), velikost=40)

fail = False
while True:
    sirina = random.randint(30, 80)
    xKolesar, yKolesar = kolesar.x(), kolesar.y()
    if random.random() < 0.02 and len(ovire) <= 20:
        x = random.randint(0, maxX - sirina)
        ovire.insert(0, [risar.pravokotnik(x, -25, x + sirina, 0, zaobljen=4), sirina, True])
        
    if random.random() < 0.01:
        nagrada, tocke_in_coords = random.choice(list(nagrade_options.items()))
        tocke, (ndx, ndy) = tocke_in_coords
        nx = random.randint(0, maxX - ndx)
        nagrade.insert(0, [risar.slika(nx, -67, absolute_path + nagrada), tocke_in_coords, True])
        
    for ovira_info in ovire:
        ovira, sirina, hitable = ovira_info
        x, y = ovira.x(), ovira.y()
        if y >= maxY:
            ovire.pop()
            risar.odstrani(ovira)
        else:
            ovira.setPos(x, y+1)
        if hitable and((x < xKolesar + 5 < x + sirina or x < xKolesar + 35 < x + sirina) and (y < yKolesar + 27 < y + 25 or y < yKolesar + 57 < y + 25)):
            ovira_info[2] = False
            zivljenja -= 1
            lives.setPlainText(str(zivljenja))
            if zivljenja <= 0:
                fail = True
                
    for nagrada_info in nagrade:
        nagrada, (tocke, (ndx, ndy)), hitable = nagrada_info
        x, y = nagrada.x(), nagrada.y()
        if y >= maxY:
            nagrade.pop()
            if hitable:
                risar.odstrani(nagrada)
        else:
            nagrada.setPos(x, y+1)
            
        if hitable and((x < xKolesar + 5 < x + ndx or x < xKolesar + 35 < x + ndx) and (y < yKolesar + 27 < y + ndy or y < yKolesar + 57 < y + ndy)): 
            nagrada_info[2] = False
            score += tocke
            score_board.setPlainText(str(score))
            collect.play()
            risar.odstrani(nagrada)
        
    if fail:
        music.stop()
        end.play()
        break  
        
    if risar.desno() and xKolesar < maxX - 40: kolesar.setPos(xKolesar + 1, yKolesar)
    elif risar.levo() and xKolesar > 0: kolesar.setPos(xKolesar - 1, yKolesar)
    risar.cakaj(0.002)

risar.stoj()