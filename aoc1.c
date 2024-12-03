#include <stdio.h>
#include <stdlib.h>

int abs(int x) {
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}

int is_in(int* l, const int length, const int i) {
    for (int j=0; j<length; j++) {
        if (i == l[j])
            return 1;
    }
    return 0;
}

int min_nth(int* l, const int length, const int n) {
    int ltmp[n];
    ltmp[0] = 0;
    for (int j=0; j<length; j++) {
        if (l[ltmp[0]] > l[j])
            ltmp[0] = j;
    }
    for (int i=1; i<n; i++) {
        int k = 0;
        for (int j=0; j<length; j++) {
            if ((is_in(ltmp, i, j) != 1) && (l[j] >= l[i-1]) && (l[k] < l[j]))
                k = j;
        }
        ltmp[i] = k;
    }
    return ltmp[n-1];
}

int main() {
    FILE *file_ptr;
    file_ptr = fopen("input.txt", "r");

    if (file_ptr == NULL) {
        printf("error : the file cannot be opened\n");
        return EXIT_FAILURE;
    }

    char ch = fgetc(file_ptr);
    const int length = 1000;
    int l1[length];
    int l2[length];
    int i=0;
    int x=0, y=0;
    while (ch != EOF) {
        while (ch != ' ') {
            x = 10*x + ch - '0';
            ch = fgetc(file_ptr);
        }
        while ((ch = fgetc(file_ptr)) == ' ');
        while ((ch != '\n') && (ch != EOF)) {
            y = 10*y + ch - '0';
            ch = fgetc(file_ptr);
        }
        l1[i] = x;
        l2[i] = y;
        x = 0;
        y = 0;
        i++;
        if (ch != EOF) {
            ch = fgetc(file_ptr);
        }
    }

    int dist = 0;
    for (int i=1; i<=length; i++) {
        dist += abs(l1[min_nth(l1, length, i)] - l2[min_nth(l2, length, i)]);
    }
    printf("%d\n", dist);
}
