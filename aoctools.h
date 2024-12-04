#ifndef AOCTOOLS_H
#define AOCTOOLS_H

#include <stdbool.h>

int abs(int x);

void paste(char *src, char *dst);

int times_in(const int val, int* arr, const int length);

int arr_length_char(char* arr);

int str_to_int(char* word);

bool is_in_char(const char ch, char* l);

char** my_split(const char* file_path, char* delimiters);

#endif
