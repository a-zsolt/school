def karakterek():
    szovegek = []

    while True:
        szoveg = input("Szöveg: ")
        if szoveg == "":
            break
        szovegek.append(szoveg)

    return print("A leghosszabb szöveg: ", max(szovegek, key=len))

karakterek()