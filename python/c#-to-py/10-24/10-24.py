def menuvalaszto():
    print("Válassz a következő menüből 1-5-ig")
    print("-----------------")
    print("1.) Derékszögű háromszög szerkezthető-e az adatokból?")
    print("2.) elsőfokú egyenlet megoldó program")
    print("3.) Páros számok 1-121 között")
    print("4.) 7-el osztható számok 71-200 között")
    print("5.) 7-el osztható, páros számok 71-200 között")

    menupont = input()

    if menupont < 1 | menupont > 5:
        print("A megadott szám nem szerepel a listába.")
    elif menupont == 1:
        haromszog()
    elif menupont == 2:
        elsofoku()
    elif menupont == 3:
        paros()
    elif menupont == 4:
        het()
    elif menupont == 5:
        hetpar()

def haromszog():
    print("Add meg a hármoszög A oldalát:") 
    a = int(input()) 
    print("Add meg a háromszög B oldalát:") 
    b = int(input())
    print("Add meg a háromszög C oldalát:") 
    c = int(input())

    print("------------") 
    print("a = " + a + " b = " + b + " c = " + c) 
    print("------------") 

    if (a + b > c)
    {
        print("A háromszög nem megszerkeszthető.") 
    }
    else
    {
        double x = a * a + b * b 
        double x2 = c * c 

        if (x == x2)
        {
            print("A háromszög derékszögű és mehglehet szerkeszteni.") 
        }
        else
        {
            print("A hármoszög nem derékszögű de meglehet szerkeszteni.") 
        }
    }

