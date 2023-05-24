a_eletkor = int(input("Add meg az első életkort:"))
b_eletkor = int(input("Add meg a második életkort:"))

if a_eletkor > b_eletkor:
    print(f"Az első megadott életkor ({a_eletkor}) nagyobb mint a második ({b_eletkor}).")
elif b_eletkor > a_eletkor:
    print(f"A második megadott életkor ({b_eletkor}) nagyobb mint az első ({a_eletkor}).")
else:
    print("Az első és a második életkor értéke megyegyezik.")