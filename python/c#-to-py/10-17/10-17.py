from enum import auto
import math

def Main ():
    # konzolra kiírás
    print("Hello Python!")

    # változók deklarálása + kiírása
    ido = "Ma reggel"
    szep = "szép az idő"

    print(ido)
    print(szep)

    print(ido + " " + szep)

    #azonos változók egy sorban
    eso, esernyo = "Ha esik", "viszek enyőt"
    print(eso + " " + esernyo)

    #int deklarálása és inicializálsa
    x = 12

    print("x értéke: " + str(x))

    #több int
    a, b = 4, 7
    c = a+b

    print("a értéke: " + str(a))
    print("b értéke: " + str(b))
    print("az összeg: " + str(c))

    #beolvasás konzolról
    szam = input("Adj meg egy számot: ")
    
    print("A bekért szám: " + szam)
    print("A bekért szám típusa:")
    print(type(szam))

    # Feladat: kérd be a usertől a kör sugarát,
    # számítsd ki a kör kerületét és területét,
    # írd ki az eredményt

    pi_erteke = math.pi

    r = int(input("Add meg a kör kerületét: "))
    ker = 2 * r * pi_erteke
    ter = r * r * pi_erteke

    print("A kör területe: " + str(ker))
    print("A kör területe: " + str(ter))

    #I. elágazások
    #-------------
    #IF szerkezet "ha" - akkor

    egesz = 10

    if egesz == 10:
        print("A szám értéke: " + str(egesz))

    #IF - ELSE szerkezet, "ha" - akkor, KÜLÖNBEN
    kedv = "vidám"

    if kedv == "vidám":
        print("A kedvem: " + kedv)
    else: 
        print("Nem vagyok vidám")

    #ELSE - IF szerkezet: több feltételt tudunk vele levizsgálni
    egesz_szam = 12

    if egesz_szam == 12:
        print("A szám értéke: 12")
    elif egesz_szam == 10:
        print("A szám értéke: 10")
    else:
        print("A szám értéke sem 12, sem 10")

    # SWITCH - CASE szerkezet
    auto = "Volvo"

    match auto:
        case "Volvo":
            print("Ez az autó Volvó") 
        case "BMW":
            print("Ez az autó BMW") 
        case _:
            print("Ez az autó nem Volvó") 

    #II. CIKLUSOK
    #------------
    #for ciklus
    for i in range(10):
        print("A ciklusváltozó: " + str(i))

    #while ciklus
    j = 12
    while(j < 24):
        print("A ciklusváltozó: " + str(j))
        j+=2

Main()