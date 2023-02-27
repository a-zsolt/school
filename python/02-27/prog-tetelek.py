#Órai feladatok: -Írd meg az "osszeg-fajbol" paraméteres függvényt,
#                -ami két paramétererel rendelkezik: "bemenet", "mod"
#                -olvasd be a "input.txt" állományt egy listába
#                -írd ki a lista elemekek összegét a képernyőre

def osszeg_fajbol(bemenet, mod):
    with open(bemenet, mod) as f:
        numbers = f.read() #file beolvasása
        numbers = numbers.replace('\n', ',') #új sorok eltávolítása
        numbers = numbers.split(',') #számok listába rendezése
        print("Lista összege:", sum([int(i) for i in numbers])) #lista átalakítása int-re, lista összege

osszeg_fajbol("input.txt", "r") #funkció meghívása paraméterekkel