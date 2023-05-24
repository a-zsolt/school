import random

def listaletrehoz():
    lista = []

    i = 0
    while i < 100:
        lista.append(random.randint(0,500))
        i+=1

    return(lista)

def haromalosztahto(szamok):
    oszthatok = []

    for x in szamok:
        if x % 3 == 0:
            oszthatok.append(x)

    print(oszthatok, f"Hossza {len(oszthatok)}")
    return(len(oszthatok))

haromalosztahto(listaletrehoz())