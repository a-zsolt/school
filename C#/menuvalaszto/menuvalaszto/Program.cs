using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace menuvalaszto
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Válassz a következő menüből 1-5-ig");
            Console.WriteLine("-----------------");
            Console.WriteLine("1.) Derékszögű háromszög szerkezthető-e az adatokból?");
            Console.WriteLine("2.) elsőfokú egyenlet megoldó program");
            Console.WriteLine("3.) Páros számok 1-121 között");
            Console.WriteLine("4.) 7-el osztható számok 71-200 között");
            Console.WriteLine("5.) 7-el osztható, páros számok 71-200 között");

            int menupont = Convert.ToInt16(Console.ReadLine());

            if (menupont < 1 || menupont > 5)
            {
                Console.WriteLine("A megadott szám nem szerepel a listába.");
            }else if (menupont == 1)
            {
                Console.Clear();
                haromszog();
            }else if (menupont == 2)
            {
                Console.Clear();
                elsofoku();
            }
            else if (menupont == 3)
            {
                Console.Clear();
                paros();
            }
            else if (menupont == 4)
            {
                Console.Clear();
                het();
            }
            else if (menupont == 5)
            {
                Console.Clear();
                hetpar();
            }
        }

        static void haromszog()
        {
            Console.WriteLine("Add meg a hármoszög A oldalát:");
            double a = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Add meg a háromszög B oldalát:");
            double b = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Add meg a háromszög C oldalát:");
            double c = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("------------");
            Console.WriteLine("a = " + a + " b = " + b + " c = " + c);
            Console.WriteLine("------------");

            if (a + b > c)
            {
                Console.WriteLine("A háromszög nem megszerkeszthető.");
            }
            else
            {
                double x = a * a + b * b;
                double x2 = c * c;

                if (x == x2)
                {
                    Console.WriteLine("A háromszög derékszögű és mehglehet szerkeszteni.");
                }
                else
                {
                    Console.WriteLine("A hármoszög nem derékszögű de meglehet szerkeszteni.");
                }
            }

            Console.ReadKey();
        } 

        static void elsofoku()
        {
            Console.WriteLine("Add meg az A értékét:");
            double a = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Add meg a B értékét:");
            double b = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("------------");
            Console.WriteLine("a = " + a + " b = " + b);
            Console.WriteLine("------------");

            double x = -(a / b);

            Console.WriteLine("X értéke = " + x);
        }

        static void paros()
        {
            for (int i = 0; i < 122; i+=2)
            {
                Console.WriteLine(i);
            }

            Console.ReadKey();
        }

        static void het()
        {
            for (int i = 71; i < 200; i++)
            {
                int x = Convert.ToInt32(i.ToString().Remove(i.ToString().Length - 1));
                int utolso = i % (10);
                int x2 = utolso * 2; 

                if (x2 / 7 == 0)
                {
                    Console.WriteLine(i);
                }
            }
            Console.ReadKey();
        }

        static void hetpar()
        {
            for (int i = 71; i < 200; i+=2)
            {
                int x = Convert.ToInt32(i.ToString().Remove(i.ToString().Length - 1));
                int utolso = i % (10);
                int x2 = utolso * 2;

                if (x2 / 7 == 0)
                {
                    Console.WriteLine(i);
                }
            }
            Console.ReadKey();
        }
    }
}
