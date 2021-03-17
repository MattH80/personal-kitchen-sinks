#include <stdio.h>
#include <time.h>
#include <malloc.h>
#define TEN 10
 
/* function to generate and return random numbers. */
int *getRandom( ) {

   int r;// = alloca(TEN);
   r = 15;
 
   return &r;
}
 
/* main function to call above defined function */
int main () {

   /* a pointer to an int */
   int *p;

   p = getRandom();

   printf("%p", p);
 
   return 0;
}