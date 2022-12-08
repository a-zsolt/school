import os
import random
import math

os.system("cls")

def menu():
    menupont = int(input("Add meg hogy melyik feladatatot szeretnéd futtatni (1-9):"))

    if menupont < 1 or menupont > 9:
        print("A megadott szám nem szerepel a listába.")
    elif menupont == 1:
        első()
    elif menupont == 2:
        második()
    elif menupont == 3:
        harmadik()
    elif menupont == 4:
        negyedik()
    elif menupont == 5:
        ötödik()
    elif menupont == 6:
        hatodik()
    elif menupont == 7:
        hetedik()
    elif menupont == 8:
        nyolcadik()
    elif menupont == 9:
        kilencedik()

def első():
    os.system("cls")
    print("Első feladat.")
    print("Kérj be egy egész számot, és írd ki a kétszeresét, a heted részét (2 tizedes jegyre kerekítve), a négyzetgyökét (0.5-ödik hatvány), 3-mal osztva a hányados egész részét és a maradékot, és hogy páros vagy páratlan. (Tipp: egy szám egész, ha egyenlő az egészrészével.)")

    szam = input("Adj meg egy egész számot: ")

    #megnézzük, hogy a szám egész-e
    if szam.isdigit():
        print("A megadott szám: ", szam)
    else:
        print("Nem megfelelő számot adtál meg!")
        return

    #ha egész a szám int típusúvá alakítjuk
    szam = int(szam)

    #egyszerű számítások
    print("A megadott szám kétszerese: ", szam * 2)
    print("A megadott szám hetedrésze: ", round(szam / 7, 2))
    print("A megadott szám négyzetgyöke: ", szam ** 0.5)
    print("A megadott szám harmadrésze egészrésze: ", szam // 3)
    print("A maradék ha a számot 3-mal osztjuk: ", szam % 3)
    
    #szám páros-e
    if szam % 2 == 0:
        print("A megadott szám páros.")
    else:
        print("A megadott szám páratlan.")



def második():
    os.system("cls")
    print("Második feladat.")
    print("Írasd ki a következő értékek típusát: 'anya'    5      3.14     [1,2,3]")

    print("'anya' típusa: ", type('anya'))
    print("5 típusa: ", type(5))
    print("3.14 típusa: ", type(3.14))
    print("[1, 2, 3] típusa: ", type([1, 2, 3]))


def harmadik():
    os.system("cls")
    print("Harmadik feladat.")
    print("Kérj be a felhasználótól két számot, amely egy közönséges tört számlálója és nevezője! A program döntse el, hogy az így bevitt tört felírható-e egész számként! Ha igen, írja ki a tört értékét egész számként, ha nem, írja ki: „Nem egész”!")

    szamlalo = input("Add meg egy közönséges tört számlálóját: ")
    nevező = input("Add meg egy közönséges tört nevezőjét: ")

    #megnézzük, hogy a szám egész-e
    if szamlalo.isdigit() & nevező.isdigit():
        print("A megadott tört: ", szamlalo, "/", nevező)
    else:
        print("Nem megfelelő számokat adtál meg!")
        return

    #ha egész a szám int típusúvá alakítjuk
    szamlalo = int(szamlalo)
    nevező = int(nevező)

    #megnézzük, hogy a tört egész-e
    if szamlalo % nevező == 0:
        print("A megadott tört egész szám.")
    else:
        print("A megadott tört nem egész szám.")

def negyedik():
    os.system("cls")
    print("Negyedik feladat.")
    print("Vesszővel és szóközzel elválasztva írasd ki a képernyőre a 100000-nél kisebb négyzetszámokat!")

    #létrehozunk egy üres listát negyzek néven
    negyzetek = [0]

    x = 0
    while x < 1000:
        #ha x nek a négyzete 100000-nél kisebb, akkor hozzáadjuk a listához
        if x * x < 100000:
            negyzetek.append(x)
        x += 1

    #kiíratjuk a kész listát
    print(negyzetek)


def ötödik():
    os.system("cls")
    print("Ötödik feladat.")
    print("Egy listában tároljuk, hogy a focicsapatunk az egyes meccsein nyert, vesztett, vagy döntetlent játszott: [‘ny’, ‘ny’, ‘v’, ‘d’, ‘d’, ‘d’, ‘v’, ‘v’, ‘ny’, ‘ny’, ‘d’]. A győzelemért három, a döntetlenért egy pont jár. Írd ki a képernyőre, hány pontja van a bajnokságban?")

    erdmenyek = ["ny", "ny", "v", "d", "d", "d", "v", "v", "ny", "ny", "d"]
    pontok = 0

    for x in erdmenyek:
        if x == "ny":
            pontok += 3
        elif x == "d":
            pontok += 1

    print("A csapat összesen", pontok, "pontot szerzett.")


def hatodik():
    os.system("cls")
    print("Hatodik feladat.")
    print("Kérd be a és b egész számokat, és írd ki a/b és b/a hányadosokat és azt is, hogy a hányadosok egész számok-e (pl. 3.45 nem egész 7 egész; a törteket a feladatban két tizedes jegyre kerekítve jelenítsd meg), az a hány százaléka b-nek és fordítva.")

    szam1 = int(input("Add meg az első egész számot: "))
    szam2 = int(input("Add meg a második egész számot: "))
    print("A =", szam1, " ", "B =", szam2)

    hanyados = print("A számok hányadosa: ", round(szam1 / szam2 , 2))

    if isinstance(hanyados, int):
        print("A hányados egész szám.")
    else:
        print("A hányados nem egész szám.")

    
def hetedik():
    os.system("cls")
    print("Hetedik feladat.")
    print("Hozz létre egy listát, amelynek elemszáma véletlenszerű 20-40 között, és a lista elemei 1 és 10 közötti véletlen számok (1 és 10 is lehet benne)! Írd ki a lista elemeinek a számát, a legkisebb és a legnagyobb számot, és hogy milyen elemből hány darab van a listában.")

    lista = []

    x = 0
    while x < random.randint(20, 40):
        lista.append(random.randint(1, 10))
        x += 1

    print("A létrehozott lista:", lista)
    print("A lista hossza:", len(lista))
    print("A lista legnagyobb eleme:", max(lista))
    print("A lista legkisebb eleme:", min(lista))
    x = 1
    while x < 10:
        print("A szám", x, "előfordulásainak száma:", lista.count(x))
        x += 1


def nyolcadik():
    os.system("cls")
    print("Nyolcadik feladat.")
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



def kilencedik():
    os.system("cls")
    print("Kilencedik feladat.")
    print("Kérj be a felhasználótól egy óra:perc:másodperc alakú időt, és írd ki a képernyőre, hogy a nap eleje, vagyis 0:0:0 óta hány másodperc telt el!")

    #idő bekérése
    ido = input("Add meg az időt óra:perc:másodperc formátumban: ")

    #idő szétválasztása
    ora = int(ido[0:2])
    perc = int(ido[3:5])
    masodperc = int(ido[6:8])

    #számítások
    masodperc_ora = ora * 3600
    masodperc_perc = perc * 60
    masodperc_masodperc = masodperc
    masodperc_osszesen = masodperc_ora + masodperc_perc + masodperc_masodperc

    print("Az időpont", masodperc_osszesen, "másodperc után van a nap elejétől.")

menu()