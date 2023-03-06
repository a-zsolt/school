### Órai feladat: - írd meg az "SuperBowl" paraméteres függvényt,
### =============   ami két paraméterrel rendelkezik: "bemenet", "mod"
###               - olvasd be a "SuperBowl.txt" állományt egy listába, majd ezt dolgozd fel:
###               - írd ki a a képernyőre, hogy a "Washington Redskins" hányszor győzött
###               - írd ki a a képernyőre, hogy a "Dallas Cowboys" hányszor vesztett
###               - írd ki a a képernyőre, hogy a "Kansas City Chiefs" győzött-e
###               - válaszd ki, hogy a "Tampa Stadium" hanyadik helyen van a listában
###               állományod neve: "superbowl.py", ezt kell feltöltened ide
import os

def superbowl(bemenet, mod):
    with open(bemenet, mod, encoding="utf8") as f:
        os.system('cls')

        sb = str(f.read()) #file beolvasása

        #Washington Redskins győzelmek száma
        print("Washington Redskins győzelmek száma:", sb.count("Washington Redskins"))

        #Dallas Cowboys vereségek száma
        print("Dallas Cowboys vereségek száma:", sb.count("Dallas Cowboys"))

        #Kansas City Chiefs győzelmek száma
        if sb.count("Kansas City Chiefs") > 0:
            print("Kansas City Chiefs-nek volt győzelme")
        else:
            print("Kansas City Chiefs-nek nem volt győzelme")

        #Tampa Stadium helye
        print("Tampa Stadium helye:", sb.find("Tampa Stadium"))

        sb.close() #file bezárása

superbowl("SuperBowl.txt", "r") #funkció meghívása paraméterekkel