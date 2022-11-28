def menuvalaszto():
    print("Válassz a következő menüből 1-5-ig")
    print("-----------------")
    print("1.) Derékszögű háromszög szerkezthető-e az adatokból?")
    print("2.) elsőfokú egyenlet megoldó program")
    print("3.) Páros számok 1-121 között")
    print("4.) 7-el osztható számok 71-200 között")
    print("5.) 7-el osztható, páros számok 71-200 között")

    menupont = int(input())

    if menupont < 1 | menupont > 5:
        print("A megadott szám nem szerepel a listába.")
    elif menupont == 1:
        haromszog()
    elif menupont == 2:
        elsofoku()
    elif menupont == 3:
        paros()
    elif menupont == 4:
        het()
    elif menupont == 5:
        hetpar()


def haromszog():
    a = int(input("Add meg a hármoszög A oldalát:"))
    b = int(input("Add meg a háromszög B oldalát:"))
    c = int(input("Add meg a háromszög C oldalát:"))

    print("------------")
    print("a = " + str(a), " b = " + str(b), " c = " + str(c))
    print("------------")

    if a + b > c:
        print("A háromszög nem megszerkeszthető.")
    else:
        x = a * a + b * b
        x2 = c * c

        if x == x2:
            print("A háromszög derékszögű és mehglehet szerkeszteni.")
        else:
            print("A hármoszög nem derékszögű de meglehet szerkeszteni.")


def elsofoku():
    a = int(input("Add meg az A értékét:"))
    b = int(input("Add meg a B értékét:"))

    print("------------")
    print("a = " + str(a), " b = " + str(b))
    print("------------")

    x = -(a / b)

    print("X értéke = " + str(x))


def paros():
    i = 0
    while i < 122:
        print(i)
        i += 2


def het():
    i = 71
    while i < 200:
        if i % 7 == 0:
            print(i)
        i += 1


def hetpar():
    i = 70
    while i < 200:
        if i % 7 == 0:
            print(i)
        i += 2


menuvalaszto()
