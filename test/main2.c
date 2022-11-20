#include<stdio.h>

void pattern(int n) 
{
    int i, j;
    for (i = 1; i <= n; i++) 
    {
        for (j = n - i; j >= 1; j--)
            printf(" ");
        
        for (j = 1; j <= i; j++)
            printf("*");

        for (j = 1; j < i; j++)
            printf("*");

        printf("\n");
    }
}

int main()
{
    pattern(5);
    return 0;
}
