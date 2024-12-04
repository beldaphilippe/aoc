#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int abs(int x) {
    if (x >= 0) { return x; } else { return -x; }
}

int arr_length(char* arr) {
    int i=0;
    while (arr[i++] != '\0'){}
    return i;
}

int main() {
    char tab[4] = {'a', 'b', 'c'};
    printf("%d", arr_length(tab));
    return 0;
}
