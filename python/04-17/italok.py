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
    

print("A raktáron", italok("adatok.txt").termekek_szama(), "féle szörp van.")