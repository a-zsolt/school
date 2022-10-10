using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace masodfoku
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //vátozók létrehozása
            double a, b, c;
            //változók dklarálása
            Console.WriteLine("Add meg az a változó értékét:");
            a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Add meg a b változó értékét:");
            b = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Add meg az c változó értékét:");
            c = Convert.ToInt32(Console.ReadLine());

            //= 0 ?
            if(a == 0 || b ==0 || c == 0)
            {
                Console.WriteLine("Nem adhatsz meg olyna értéket ami =< 0-nál");
            }
            else
            {
                Console.WriteLine("a = " + a + " b = " + b + ", c = " + c);
            }
            Console.WriteLine("-------------");

            double xfirst = -b + b - 4 * a * c;
            double x = xfirst / 2 * 9;

            double x2first = -b - b - 4 * a * c;
            double x2 = x2first/2*9;

            Console.WriteLine("x = " + x);
            Console.WriteLine("x2 = " + x2);
            Console.WriteLine("-------------");

            double eredmeny = a*x2+b*c+x;

            Console.WriteLine("A végeredmény: " + eredmeny);



            Console.ReadKey();
        }
    }
}
