#Írj függvényt, ami:
#===================

#1.) egy input fájlt (te írod az "input.txt-t" számok legyenek,
# veszzővel elválasztva) vár, beolvassa a fájlt
# egy listába, majd kiírja a lista elemeit.

#2.) az 1es feladatot paraméteresen oldja meg

#3.) az 1es feladatot oldja meg a fájl közvetlen
#    használatával, a "with" utasítással

#4.) írj függvényt, ami a elsőfokú egyenlet együtthatóit várja paraméterül, és meghatározza a gyökeket

#5.) A másodfokú egynelet eggyüthatóit várja paraméterül, és meghatározza a gyökeket

import os
import math

txt = "input.txt"

def read_input(file):
    with open(file, 'r') as f:
        numbers = f.read()
        numbers = numbers.split(',')
        numbers = [int(i) for i in numbers]
        print(numbers)
        return numbers


def read_input_no_param():
    with open('input.txt', 'r') as f:
        numbers = f.read()
        numbers = numbers.split(',')
        numbers = [int(i) for i in numbers]
        print(numbers)
        return numbers


def elsofoku(m, b):
    if m == 0:
        print("Nincs megoldás az m paraméte rnem lehet 0")
    else:
        x = -b / m
        print("A megadott egyenlet: f(x)=", str(m) + "x +", b)
        print("A megoldás: x=", x)

def masodfoku():
    for x in read_input(txt):
        print(math.sqrt(x))

def menu():
    print("1.) Elsőfokú egyenlet megoldó")
    print("2.) Másodfokú egyenlet megoldó")
    print("3.) File olvasás")
    
    menupont = int(input("Válassz egy menüpontot: "))

    if menupont == 1:
        os.system('cls')
        m = int(input("Add meg az egyenlet m paraméterét: "))
        b = int(input("Add meg az egyenlet b paraméterét: "))
        elsofoku(m, b)
    elif menupont == 2:
        os.system('cls')
        masodfoku()
    elif menupont == 3:
        os.system('cls')
        read_input(txt)
    else:
        print("Nincs ilyen menüpont!")


menu()