import numpy as np
import matplotlib.pyplot as plt

coordinates = np.loadtxt("meritve.txt", dtype=np.int64)
slika = np.zeros((256, 256), dtype=np.uint8)

rewind = 0
flag = False
while True:
    for _, x, y, dx, dy in coordinates:

        x = x + dx * rewind
        y = y + dy * rewind

        if not(0 <= x <= 255 and 0 <= y <= 255):
            flag = True
            break
    if flag:
        rewind -= 1
        flag = False
    else:
        break

for color, x, y, dx, dy in coordinates:

    x = x + dx * rewind
    y = y + dy * rewind

    slika[x, y] = color

plt.imsave("Pred_Kih.png", slika, cmap="afmhot")
