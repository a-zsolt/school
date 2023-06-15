import math

def Tavolsag(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(Tavolsag(1, 1, 2, 2))

x1 = input('Az őrző koordinátája (x,y): ')

x2 = input('Az aes sedai koordinátája (x,y): ')

orzo_cord = x1.split(',')
aessedao_cord = x2.split(',')

tavolsag = round(Tavolsag(int(orzo_cord[0]), int(orzo_cord[1]), int(aessedao_cord[0]), int(aessedao_cord[1])))

print(f'Az őrző az aes sedaitól {tavolsag} km távolságra vannak egymástól.')
print(f'Közöttük {math.floor(tavolsag / 3)} trallok található. ')

