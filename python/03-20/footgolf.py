import os

def FootGolf(bemenet, mod):
    os.system("cls")
    #file beolvasása és lista létrehozása, newline karakterek eltávolítása
    data = open(bemenet, mod, encoding="utf8").read().replace("\n", ";").split(";")
    
    #ha a fileban több mint 500 sor van bezárjuk
    

    lista = list(data)

    #versenyzők listája
    versenyzok = [lista[i] for i in range(0, len(lista), 11)]

    #nő versenyzők listája
    no_versenyzok = [lista[i] for i in range(0, len(lista), 11) if lista[i+1] == "Noi"]
    
    #női versenyzők aránya
    noi_arany = round(len(no_versenyzok) / len(versenyzok) * 100, 2)

    #pontszámok listája
    #ha i egy szám akkor adjuk hozzá a pontok listához
    pontok = []
    for i in lista:
        if i.isdigit():
            pontok.append(int(i))

    #összeadjuk az első nyolc elemet majd a következő nyolc elemet stb.
    osszegek = []
    for i in range(0, len(pontok), 8):
        osszegek.append(sum(pontok[i:i+8]))


    #megoldások
    print("1. Feladat:", lista, '\n')

    print("2. Feladat: A versenyen", len(versenyzok), "versenyző indult.", "\n")

    print("3. Feladat: A versenyen", noi_arany, "% a női versenyzők aránya.", "\n")

    print("4. Feladat: Bajjnok női versenyző:")
    print("             Név:", versenyzok[osszegek.index(max(osszegek))])
    print("             Egyesület:", lista[osszegek.index(max(osszegek)) * 11 + 2])
    print("             Pontszám:", max(osszegek), "\n")


FootGolf("fob2016.txt", "r")