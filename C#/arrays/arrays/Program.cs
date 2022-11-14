/*
             * Tömb: nem elemi adatszerkezet, minden programnyelvaben szerepelnek
             * A tömb meghatározott számú, azonos típusu elemek halmaza. Minden elemre egyértelműen mutat egy index.
             * 
             * Fajtái 1.): Vektorok: egy dimenziós tömb => csak 1 sora van
             *      Alapértelmazetten tömb alatt vektort értünk
             *      
             *      Általánosan: vl["alma", "körte", "banán"]
             *          Ebben a vektorvan stringek vannak, 3 elemű vektor => a vektor hossza 3
             *          Elsö elem (0): alma
             *          Második elem (1): körte
             *          Harmadik elem (2): banán
             *          
             *      Az elemekre indexükkel hivatkozunk
             *      
             *             Stringek: hasonlóak a vektorokhoz, ugyanúgy indexelődnek
             *             
             *                  string gyümölcs = "kiwi"
             *                  (4 hoszzú string)
             *                  Első elem (0): k
             *                  Második elem (1): i
             *                  Harmadik elem (2): w
             *                  Negyedik elem (3): i
             *              
             * Matix: két dimenziós tömb: sorai és oszlopai vannak
             * 
             *  Általánosan: m1| 3, 6, 12, 34, 72 |
             *                 | 1, 1,  9,  3, 21 |
             *                 | 3, 3,  3, 89, 92 |
             *                 
             *              Az m1 ,áteixnak 3 sora van és 5 oszlopa van. Külön indexelődnek a sorok és az oszlopok.
             *               m1| 00, 01, 02, 03, 04 |
             *                 | 10, 11, 12, 13, 14 |
             *                 | 20, 21, 22, 23, 24 |
             *              
             */

using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace arrays
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //vektorok
            char[] chararray = new char[] { 'b', 'd', 'a', 'c' };
            int[] intarray = new int[] { 1, 2, 3, 4, 5, 6, 7 };
            string[] stringarray = new string[] { "Volvo", "BMW", "Audi" };

            //vektor kiiratás
            Console.WriteLine(chararray[2]);
            Console.WriteLine(intarray[0]);
            Console.WriteLine(stringarray[1]);

            //tömb bejárása for ciklussal (while, foreach)
            for(int i=0; i < chararray.Length; i++)
            {
                Console.WriteLine(chararray[i]);
            }

            //while
            int j = 0;
            while(intarray.Length > j)
            {
                Console.WriteLine(intarray[j]);
                j++;
            }

            //for each
            foreach(var k in stringarray)
            {
                Console.WriteLine(k);
            }

            //tömb raandom számokkal
            int[] randomint = new int[50];

            Random r = new Random(420);

            foreach(var x in randomint)
            {
                randomint[x] = r.Next(420);
                Console.WriteLine(randomint[x]);
            }

            string[] niggaarray = new string[] { "Snitch nigga", "Bitch nigga", "thats that shit i dont like" };

            for (int i = 0; i < 69; i++)
            {
                Console.WriteLine(niggaarray[0]);
                Console.WriteLine(niggaarray[2]);
                Console.WriteLine(niggaarray[1]);
                Console.WriteLine(niggaarray[2]);
            }

            //matrix hard code feltöltéés
            int[,] escapethematrix = new int[,]
            {
                { 3, 6, 12 },
                { 1, 1, 9 },
                { 3, 3, 69}
            };

            Console.WriteLine(escapethematrix[2,2]);    

            //összes elem kiiratása
            foreach (var y in escapethematrix)
            {
                Console.WriteLine(y);
            }
            Console.ReadKey();

            //matrix betöltése
            int[,] fillthematrix = new int[3, 3];
            
        }
    }
}
