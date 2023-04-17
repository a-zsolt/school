szamlalo = int(input("Kérem a számlálót:"))
nevezo = int(input("Kérem a nevezőt:"))

if szamlalo < nevezo:
    print("A tört kissebb, mint egy egész.")
elif szamlalo == nevezo:
    print("A tört egyenlő egy egész számmal.")
else:
    print("A tört nagyobb, mint egy egész.")

