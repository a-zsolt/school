class italok:
    def __init__(self, file):
        self.file = file

    def beolvasas(self):
        data = open(self.file, "r", encoding="utf8").read().replace("\n", ";").split(";")

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

        for i in termekek:
            if isinstance(i, (int, float, complex)) == False:
                pass
            else:
                termekek.remove(i)
        return len(termekek), print(termekek)
    

print("A raktáron", italok("adatok.txt").termekek_szama(), "féle szörp van.")