class fegyhaz:
    def __init__ (self, orlista, rablista):
        self.orlista = open(orlista, "r", encoding="utf8").read().replace("\n", ";").split(";")
        self.rablista = open(rablista, "r", encoding="utf8").read().replace("\n", ";").split(";")

    def letszam(self):
        print(f"Őrök létszáma a fegyházban: {len(self.orlista)}")
        print(f"Rabok létszáma a fegyházban: {len(self.rablista)}")
        

    def rabkeres(self):
        rab = input("Adja meg a keresett rab azonosítóját: ")
        talalt_rab = []

        for x in self.rablista:
            if x[0:4] == rab:
                talalt_rab.append(x)
            else:
                pass

        if not talalt_rab:
            print(f"A megadott azonosítóval({rab}) nem található rab.")
        else:
            biceps = talalt_rab[0].split(' ')
            print(f"A keresett rab bicepsz mérete: {biceps[1]} cm")

    def orkeres(self):
        fegyor = input("Adja meg a keresett fegyőrnek az azonosítóját: ")
        talalt_or = []

        for x in self.orlista:
            if x[0:4] == fegyor:
                talalt_or.append(x)
            else:
                pass

        if not talalt_or:
            print(f"A megadott azonosítóval({fegyor}) nem található őr.")
        else:
            ob = talalt_or[0].split(' ')
            or_biceps = float(ob[1].replace(',', '.'))

            for x in self.rablista:
                self.rablista[self.rablista.index(x)] = self.rablista[self.rablista.index(x)].split(' ')


            setaltathato_rabok = []

            for x in self.rablista:
                xfloat = float(x[1].replace(',', '.'))
                if xfloat < or_biceps:
                    setaltathato_rabok.append(x[0])

            print(f"A {fegyor} azonosítóval rendelkező fegyőr a következő rabokat viheti levegőztetni: \n {str(setaltathato_rabok)}")



fegyhaz('fegyorok.txt', 'rabok.txt').letszam()
fegyhaz('fegyorok.txt', 'rabok.txt').rabkeres()
fegyhaz('fegyorok.txt', 'rabok.txt').orkeres()
