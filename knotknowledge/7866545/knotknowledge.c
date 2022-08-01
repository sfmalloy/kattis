#include <stdio.h>
#include <stdlib.h>

typedef unsigned long u32;

int main() {
    u32 N;
    scanf("%lu", &N);

    int all = 0;
    int need = 0;
    int x;
    for (u32 i = 0; i < N; ++i) {
        scanf("%d", &x);
        all += x;
    }

    for (u32 i = 0; i < N - 1; ++i) {
        scanf("%d", &x);
        need += x;
    }

    printf("%d\n", (all - need));
}
