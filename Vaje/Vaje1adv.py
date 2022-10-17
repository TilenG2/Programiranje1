import math

# a = float(input("Vpisi a: "))
# b = float(input("Vpisi c: "))
# c = float(input("Vpisi b: "))
# try:
#     x1 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
#     x2 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
#     if x1 == x2:
#         print("Enačba ima eno realno rešitev:", x1)
#     else:
#         print("Enačba ima dve realni rešitvi:", x1, "in", x2)
# except ValueError:
#     print("Enačba nima realnih rešitev.")

# i = 1
# while i <= 100:
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7: #"7" in str(i)
#         print("BUM", end = ' ')
#     else:
#         print(i, end = ' ')
#     i += 1

# N = int(input("Vpisi število: "))
# print( (N * (N + 1)) // 2)

# i = 0
# N = int(input("Vpisi število: "))
# while True:
#     if math.pow(i, 2) < N:
#         i += 1
#     elif math.pow(i, 2) == N:
#         print("Število je kvadrat")
#         break
#     else:
#         print("Število ni kvadrat")
#         break

# count = int(input("Vpiši število kock: "))
# N = int(math.sqrt(count)) + 1
# if N * N > count:
#     N -= 1
# print("Potrebujemo škatlo širine", N, "v kateri je prostora še za", count - int(math.pow(N, 2)), "kock")

