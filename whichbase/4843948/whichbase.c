#include <stdio.h>

int convert_base(int, int);

int main() {
    int p;
    scanf("%d", &p);

    for (int i = 0; i < p; ++i) {
        int k, d;
        scanf("%d %d", &k, &d);
        printf("%d %d %d %d\n", k, convert_base(d, 8), d, convert_base(d, 16));
    }

    return 0;
}

int convert_base(int dec, int base) {
    int s = 0, pow = 1;
    while (dec > 0) {
        int digit = dec % 10;
        if (digit >= base) {
            return 0;
        }

        s += digit * pow;
        pow *= base;
        dec /= 10;
    }

    return s;
}
