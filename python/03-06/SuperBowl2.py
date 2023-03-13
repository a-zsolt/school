### Órai feladat: - írd meg az "SuperBowl" paraméteres függvényt,
### =============   ami két paraméterrel rendelkezik: "bemenet", "mod"
###               - olvasd be a "SuperBowl.txt" állományt egy listába, majd ezt dolgozd fel:
###               - írd ki a a képernyőre, hogy a "Washington Redskins" hányszor győzött
###               - írd ki a a képernyőre, hogy a "Dallas Cowboys" hányszor vesztett
###               - írd ki a a képernyőre, hogy a "Kansas City Chiefs" győzött-e
###               - válaszd ki, hogy a "Tampa Stadium" hanyadik helyen van a listában
###               állományod neve: "superbowl.py", ezt kell feltöltened ide
###               ------------------------------------------------------------------
###               - Határozd meg és írd ki a képernyőre, higy a döntők során mennyi volt az átlagos
###                 pontkülönbség a két csapat dközött
###                 az átlagot egy tizedesjegyre kerekítve jelentsd meg
###               - Keresd meg, hogy melyik döntőn volt a legtöbb néző!
###               Feltételezheted, hogy nem alakult ki holtverseny

import os

def SuperBowl(bemenet, mod):
    
    #file beolvasása és lista létrehozása, newline karakterek eltávolítása
    data = open(bemenet, mod, encoding="utf8").read().replace("\n", ";").split(";")
    lista = list(data)
    
    #győztesek listája
    gyoztesek = [lista[i] for i in range(10, len(lista), 8)]
    print("Győztesek listája:", gyoztesek, "\n")

    #vesztesek listája
    vesztesek = [lista[i] for i in range(12, len(lista), 8)]
    print("Vesztesek listája:", vesztesek, "\n")

    #pontok listája
    eredmenyek = [lista[i] for i in range(11, len(lista), 8)]
    print("Pontok listája:", eredmenyek, "\n")

    eredmenyek_hasitott = []
    for i in eredmenyek:
        eredmenyek_hasitott.append(i.split("-"))
    print("Pontok listája hasítva:", eredmenyek_hasitott, "\n")

    #eredmény győztes
    eredmenyek_gyoztes = []
    for i in eredmenyek_hasitott:
        eredmenyek_gyoztes.append(int(i[0]))

    print("eredmények_gyoztes:", eredmenyek_gyoztes, "\n")

    #eredmény vesztes
    eredmenyek_vesztes = []
    for i in eredmenyek_hasitott:
        eredmenyek_vesztes.append(int(i[1]))

    print("eredmények_vesztes:", eredmenyek_vesztes, "\n")

    #nézők listája
    nezok = [lista[i] for i in range(15, len(lista), 8)]
    print("Nézők listája:", nezok, "\n")



    #washigton redskins győzelmek száma
    print("Washington Redskins győzelmek száma:", gyoztesek.count("Washington Redskins"))

    #dallas cowboys vereségek száma
    print("Dallas Cowboys vereségek száma:", vesztesek.count("Dallas Cowboys"))

    #kansas city chiefs győzött-e
    if gyoztesek.count("Kansas City Chiefs") > 0:
        print("Kansas City Chiefs-nek volt győzelme")
    else:
        print("Kansas City Chiefs-nek nem volt győzelme")
    
    #tampa stadium helye
    print("Tampa Stadium helye:", lista.index("Tampa Stadium"))

    #átlagos pontkülönbség
    print("Átlagos pontkülönbség:", round((sum(eredmenyek_gyoztes) - sum(eredmenyek_vesztes)) / len(eredmenyek_gyoztes), 1))

    #legtöbb néző
    print("Legtöbb néző:", max(nezok), "Meccs:", lista[lista.index(max(nezok)) - 1],",", lista[lista.index(max(nezok))- 7])
    


SuperBowl("SuperBowl.txt", "r")