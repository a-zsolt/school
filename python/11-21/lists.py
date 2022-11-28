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

    print(colored("Elem kiiratása indexel", attrs=["bold", "underline"]))
    print("Kiíhatjuk az egész listát vagy csak a kijelölt elemeket index segítségével.")
    print("Egy listában a lista mögé [] + számmal jeöljükk ki az elemet.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(lista)", "green"))
    print(colored("print(lista[1] + ', ' lista[4])", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(lista, "yellow"))
    print(colored(lista[1] + ", " + lista[4], "yellow"))
    print(" ")

    print(colored("Elem megváltozatása indexel", attrs=["bold", "underline"]))
    print("Egy listában a lista mögé [] + számmal jeöljükk ki az elemet és mint egy vátltozót módosíthatjuk.")
    print(colored("---------CODE---------", "green"))
    print(colored("lista", "green"))
    print(colored("lista[1] = 'változtatott'", "green"))
    print(colored("lista", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(lista, "yellow"))
    lista[1] = "változtatott"
    print(colored(lista, "yellow"))
    print(" ")

    print(colored("Elem hozzáadása", attrs=["bold", "underline"]))
    print("A lista végéhez hozzáadhatunk egy elemet a .append() metódussal.")
    print(colored("---------CODE---------", "green"))
    print(colored("lista.append('új elem')", "green"))
    print(colored("lista", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    lista.append("új elem")
    print(colored(lista, "yellow"))
    print(" ")

    print(colored("Elem kitörlése", attrs=["bold", "underline"]))
    print("A lista végéről törölhetünk egy elemet a .remove() metódussal.")
    print(colored("---------CODE---------", "green"))
    print(colored("lista.remove('új elem')", "green"))
    print(colored("lista", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    lista.remove("új elem")
    print(colored(lista, "yellow"))
    print(" ")

    print(colored("Egy listán át 'Loop'-ni", attrs=["bold", "underline"]))
    print("Egy listán át tudunk 'Loop'-ni a következőképpen:")
    print(colored("---------CODE---------", "green"))
    print(colored("for x in lista:", "green"))
    print(colored("    print(x)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    for x in lista:
        print(colored(x, "yellow"))
    print(" ")

    print(colored("Lista összehasonlítása", attrs=["bold", "underline"]))
    print("A lista összehasonlítás segít létehozni egy új listát egy másik lista alapján.")
    print("Két listát összehasonlíthatunk a következőképpen:")
    print(colored("---------CODE---------", "green"))
    print(colored("lista1 = ['alma', 'körte', 'szilva', green", "green"))
    print(colored("ujlista = []", "green"))
    print(colored("for x in lista1:", "green"))
    print(colored("    if 'a' in x:", "green"))
    print(colored("        ujlista.append(x)", "green"))
    print(colored("print(ujlista)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    lista1 = ["alma", "körte", "szilva"]
    ujlista = []
    for x in lista1:
        if "a" in x:
            ujlista.append(x)
    print(colored(ujlista, "yellow"))
    print(" ")

    print(colored("Lista rendezése.", attrs=["bold", "underline"]))
    print("A lista rendezéséhez a .sort() metódust használjuk.")
    print("Ennél a példánál a lista elemeit ABC sorrendbe rendezzük.")
    print(colored("---------CODE---------", "green"))
    print(colored("lista.sort()", "green"))
    print(colored("print(lista)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    lista.sort()
    print(colored(lista, "yellow"))
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

    print(colored("Egy touplen át 'Loop'-ni", attrs=["bold", "underline"]))
    print("Egy touplen át tudunk 'Loop'-ni a következőképpen:")
    print(colored("---------CODE---------", "green"))
    print(colored("for x in tuple:", "green"))
    print(colored("    print(x)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    for x in tuple:
        print(colored(x, "yellow"))
    print(" ")

    print(colored("Tuple elem előfordulásának száma.", attrs=["bold", "underline"]))
    print("A tuple-ban az elem előfordulásának számát a .count() metódussal tudjuk meghatározni.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(tuple.count('lists'))", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(tuple.count("lists"), "yellow"))
    print(" ")

    print(colored("Tuple index", attrs=["bold", "underline"]))
    print("A tuple-ban az elem indexét a .index() metódussal tudjuk meghatározni.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(tuple.index('lists'))", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(tuple.index("lists"), "yellow"))
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
    print(" ")

    print(colored("Lista hosszúság", attrs=["bold", "underline"]))
    print("A set hosszúságát a len() metódussal tudjuk meghatározni.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(len(set))", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(len(set), "yellow"))
    print(" ")

    print(colored("Egy set-en át 'Loop'-ni", attrs=["bold", "underline"]))
    print("Egy set-en át tudunk 'Loop'-ni a következőképpen:")
    print(colored("---------CODE---------", "green"))
    print(colored("for x in set:", "green"))
    print(colored("    print(x)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    for x in set:
        print(colored(x, "yellow"))
    print(" ")


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

    print(colored("Lista hosszúság", attrs=["bold", "underline"]))
    print("A dictionary hosszúságát a len() metódussal tudjuk meghatározni.")
    print(colored("---------CODE---------", "green"))
    print(colored("print(len(dictionary))", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    print(colored(len(dictionary), "yellow"))
    print(" ")

    print(colored("Elem hozzáadása", attrs=["bold", "underline"]))
    print("A dictionary-hez új elemet a dictionary[""kulcs""] = érték módszerrel tudunk hozzáadni.")
    print(colored("---------CODE---------", "green"))
    print(colored("dictionary['new'] = 'új elem'", "green"))
    print(colored("print(dictionary)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    dictionary["new"] = "új elem"
    print(colored(dictionary, "yellow"))
    print(" ")

    print(colored("Elem módosítása", attrs=["bold", "underline"]))
    print("A dictionary-ben lévő elemet a dictionary[""kulcs""] = érték módszerrel tudunk módosítani.")
    print(colored("---------CODE---------", "green"))
    print(colored("dictionary['new'] = 'módosított új elem'", "green"))
    print(colored("print(dictionary)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    dictionary["new"] = "módosított új elem"
    print(colored(dictionary, "yellow"))
    print(" ")

    print(colored("Elem törlése", attrs=["bold", "underline"]))
    print("A dictionary-ben lévő elemet a del dictionary[""kulcs""] módszerrel tudunk törölni.")
    print(colored("---------CODE---------", "green"))
    print(colored("del dictionary['new']", "green"))
    print(colored("print(dictionary)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    del dictionary["new"]
    print(colored(dictionary, "yellow"))
    print(" ")
    

    print(colored("Egy dictionary-ben át 'Loop'-ni", attrs=["bold", "underline"]))
    print("Egy dictionary-ben át tudunk 'Loop'-ni a következőképpen:")
    print(colored("---------CODE---------", "green"))
    print(colored("for x in dictionary:", "green"))
    print(colored("    print(x)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    for x in dictionary:
        print(colored(x, "yellow"))
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

    print(colored("Elem hozzáadása az arryhoz.", attrs=["bold", "underline"]))
    print("Az append() metódussal tudunk egy elemet hozzáadni az array-hoz.")
    print(colored("---------CODE---------", "green"))
    print(colored("array.append(""new element"")", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    array.append("new element")
    print(colored(array, "yellow"))
    print(" ")

    print(colored("Elem törlése az arry-ból.", attrs=["bold", "underline"]))
    print("A remove() metódussal tudunk egy elemet törölni az array-ból.")
    print(colored("---------CODE---------", "green"))
    print(colored("array.remove(""new element"")", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    array.remove("new element")
    print(colored(array, "yellow"))
    print(" ")

    print(colored("Egy array-en át 'Loop'-ni", attrs=["bold", "underline"]))
    print("Egy array-en át 'Loop'-ni a következő kóddal tudjuk megtenni:")
    print(colored("---------CODE---------", "green"))
    print(colored("for x in array:", "green"))
    print(colored("    print(x)", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    for x in array:
        print(colored(x, "yellow"))
    print(" ")

    print(colored("Array rendezése.", attrs=["bold", "underline"]))
    print("Az array rendezéséhez a sort() metódust használjuk.")
    print(colored("---------CODE---------", "green"))
    print(colored("array.sort()", "green"))
    print(colored("---------OUTPUT-------", "yellow"))
    array.sort()
    print(colored(array, "yellow"))
    print(" ")

    


menu()
