class teglalap:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def kerulet(self):
        return 2 * (self.a + self.b)
    
    def terulet(self):
        return self.a * self.b
    
input = input("Add meg a téglalap oldalait: ").split(" ")
a = int(input[0])
b = int(input[1])
teglalap = teglalap(a, b)

print(f"A téglalap kerülete: {teglalap.kerulet()}")
print(f"A téglalap területe: {teglalap.terulet()}")