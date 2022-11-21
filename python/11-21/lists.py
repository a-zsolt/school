import os
from termcolor import colored
from colored import stylize


def menu():
    print("1.) Lists")
    print("2.) Tuples")
    print("3.) Sets")
    print("4.) Dictionaries")
    print("5.) Arrays")
    menupont = int(input("Válaszd ki mit szertnél megtanulni:"))

    if menupont < 1 | menupont > 5:
        print("A megadott szám nem szerepel a listába.")
    elif menupont == 1:
        lists()
    elif menupont == 2:
        tuples()
    elif menupont == 3:
        sets()
    elif menupont == 4:
        dictionaries()
    elif menupont == 5:
        arrays()

def lists():
    os.system('cls')
    print("Létrehozunk egy listát a következő kóddal: ")
    lista = ["lists", "tuples", "sets", "dictionaries", "arrays"]
    print(colored("lista = " + str(lista), "green"))
    print("A listát több változó tárolására használhatjuk.")
    print("A lista elemeinek indexe van aminek a számozása nullától kezdődik. (Tehát a mi esetünkben index 0 = lists)")
    print("Egy listában lehetnek duplikált elemek is és külön elemnek fognak számítani.")
    print(" ")

    print("Kiíhatjuk az egész listát vagy csak a kijelölt elemeket index segítségével.")
    print("Egy listában a lista mögé [] + számmal jeöljükk ki az elemet.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(lista)", "green"))
    print(colored("print(lista[1] + ', ' lista[4])", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(lista, "yellow"))
    print(colored(lista[1] + ", " + lista[4], "yellow"))

    print(colored("Metódusok", "underlined"))



    

menu()