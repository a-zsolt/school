# 1. feladat
with open('naptar.txt') as fajl:
    forras = fajl.read().splitlines()
keret = int(forras[0].split(' ')[1])
adatok = [forras[index1].split(' ') for index1 in range(1,len(forras))]
print(keret)
print(adatok)
# a hazai csapat neve, az ellenfél csapatának neve, a nap sorszáma, jegyár
for adat in adatok:
    adat[2]=int(adat[2])
    adat[3]=int(adat[3])

# 2. feladat
print('2. feladat')
arak = [int(adat[3]) for adat in adatok if adat[0]=='Voros_Rokak' or adat[1]=='Voros_Rokak']
print('A Voros_Rokak',len(arak),'mérkőzést játszik, a jegyárak összege',sum(arak),'Ft')

# 3. feladat
print('\n3. feladat')
napok = [adat[2] for adat in adatok if adat[0]=='Voros_Rokak']
napok.sort()
print('Először: '+str(napok[0])+'. napon, utoljára: '+str(napok[-1])+'. napon')

# 4. feladat
print('\n4. feladat')
kedvencek = ['Computerbontok','Bohocok','Voros_Rokak']
napok = [adat[2] for adat in adatok if adat[0] in kedvencek and adat[1] in kedvencek]
napok.sort()
print('Utolsó mérkőzés napja:',napok[-1])

# 5. feladat
print('\n5. feladat')
csoport1 = [adat for adat in adatok if adat[0]=='Voros_Rokak' or adat[1]=='Voros_Rokak']
keret -= sum(arak)
csoport2 = [adat for adat in adatok if (adat[0]=='Computerbontok' or adat[0]=='Bohocok') and adat not in csoport1]
csoport2.sort(key = lambda e:e[3])
index1 = 0
while keret-csoport2[index1][3]>0:
    keret -= adat[3]
csoport1.append(csoport2[index1])
index1 += 1
napok = list({adat[2] for adat in csoport1})
napok.sort()
napok1 = [str(nap) for nap in napok] # a kiíráshoz stringgé kell átalakítani a számokat
print('A következő napokra vesz jegyet:',' '.join(napok1))

# 6. feladat
print('\n6. feladat')
for kedvenc in kedvencek:
    print(kedvenc+':',len([1 for adat in csoport1 if adat[0]==kedvenc or adat[1]==kedvenc]))

print(csoport1)