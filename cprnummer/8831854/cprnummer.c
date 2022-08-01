#include <stdio.h>
#include <stdlib.h>

int main() {
    char cpr[12];
    scanf("%s", cpr);

    int nums[12] = {4,3,2,7,6,5,0,4,3,2,1};

    int res = 0;
    for (size_t i = 0; i < 11; ++i) {
        if (cpr[i] != '-') {
            res += nums[i] * (cpr[i] - '0');
        }
    }

    printf("%d\n", res % 11 == 0);
    return 0;
}
