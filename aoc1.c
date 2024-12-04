#include <stdio.h>
#include <stdlib.h>
#include "aoctools.h"

int comp(const void* x, const void* y) {
    int i1 = *((const int*) x);
    int i2 = *((const int*) y);
    return i1 - i2;
}

int main() {
    char** txt = my_split("input.txt", " \n");
    const int length = 1000;
    int dist = 0;
    int l1[length];
    int l2[length];
    for (int i=0; i<length; i++) {
        l1[i] =  str_to_int(txt[2*i]);
        l2[i] =  str_to_int(txt[2*i+1]);
    }
    qsort(l1, length, sizeof(int), comp);
    qsort(l2, length, sizeof(int), comp);
    for (int i=0; i<length; i++) {
        /*printf("%d, %d\n", str_to_int(txt[2*i]), str_to_int(txt[2*i+1]));*/
        dist += abs(l1[i]-l2[i]);
    }
    printf("Partie 1 : %d\n", dist);

    int sim = 0;
    for (int i=0; i<length; i++) {
        sim += l1[i]*times_in(l1[i], l2, length);
    }
    printf("Partie 2 : %d\n", sim);
    return 0;
}
