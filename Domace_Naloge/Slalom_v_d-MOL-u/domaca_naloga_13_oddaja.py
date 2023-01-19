import risar
import random
(naj_x, naj_y) = risar.maxX, risar.maxY
blockchain = []
while True:
    if random.random() < 0.02 and len(blockchain) <= 20: 
        width = random.randint(30, 80)
        x = random.randint(0, naj_x - width)
        blockchain.append((risar.pravokotnik(x, 0, x + width, 25, zaobljen=2, barva=risar.nakljucna_barva())))
    for block in blockchain:
        y = block.y()
        if y >= naj_x:
            blockchain.remove(block)
            risar.odstrani(block)
        else:
            block.setY(y+1)
    risar.cakaj(0.002)