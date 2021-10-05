//;https://www.hackerrank.com/challenges/c-tutorial-pointer/problem

#include <stdio.h>
// /exemplo
void increment(int *v) {
   (*v)++; // precisa de colchetes para acessar o valor do ponteiro
}

int testaIncrement() {
   int a;
   scanf("%d", &a);
   increment(&a);
   printf("%d\n", a);
   return 0;
}  

// /resolução
void teste (int *a, int *b) {
   int c1 = (*a)+(*b); //ponteiros
// ternary operator
   int c2 = (*a > *b) ? *a -*b : *b -*a; // Se o A foi maior que B, o resultado é A-B, senão, B-A assim não tem resultado negativo

   printf("%d\n", c1);
   printf("%d\n", c2);
   }


int main(int argc, char const *argv[])
{
   int entrada1, entrada2;
   scanf("%d", &entrada1);
   scanf("%d", &entrada2);
   

   teste(&entrada1, &entrada2); //endereços
   return 0;
}


