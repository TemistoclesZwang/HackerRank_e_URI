//; https://www.hackerrank.com/challenges/c-tutorial-functions/problem

#include <stdio.h>

int func_1(int a, int b, int c, int d){
   int maiorTemp = a;

   maiorTemp = (maiorTemp > b) ? maiorTemp : b;
   maiorTemp = (maiorTemp > c) ? maiorTemp : c; 
   maiorTemp = (maiorTemp > d) ? maiorTemp : d; 

   return maiorTemp;
}

int main(int argc, char const *argv[])
{
   int entrada1, entrada2, entrada3, entrada4;

   scanf("%d", &entrada1);
   scanf("%d", &entrada2);
   scanf("%d", &entrada3);
   scanf("%d", &entrada4);

   printf("%d\n", func_1(entrada1, entrada2, entrada3, entrada4));

   return 0;

}

