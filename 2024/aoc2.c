#include <stdio.h>
#include <stdlib.h>
#include "aoctools.h"

/*int comp(const void* x, const void* y) {*/
    /*int i1 = *((const int*) x);*/
    /*int i2 = *((const int*) y);*/
    /*return i1 - i2;*/
/*}*/

bool is_safe(int* report, const int length) {
    bool incr;
    int prec = report[0];
    int curr;
    for (int i=1; i<length; i++) {
        curr = report[i];
        if (i == 1) {
            if (prec > curr) incr = false;
            else incr = true;

        }
        if ((4 <= abs(curr - prec)) || (abs(curr - prec) == 0) || ((curr < prec) && incr) || ((curr > prec) && !incr)) {
            return false;
        }
        prec = curr;
    }
    return true;
}

int main_part1() {
    char** txt = get_lines_file("input.txt", 1000, 100);
    int cmt = 0;
    char** cline;
    int cline_int[100];
    int j;
    for (int i=0; i<1000; i++) { // parcours des lignes
        cline = split(txt[i], " ");
        j = 0; // parcours des nbs du report
        while (cline[j][0] != '\0') {
            cline_int[j] = str_to_int(cline[j]);
            j++;
        }
        if (is_safe(cline_int, j))
            cmt++;
    }
    printf("Partie 1 : %d\n", cmt);
    return 0;
}

int main() {
    char** txt = get_lines_file("input.txt", 1000, 100);
    int cmt = 0;
    char** cline;
    int cline_int[100];
    int j;
    bool skipped; // the int to skip has been skipped
    for (int i=0; i<1000; i++) { // parcours des lignes
        cline = split(txt[i], " ");
        j = 0; // parcours des nbs du report
        while (cline[j][0] != '\0') {
            cline_int[j] = str_to_int(cline[j]);
            j++;
        }
        if (is_safe(cline_int, j)) {
            cmt++;
        } else {
            /*const int length = j-1;*/
            int cline_int_alt[(const int) (j-1)];
            for (int k=0; k<j; k++) { // int to skip
                skipped = false;
                for (int id=0; id<j; id++) { // int added to sublist
                    if (id == k) skipped = true;
                    else {
                        if (skipped) cline_int_alt[id-1] = cline_int[id];
                        else cline_int_alt[id] = cline_int[id];
                    }
                }
                if (is_safe(cline_int_alt, j-1)) {
                    cmt++;
                    break;
                }
            }
        }
    }
    printf("Partie 2 : %d\n", cmt);

    /*int sim = 0;*/
    /*for (int i=0; i<length; i++) {*/
        /*sim += l1[i]*times_in(l1[i], l2, length);*/
    /*}*/
    /*printf("Partie 2 : %d\n", sim);*/
    return 0;
}
