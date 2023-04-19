class italok:
    def __init__(self, file):
        self.file = file

    def beolvasas(self):
        data = open(self.file, "r", encoding="utf8").read().replace("\n", ";").split(";")

        while "" in data:
            data.remove("")

        lista = list(data)

        #convert numbers to int
        for i in range(len(data)):
            try:
                lista[i] = float(lista[i])
            except ValueError:
                pass

        return lista

    def termekek_szama(self):
        termekek = self.beolvasas()

        termekek_szorp = []
        for i in termekek:
            if not isinstance(i, (int, float, complex)):
                termekek_szorp.append(i)
        return len(termekek_szorp)
    
    def termekek_legtobb(self):
        termekek = self.beolvasas()

        termekek_szorp = []
        for i in termekek:
            if isinstance(i, (int, float, complex)):
                termekek_szorp.append(i)

        return print("A legtöbb szörp",termekek[termekek_szorp.index(max(termekek_szorp)) + 2], "méghozzá", max(termekek_szorp), "literel")
    
    def termek_atlag_ar(self):
        termekek = self.beolvasas()

        arak = []
        for i in range(2, len(termekek), 3):
            if isinstance(termekek[i], (int, float)):
                arak.append(termekek[i])
        
        atlag_ar = round(sum(arak) / len(arak), 1)
        return print("Átlagos ár:", atlag_ar, "Ft")
    
    def keszlet_erteke(self):
        termekek = self.beolvasas()

        arak = []
        for i in range(2, len(termekek), 3):
            if isinstance(termekek[i], (int, float)):
                arak.append(termekek[i])

        liter = []
        for i in range(1, len(termekek), 2):
            if isinstance(termekek[i], (int, float)):
                liter.append(termekek[i])
        
        keszlet_erteke = round(sum(arak) * sum(liter), 1)
        return print("A készlet értéke:", round(keszlet_erteke / 1000000, 1), "millió Ft")
    
    def atlag_feletti_termekek(self):
        termekek = self.beolvasas()

        arak = []
        for i in range(2, len(termekek), 3):
            if isinstance(termekek[i], (int, float)):
                arak.append(termekek[i])
        
        atlag_ar = round(sum(arak) / len(arak), 1)

        feletti_termekek = []
        for i in range(2, len(termekek), 3):
            if isinstance(termekek[i], (int, float)):
                if termekek[i] > atlag_ar:
                    feletti_termekek.append(termekek[i])

        return print("Átlag feletti termékek:", feletti_termekek)

print("A raktáron", italok("adatok.txt").termekek_szama(), "féle szörp van.")
italok("adatok.txt").termekek_legtobb()
italok("adatok.txt").termek_atlag_ar()
italok("adatok.txt").keszlet_erteke()
italok("adatok.txt").atlag_feletti_termekek()