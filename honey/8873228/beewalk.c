/**
 * beewalk.c
 * Solution to Honeycomb Walk problem
 */

/******************************************************/
// Includes
#include <stdio.h>
#include <stdlib.h>

/******************************************************/
// Typedefs

typedef struct GridTotal {
    int found;
    int total;
} gridtotal_t;

/******************************************************/
// Globals
const int paths[6][2] = { {0, 2}, {1, 1}, {1, -1}, {0, -2}, {-1, -1}, {-1, 1} };

gridtotal_t* totals;

/******************************************************/
// Function decls

// Walk a path from the origin of size n
int walk(int n);

// Walk a path from point (x, y) of size n.
int walk_path(int n, int x, int y);

// Get a pair from the totals "cache".
gridtotal_t* get_pair(int n, int x, int y);

/******************************************************/

int main() {
    int t;
    scanf("%d", &t);

    // this could probably be smaller but whatever
    totals = (gridtotal_t*) malloc(15 * 30 * 30 * sizeof(gridtotal_t));

    for (int i = 0; i < t; ++i) {
        int n;
        scanf("%d", &n);
        printf("%d\n", walk(n));
    }

    free(totals);

    return 0;
}

int walk(int n) {
    return walk_path(n, 0, 0);
}

int walk_path(int n, int x, int y) {
    if (n == 0) {
        return !(x || y);
    }

    int total = 0;
    for (int i = 0; i < 6; ++i) {
        int new_x = x + paths[i][0];
        int new_y = y + paths[i][1];
        if (abs(new_x) + abs(new_y) < 2 * n) {
            gridtotal_t* pair = get_pair(n, new_x, new_y);
            if (!pair->found) {
                pair->total = walk_path(n - 1, new_x, new_y);
                pair->found = 1;
            }
            total += pair->total;
        }
    }

    return total;
}

gridtotal_t* get_pair(int n, int x, int y) {
    x += 14;
    y += 14;
    // definitely got the formula for 3D to 1D coordinate from stack overflow
    return &totals[n + 14 * (x + 28 * y)];
}
