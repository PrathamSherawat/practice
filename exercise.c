#include<stdio.h>
#include<conio.h>
void main()
{
    int a[10],i=0,j,count=0,k,num;
    printf("enter the number");
    scanf("%d",&num);
    while(num>0)
    {
        count++;
        a[i]=num%10;
        num=num/10;
        i++;
    }
    for(i=count-1;i>=0;i--)
    {
        for(j=i;j>=0;j--)
        {
            printf("%d",a[j]);
        }
        printf("\n");
    }
    getch();

}