#include <stdio.h>
#include <stdbool.h>

int abs(int x) {
    if (x >= 0) { return x; } else { return -x; }
}

bool is_in(const int i, int* l, const int length) {
    for (int j=0; j<length; j++) {
        if (i == l[j])
            return true;
    }
    return false;
}

char** my_split(const char* file_path, const char* delimiters) {
    FILE *file_ptr;
    file_ptr = fopen(file_path, "r");
    if (file_ptr == NULL) {
        fprintf(stderr, "the file cannot be opened\n");
    ch =
    
}


char** split(char* line, char* delimiters) {
  const int MAX_NOTES = 5;
  char **split_line = malloc(sizeof(char *) * (MAX_NOTES + 1));
  for (int i = 0; i < MAX_NOTES + 1; i++)
    split_line[i] = NULL;
  int i = 0;
  int w_n = 0;
  while (line[i] != '\0') {
    int w_start = i;
    while (line[i] != delimiter && line[i] != '\0') {
      i++;
    }
    if (w_start != i) {
      int tmp = line[i];
      line[i] = '\0';
      split_line[w_n] = malloc(sizeof(char) * (i - w_start + 1));
      paste(&line[w_start], split_line[w_n]);
      line[i] = tmp;
      w_n++;
    } else
      i++;
  }
  split_line[w_n] = malloc(sizeof(char));
  split_line[w_n][0] = '\0';
  return split_line;
}





