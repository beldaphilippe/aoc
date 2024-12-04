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

bool str_comp(char* s1, char* s2) {
    int i = 0;
    while ((s1[i] != '\0') && (s2[i] != '\0')) {
        if (s1[i] != s2[i])
            return false;
        i++;
    }
    if (s1[i] != s2[i])
        return false;
    return true;
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

char **split(char* line, char* delimiters) {
    char **split_line = malloc(sizeof(char *) * 1000);
    int k = 0; // position in line
    int j = 0; // index of current word
    int l = 0; // length of current word
    char cword[100]; // current word being read
    while (true) {
        if ((is_in_char(line[k], delimiters)) || (line[k] == '\0')) {
            if (l != 0) {
                cword[l] = '\0';
                split_line[j] = malloc(sizeof(char)*(l+1));
                paste(cword, split_line[j]);
                l = 0;
                j++;
            }
            if (line[k] == '\0') break;
        } else {
            cword[l] = line[k];
            l++;
        }
        k++;
    }
    split_line[j] = malloc(sizeof(char));
    split_line[j][0] = '\0';
    return split_line;
}

char** get_lines_file(const char* file_path, const int line_nb, const int line_length) {
    FILE *file_ptr;
    file_ptr = fopen(file_path, "r");
    if (file_ptr == NULL) {
        fprintf(stderr, "the file cannot be opened\n");
    }
    char** txt = malloc(sizeof(char*)*line_nb);
    char ch = fgetc(file_ptr);
    int i = 0; // line index
    int j = 0; // col index
    while (ch != EOF) {
        txt[i] = malloc(sizeof(char)*line_length);
        j = 0;
        while ((ch != '\n') && (ch != EOF)) {
            txt[i][j] = ch;
            ch = fgetc(file_ptr);
            j++;
        }
        txt[i][j] = '\0';
        i++;
        ch = fgetc(file_ptr);
    }
    return txt;
}

char** get_file(const char* file_path, char* delimiters) {
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
