import os

os.system('cls')

l = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
print("Az input lista: ", l)
print("A lista hossza: ", len(l))

for index, elem in enumerate(l):
    print("index:", index, "elem:", elem)

print("\n")

print("A lista összege: ", sum(l))
