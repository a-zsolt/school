class Vorosrokak:
    #első feladat
    def __init__(self, naptar):
        with open(naptar) as fajl:
            raw = fajl.read().splitlines()

        self.penz = int(raw[0].split(' ')[1])
        self.naptar = [raw[index1].split(' ') for index1 in range(1, len(raw))]
        self.roka_mecsek = []
        self.kedvencek = ['Computerbontok', 'Bohocok', 'Voros_Rokak']

        for x in self.naptar:
            for i in x:
                if i == 'Voros_Rokak':
                    self.roka_mecsek.append(x)

    #második feladat
    def rokaka(self):
        roka_mecsek = []

        for x in self.roka_mecsek:
            roka_mecsek.append(int(x[3]))

        print(f'A Vörös Rókák {len(roka_mecsek)} mérkőzést játszik, a jegyárnak összege {sum(roka_mecsek)} Ft')

    #harmadik feladat
    def rokaminmax(self):
        print(f'Először: {self.roka_mecsek[0][2]}. napon, utoljára: {self.roka_mecsek[-1][2]}. napon')

    #negyedik feladat
    def utolsokedvenc(self):


        kedvencmecs = []

        for x in self.naptar:
            if x[0] in self.kedvencek and x[1] in self.kedvencek:
                kedvencmecs.append(x)

        print(f'Utolsó mérkőzés napja ahol a kedvenc csapatok egymás ellen játszanak: {kedvencmecs[-1][2]}')

    #ötödik feladat
    def jegyek(self):
        vjegyek = self.roka_mecsek
        mjegyek = []
        mnapok = []

        for x in self.naptar:
            if x[0] in self.kedvencek and x[1] !="Voros_Rokak" and x[0] != "Voros_Rokak":
                vjegyek.append(x)

        for x in vjegyek:
            if int(x[3]) < self.penz:
                mjegyek.append(x)
                self.penz = self.penz - int(x[3])

        for x in mjegyek:
            if int(x[2]) not in mnapok:
                mnapok.append(int(x[2]))

        mnapok.sort()
        mnapok = [str(nap) for nap in mnapok]

        print('A következő napokra vesz jegyet:', ' '.join(mnapok))

        #hatodik feladat
        for x in self.kedvencek:
            print(x+':',len([1 for adat in vjegyek if adat[0]==self.kedvencek or adat[1]==self.kedvencek]))











Vorosrokak('naptar.txt').rokaka()
Vorosrokak('naptar.txt').rokaminmax()
Vorosrokak('naptar.txt').utolsokedvenc()
Vorosrokak('naptar.txt').jegyek()