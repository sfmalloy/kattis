#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        char line[9];
        scanf("%s", line);

        if (!strcmp(line, "P=NP"))
            puts("skipped");
        else {
            long sum = 0;
            char* token = strtok(line, "+");
            char* end;
            while (token) {
                sum += strtol(token, &end, 10);
                token = strtok(NULL, "+");
            }
            
            printf("%ld\n", sum);
        }
    }


//char input[] = "A+bird+came+down+the+walk";
//    printf("Parsing the input string '%s'\n", input);
//    char *token = strtok(input, "+");
//    while(token) {
//        puts(token);
//        token = strtok(NULL, "+");
//    }
// 
//    printf("Contents of the input string now: '");
//    for(size_t n = 0; n < sizeof input; ++n)
//        input[n] ? putchar(input[n]) : fputs("\\0", stdout);
//    puts("'");

    return 0;
}
