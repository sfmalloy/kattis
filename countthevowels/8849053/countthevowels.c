#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    const size_t BUFFER = 81;
    const char* const VOWELS = "aeiou";

    char input[BUFFER];
    fread(input, BUFFER, sizeof(char), stdin);
    input[BUFFER - 1] = 0;
    size_t N = strlen(input);
    
    int total = 0;
    for (size_t i = 0; i < N; ++i) {
        int lower = tolower(input[i]);
        for (size_t v = 0; v < 5; ++v) {
            if (lower == VOWELS[v]) {
                ++total;
                break;
            }
        }
    }

    printf("%d\n", total);

    return 0;
}
