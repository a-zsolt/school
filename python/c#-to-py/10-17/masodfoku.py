from re import X
from turtle import st


def szamitas ():
    #változók bekérése
    a = int(input("Add meg az A változó értékeét: "))
    b = int(input("Add meg a B változó értékét: "))
    c = int(input("Add meg a C vátozó értékét: "))

    print("------------")
    #= 0?
    if a == 0 | b == 0 | c == 0:
        print("Nem adhatsz meg olyan értéket ami =< 0-val")
    else:
        print("a = " + str(a))
        print("b = " + str(b))
        print("c = " + str(c))

    print("------------")

    #x kiszámítása
    xelso = +b + b - 4 * a * c
    x = xelso / 2 * 9

    #x2 kiszámítása
    x2elso = -b - b - 4 * a * c
    x2 = x2elso / 2 * 9

    print("x = " + str(x))
    print("x2 = " + str(x2))

    print("------------")

    #a kiszámított x és x2-vel végeredmény kiszámítása
    eredmeny = a*x2*b*c+x

    print("A végeredmény: " + str(eredmeny))

szamitas()