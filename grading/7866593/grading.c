#include <stdio.h>
#include <stdlib.h>

typedef unsigned long u32;

int main() {
    int a,b,c,d,e;
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);

    int grade;
    scanf("%d", &grade);

    if (grade < e)
        printf("F\n");
    else if (grade < d)
        printf("E\n");
    else if (grade < c)
        printf("D\n");
    else if (grade < b)
        printf("C\n");
    else if (grade < a)
        printf("B\n");
    else
        printf("A\n");

    return 0;
}
