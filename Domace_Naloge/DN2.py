weight = int(input("Vnesi tezo goriva v tonah: "))
count = 0
gorivo = 0
while weight > 0:
    weight = weight // 3 - 2
    gorivo += weight if weight > 0 else 0
    count += 1
print(count)
print(gorivo)
