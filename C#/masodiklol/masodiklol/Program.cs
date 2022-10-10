using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace masodiklol
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*OPERÁTOROK:
            
              ÖKÖLSZABÁLY: az operátorok van precedenciája, azaz amúvelet végrahajtási sorrendje.
              (programonként változhat) Ezért zárójelezünk --> így tudjuk szemantikailag helyesen felépíteni az algoritmusokat
              
              matematikai operatorok:
              "<", ">", "==", ">=", "=<", "*", "/", "+", "-", "%"(modulo)

              logikai operátorok:
              Ha a logikai változó értéke igaz, akkor ehhez "1" tartozik,
              ha a logikai változó értéke hamis, akkor ehhez "0" tartozik

              ÉS logikai mművelet "and", "&&", igazság táblázata
              Két logikai ÉS kapcsolata akkor és csak akkor Igaz, ha mindkét logikai változó igaz.

              VAGY logikai művelet "or", "||"
              ------------------------------
              Két logikai vátozó VAGY kapcsolata akkor és csak akkor igaz ha minkettő logokai válozó IGAZ   
             */

            /*I. SZEKVENCIA
              ==========
              Utasítások soros végrehajtása
             */
            string gyumolcs = "alma";
            Console.WriteLine("Gyümölcs neve: " + gyumolcs);

            /*II. ELÁGAZÁSOK
              GyaRAN ELŐFORDUL, hogy nm kell visgálnnk egy állítást, és attól függően, hogy igaz vagy hamis más-más utasítást kell végrhajtenunk.
              Ilyen estekeben elágazást kell használnunk
             */
            int egesz = 69;
            string kedv = "vidám";

            if(egesz == 10)
            {
                Console.WriteLine("X értéke: " + egesz);
            }
            else
            {
                Console.WriteLine("X éréke nem tíz :CC");
                kedv = "szomorú";
            }
            
            if(kedv == "vidám")
            {
                Console.WriteLine("Vidám vagyok :)");
            }
            else
            {
                Console.WriteLine("Nem vagyok vidám :C");
            }

            if(egesz < 10)
            {
                Console.WriteLine("Mert a szám kisebb mint 10 " + Convert.ToInt32(egesz - 10));
            }else if(egesz > 10)
            {
                Console.WriteLine("Mert a szám nagyobb mint 10");
            }


            //switch - case szerkezet
            string auto = "r34";

            switch (auto)
            {
                case "r34":
                    Console.WriteLine("Sheesh aútó");
                    break;
                case "bmw":
                    Console.WriteLine("Vidd már ezt a rákot innen!!!");
                    break;
                default:
                    Console.WriteLine("Nem sheesh autó :C");
                    break;
            }

            /*III. Ciklusok
             
              előtesztelő:
                -for
                -kiterjesztett for: for each
                -while
             hátultesztelő:
                -do - while
             */

            //for ciklus
            for (int i = 1; i < 10; i++)
            {
                Console.WriteLine(i);
            }

            //while ciklus
            int x = 1;
            while (x < 24)
            {
                Console.WriteLine("Poggers amíg x kissebb mint 24. Most járunk: " + x);
                x++;
            }


            Console.ReadKey();
        }
    }
}
