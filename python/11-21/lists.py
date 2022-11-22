import os
from termcolor import colored


def menu():
    print("1.) Lists")
    print("2.) Tuples")
    print("3.) Sets")
    print("4.) Dictionaries")
    print("5.) Arrays")
    menupont = int(input("Válaszd ki mit szertnél megtanulni:"))

    if menupont < 1 or menupont > 5:
        print(colored("A megadott szám nem szerepel a listába.", "red"))
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
    print("Egy listában bármilyen típusú változót tárolhatunk.")
    print(" ")

    print("Kiíhatjuk az egész listát vagy csak a kijelölt elemeket index segítségével.")
    print("Egy listában a lista mögé [] + számmal jeöljükk ki az elemet.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(lista)", "green"))
    print(colored("print(lista[1] + ', ' lista[4])", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(lista, "yellow"))
    print(colored(lista[1] + ", " + lista[4], "yellow"))
    print(" ")

    print(colored("Metódusok", attrs=["bold", "underline"]))
    print("A listához tartozó metódusokat a következőképpen tudjuk meghívni:")
    print(" - append()", "|", "Egy elemet ad hozzá a listához.")
    print(" - clear()", "|", "Törli az összes elemet a listából.")
    print(" - copy()", "|", "Másolatot készít a listáról.")
    print(" - count()", "|", "Megszámolja az elemeket a listában.")
    print(" - extend()", "|", "Egy másik listát ad hozzá a listához.")
    print(" - index()", "|", "Megkeresi az elem indexét a listában.")
    print(" - insert()", "|", "Beszúr egy elemet a listába.")
    print(" - pop()", "|", "Törli az utolsó elemet a listából.")
    print(" - remove()", "|", "Törli a megadott elemet a listából.")
    print(" - reverse()", "|", "Megfordítja a listát.")
    print(" - sort()" "|", "Rendezi a listát.")
    print(" ")

    print(colored("Lista hosszúság", attrs=["bold", "underline"]))
    print("A lista hosszúságát a len() metódussal tudjuk meghatározni.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(len(lista))", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(len(lista), "yellow"))
    print(" ")


def tuples():
    os.system('cls')
    print("Létrehozunk egy tuple-t a következő kóddal: ")
    tuple = ("lists", "tuples", "sets", "dictionaries", "arrays")
    print(colored("tuple = " + str(tuple), "green"))
    print("A tuple-t nem lehet módosítani, csak kiolvasni.")
    print("A tuple-t több változó tárolására használhatjuk.")
    print("A tuple elemeinek indexe van aminek a számozása nullától kezdődik. (Tehát a mi esetünkben index 0 = lists)")
    print("Egy tuple-ban lehetnek duplikált elemek is és külön elemnek fognak számítani.")
    print(" ")

    print("Kiíhatjuk az egész tuple-t vagy csak a kijelölt elemeket index segítségével.")
    print("Egy tuple-ban a tuple mögé [] + számmal jeöljükk ki az elemet.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(tuple)", "green"))
    print(colored("print(tuple[1] + ', ' tuple[4])", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(tuple, "yellow"))
    print(colored(tuple[1] + ", " + tuple[4], "yellow"))
    print(" ")

    print(colored("Lista hosszúság", attrs=["bold", "underline"]))
    print("A tuple hosszúságát a len() metódussal tudjuk meghatározni.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(len(tuple))", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(len(tuple), "yellow"))
    print(" ")


def sets():
    os.system('cls')
    print("Létrehozunk egy set-et a következő kóddal: ")
    set = {"lists", "tuples", "sets", "dictionaries", "arrays"}
    print(colored("set = " + str(set), "green"))
    print("A set-et nem lehet módosítani, csak kiolvasni.")
    print("A set-et több változó tárolására használhatjuk.")
    print("A set elemei nicsenek indexelve.")
    print("Egy set-ben nem lehetnek duplikált elemek.")
    print(" ")

    print("Kiíhatjuk az egész set-et.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(set)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(set, "yellow"))


def dictionaries():
    os.system('cls')
    print("Létrehozunk egy dictionary-t a következő kóddal: ")
    dictionary = {
        "lists": "listák",
        "tuples": "tuple-ök",
        "sets": "set-ek",
        "dictionaries": "dictionary-k",
        "arrays": "array-k"
    }
    print(colored("dictionary = " + str(dictionary), "green"))
    print("A dictionary kulcs-érték párokat tárol.")
    print("A dictionary elemei rendszerezve vannak de nem index alapján hanem kulcs neve alapján.")
    print("Egy dictionary-ben nem lehetnek duplikált elemek.")
    print(" ")

    print("Kiíhatjuk az egész dictionary-t vagy csak a kijelölt elemeket a kulcs neve segítségével.")
    print("Egy dictionary-ben a dictionary mögé []-ben a kulcs nevével jeöljük ki az elemet.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(dictionary)", "green"))
    print(colored("print(dictionary[""tuples""] + ', ' dictionary[""arrays""])", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(dictionary, "yellow"))
    print(colored(dictionary["tuples"] + ", " + dictionary["arrays"], "yellow"))
    print(" ")


def arrays():
    os.system('cls')
    print("Létrehozunk egy array-t a következő kóddal: ")
    array = ["lists", "tuples", "sets", "dictionaries", "arrays"]
    print(colored("array = " + str(array), "green"))
    print("Az array-t akkor használjuk ha sok adatot szeretnénk tárolni.")
    print("Az array elemeinek indexe van aminek a számozása nullától kezdődik. (Tehát a mi esetünkben index 0 = lists)")
    print("Egy array-ben lehetnek duplikált elemek is és külön elemnek fognak számítani.")
    print(" ")

    print("Kiíhatjuk az egész array-t vagy csak a kijelölt elemeket index segítségével.")
    print("Egy array-ben az array mögé [] + számmal jeöljükk ki az elemet.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(array)", "green"))
    print(colored("print(array[1] + ', ' array[4])", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(array, "yellow"))
    print(colored(array[1] + ", " + array[4], "yellow"))
    print(" ")

    print(colored("Metódusok", attrs=["bold", "underline"]))
    print("A listához tartozó metódusokat a következőképpen tudjuk meghívni:")
    print(" - append()", "|", "Egy elemet ad hozzá a listához.")
    print(" - clear()", "|", "Törli az összes elemet a listából.")
    print(" - copy()", "|", "Másolatot készít a listáról.")
    print(" - count()", "|", "Megszámolja az elemeket a listában.")
    print(" - extend()", "|", "Egy másik listát ad hozzá a listához.")
    print(" - index()", "|", "Megkeresi az elem indexét a listában.")
    print(" - insert()", "|", "Beszúr egy elemet a listába.")
    print(" - pop()", "|", "Törli az utolsó elemet a listából.")
    print(" - remove()", "|", "Törli a megadott elemet a listából.")
    print(" - reverse()", "|", "Megfordítja a listát.")
    print(" - sort()" "|", "Rendezi a listát.")
    print(" ")


menu()
