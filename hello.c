#include <stdio.h>
#include <conio.h>
void main()
{
   int i,j,k=10;
   for(i=1;i<=4;i++)
   {
      for(j=1;j<=i;j++)
      {
         printf("\n");
         printf("%d",k--);

      }
      printf("\n");
   }
   printf("Hello, World!");
   getch();
}
