import os
import random
import math

def menu():
    print("1.) Írj programot, amely bekér 8 osztályzatot, eltárolja őket egy listában, majd kiírja őket egy sorban, vesszővel elválasztva. Új sorokba kiírja az összegüket, szorzatukat, átlagukat (két tizedes jegyre kerekítve)!")
    print("2.) Kérj be egy nap nevét a felhasználótól és döntsd el, hogy tényleg egy nap nevét adta-e meg. (Segítségül: tárold el a hét napjait egy listában és vizsgáld meg, hogy amit a felhasználó megadott, az eleme-e ennek a listának.)")
    print("3.) Kérjél be öt számot szóközzel elválasztva a felhasználótól és döntsd el, hogy mennyi van 1 és 10 között!")
    print("4.) Döntsd el egy 100-nál kisebb bekért számról, hogy prímszám-e!")
    print("5.) Adott egy lista: [17, 74, 33, 28, 67, 12, 42, 63]. Írd ki a képernyőre a következő kérdésekre adott válaszokat: melyik az első és az utolsó páros szám, hányadik az első héttel osztható szám, melyik az első 60 és 70 közé eső szám, hányadik elem a 12?")
    print("6.) Ha egy szabályos pénzérmét feldobunk, akkor egyenlő eséllyel lehet fej (F) vagy írás (I) az eredmény. Szimulálj öt pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is! Az eredményt írasd ki a képernyőre a mintának megfelelően! Kérj be a felhasználótól egy tippet, majd szimulálj egy pénzfeldobást és írasd ki, hogy eltalálta-e vagy sem!")
    print("7.) Kérj be egy mondatot, cseréld le az ékezetes betűket az ékezet nélküli párjukra, ill. a hosszú í-t i-re, írasd ki az eredményt! seréld le a kisbetűket nagybetűkre, és azt is írasd ki! Töröld a nagybetűs verzióból az írásjeleket és a szóközöket, és az eredményt írasd ki a képernyőre!")
    print("8.) Kérj be a felhasználótól egy szót és döntsd el, hogy tartalmaz-e magánhangzót! Amennyiben tartalmaz, a program írja ki a „Van benne magánhangzó.” szöveget, különben azt, hogy „Nincs benne magánhangzó.” Figyelj az ékezetes kis- és nagybetűkre is!")
    print("9.) Tanulmányozd a print() használatának eseteit, és jelenítsd meg print függvénnyel 20 és 7 hányadosát a lenti minta szerint! Az elválasztók tabulátorok.")
    menupont = int(input("Add meg hogy melyik feladatatot szeretnéd futtatni (1-9):"))

    if menupont < 1 or menupont > 9:
        print("A megadott szám nem szerepel a listába.")
    elif menupont == 1:
        elso()
    elif menupont == 2:
        masodik()
    elif menupont == 3:
        harmadik()
    elif menupont == 4:
        negyedik()
    elif menupont == 5:
        otodik()
    elif menupont == 6:
        hatodik()
    elif menupont == 7:
        hetedik()
    elif menupont == 8:
        nyolcadik()
    elif menupont == 9:
        kilencedik()


def elso():
    os.system("cls")
    print("Első feladat.")
    print("Írj programot, amely bekér 8 osztályzatot, eltárolja őket egy listában, majd kiírja őket egy sorban, vesszővel elválasztva. Új sorokba kiírja az összegüket, szorzatukat, átlagukat (két tizedes jegyre kerekítve)!")

    #létrehozunk egy üres listát osztályzatoknak
    osztalyzatok = []

    #jegyek bekérése
    while len(osztalyzatok) < 8:
        osztalyzatok.append(int(input("Add meg " + str(len(osztalyzatok) + 1) + ". osztályzatot: ")))

    #számítások
    print("Az osztályzatok:", osztalyzatok)
    print("Az osztályzatok összege:", sum(osztalyzatok))
    print("Az osztályzatok szorzata:", math.prod(osztalyzatok))
    print("Az osztályzatok átlaga:", round(sum(osztalyzatok) / len(osztalyzatok), 2))



def masodik():
    os.system("cls")
    print("Masodik feladat")
    print("Kérj be egy nap nevét a felhasználótól és döntsd el, hogy tényleg egy nap nevét adta-e meg. (Segítségül: tárold el a hét napjait egy listában és vizsgáld meg, hogy amit a felhasználó megadott, az eleme-e ennek a listának.)")

    #hét napjai (ezzel hasonlítjuk össze az inputot)
    hetnapjai = ["hétfő", "hetfo", "kedd", "szerda", "csütörtök", "csutortok", "péntek", "pentek", "szombat", "vasárnap", "vasarnap"]

    #input bekérése
    nap = input("Add meg a napot: ")

    #ellenőrzés
    if nap.lower() in hetnapjai:
        print("A megadott nap a hétben szerepel.")
    else:
        print("A megadott nap a hétben nem szerepel.")


def harmadik():
    os.system("cls")
    print("Harmadik feladat")
    print("3.) Kérjél be öt számot szóközzel elválasztva a felhasználótól és döntsd el, hogy mennyi van 1 és 10 között!")

    #létterhozunk egy üres listát
    szamok = []
    kivalasztot = []

    #számok bekérése
    while len(szamok) < 5:
        szamok.append(int(input("Add meg " + str(len(szamok) + 1) + ". számot: ")))

    for x in szamok:
        if 1 < x < 10:
            kivalasztot.append(x)

    print(len(kivalasztot), "szám van 1 és 10 között")


def negyedik():
    os.system("cls")
    print("Negyedik feladat")
    print("4.) Döntsd el egy 100-nál kisebb bekért számról, hogy prímszám-e!")

    #szám bekérése
    szam = int(input("Adj meg egy száznál kisebb egész számot:"))

    #szamitas
    if szam > 1:
        for x in range(2, szam/2+1):
            if (szam % x) == 0:
                print(szam, "nem prím szám")
                break
        else:
                print(szam, "prím szám")
    else:
        print(szam, "nem prím szám")


def otodik():
    os.system("cls")
    print("Ötödik feladat")
    print("Adott egy lista: [17, 74, 33, 28, 67, 12, 42, 63]. Írd ki a képernyőre a következő kérdésekre adott válaszokat: melyik az első és az utolsó páros szám, hányadik az első héttel osztható szám, melyik az első 60 és 70 közé eső szám, hányadik elem a 12?")
    szamok = [17, 74, 33, 28, 67, 12, 42, 63]

    parosszamok = []
    #páros szám
    for x in szamok:
        if (x % 2) == 0:
            parosszamok.append(x)

    print("Az első páros szám:", parosszamok[0])
    print("Az első páros szám:", parosszamok[len(parosszamok)-1])

    #héttel osztható
    for x in szamok:
        if x % 7 == 0:
            print("Első héttel osztható szám:", x)
            break

    #első 60 és 70 közé eső szám
    for x in szamok:
        if 60 < x < 70:
            print("Az első 60 és 70 közé eső szám:", x)
            break

    print("A 12", str(szamok.index(12)+1) + ".", "a listában.")


def hatodik():
    os.system("cls")
    print("Hatodik feladat")
    print("Ha egy szabályos pénzérmét feldobunk, akkor egyenlő eséllyel lehet fej (F) vagy írás (I) az eredmény. Szimulálj öt pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is! Az eredményt írasd ki a képernyőre a mintának megfelelően! Kérj be a felhasználótól egy tippet, majd szimulálj egy pénzfeldobást és írasd ki, hogy eltalálta-e vagy sem!")

    dobasok = []

    x = 0
    while x < 6:
        dobasok.append(random.choice(['F', 'I']))
        x += 1

    print(dobasok[0], dobasok[1], dobasok[2], dobasok[3], dobasok[4])

    tipp = input("Fej vagy írás (F/I):")
    print("A tipp:", tipp, "a dobás eredménye:", dobasok[5])

    if dobasok[5] == tipp:
        print("Ön nyert.")
    else:
        print("Ön vesztett.")


def hetedik():
    os.system("cls")
    print("Hetedik feladat")
    print("7.) Kérj be egy mondatot, cseréld le az ékezetes betűket az ékezet nélküli párjukra, ill. a hosszú í-t i-re, írasd ki az eredményt! seréld le a kisbetűket nagybetűkre, és azt is írasd ki! Töröld a nagybetűs verzióból az írásjeleket és a szóközöket, és az eredményt írasd ki a képernyőre!")



def nyolcadik():
    os.system("cls")
    print("Nyolcadik feladat")
    print("Kérj be a felhasználótól egy szót és döntsd el, hogy tartalmaz-e magánhangzót! Amennyiben tartalmaz, a program írja ki a „Van benne magánhangzó.” szöveget, különben azt, hogy „Nincs benne magánhangzó.” Figyelj az ékezetes kis- és nagybetűkre is!")


def kilencedik():
    os.system("cls")
    print("Kilencedik feladat")
    print("Tanulmányozd a print() használatának eseteit, és jelenítsd meg print függvénnyel 20 és 7 hányadosát a lenti minta szerint! Az elválasztók tabulátorok.")


menu()