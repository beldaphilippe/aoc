#ifndef AOCTOOLS_H
#define AOCTOOLS_H

#include <stdbool.h>

int abs(int x);

void paste(char *src, char *dst);

int times_in(const int val, int* arr, const int length);

bool str_comp(char* s1, char* s2);

int arr_length_char(char* arr);

int str_to_int(char* word);

bool is_in_char(const char ch, char* l);

char **split(char* line, char *delimiter);

char** get_lines_file(const char* file_path, const int line_nb, const int line_length);

char** get_file(const char* file_path, char* delimiters);

#endif
