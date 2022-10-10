using System;
using System.Collections.Generic;
using System.Linq;
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
                Console.WriteLine("Mert a szám kisebb mint 10 " + egesz - 10);
            }else if(egesz > 10)
            {
                Console.WriteLine("Mert a szám nagyobb mint 10");
            }
            
            Console.ReadKey();
        }
    }
}
