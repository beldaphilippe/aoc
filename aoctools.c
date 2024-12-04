#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "aoctools.h"

int abs(int x) {
    if (x >= 0) return x;
    else return -x;
}

void paste(char *src, char *dst) {
    while (*src != '\0') {
        *dst = *src;
        dst++;
        src++;
    }
    *dst = '\0';
}

int times_in(const int val, int* arr, const int length) {
    int cmt = 0;
    for (int i = 0; i<length; i++) {
        if (val == arr[i])
           cmt++;
    }
    return cmt;
}

int arr_length_char(char* arr) {
    int i=0;
    while (arr[i++] != '\0'){}
    return i;
}

int str_to_int(char* word) {
    int x = 0;
    while (*word != '\0') {
        x = 10*x + *word - '0';
        word++;
    }
    return x;
}

bool is_in_char(const char ch, char* l) {
    int length = arr_length_char(l);
    for (int j=0; j<length; j++) {
        if (ch == l[j])
            return true;
    }
    return false;
}

char** my_split(const char* file_path, char* delimiters) {
    FILE *file_ptr;
    file_ptr = fopen(file_path, "r");
    if (file_ptr == NULL) {
        fprintf(stderr, "the file cannot be opened\n");
        return NULL;
    }
    char ch = fgetc(file_ptr);
    char** txt = malloc(sizeof(char*)*10000);
    char cword[100];
    int j=0;
    int i;
    while (ch != EOF) {
        while (is_in_char(ch, delimiters)) {
            ch = fgetc(file_ptr);
        }
        i = 0;
        while ((!(is_in_char(ch, delimiters))) && (ch != EOF)) {
            /*printf("%d : %d : '%c'\n", j, i, ch);*/
            cword[i] = ch;
            i++;
            ch = fgetc(file_ptr);
        }
        cword[i] = '\0';
        txt[j] = malloc(sizeof(char)*arr_length_char(cword));
        paste(cword, txt[j]);
        j++;
    }
    return (char**) txt;
}
