class Zoldsegek:
    def __init__(self, adatok):
        with open(adatok, encoding="utf8") as fajl:
            raw = fajl.read().splitlines()

            self.zoldsegek = [raw[index1].split(';') for index1 in range(0, len(raw))]
            self.arak = []
            self.darab = []

            for x in self.zoldsegek:
                self.darab.append(int(x[0]))

            for x in self.zoldsegek:
                self.arak.append(int(x[2]))

    def termekeksz(self):
        print(f'{len(self.zoldsegek)} termék van raktáron')

    def maxtermek(self):
        legtobb = self.zoldsegek[self.darab.index(max(self.darab))]

        print(f'Legtobb termék: {legtobb[1]} {legtobb[0]}db')

    def atlagtermekar(self):
        print(f'A termékek átlagára: {round(sum(self.arak) / len(self.arak), 2)} Ft')

    def keszletertek(self):
        print(f'A készlet értéke: {round(sum(self.arak) * sum(self.darab) / 1000000, 5)} millió Ft')

    def atlagfelett(self):
        atlagf = []

        for x in self.arak:
            if x > sum(self.arak) / len(self.arak):
                atlagf.append(self.zoldsegek[self.arak.index(x)])

        print('A következő termékek vannak az átlag ár felett:')

        for x in atlagf:
            print(f'                            {x[1]} {x[2]} Ft')


Zoldsegek('adatok.txt').termekeksz()
Zoldsegek('adatok.txt').maxtermek()
Zoldsegek('adatok.txt').atlagtermekar()
Zoldsegek('adatok.txt').keszletertek()
Zoldsegek('adatok.txt').atlagfelett()
