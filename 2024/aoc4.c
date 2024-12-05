#include <stdio.h>
#include <stdlib.h>
#include "aoctools.h"

bool search_word(char** txt, char* word, const int direction) {
    int** DIRECTIONS = {{-1,0}, {-1,1}, {0,1}, {1,1}, {1,0}, {1,-1}, {0,-1}, {-1,-1}};
    if (*word ==
    return search_word(txt, word++, direction);
    else return false;
}

int main() {
    const int HEIGHT = 140;
    const int WIDTH = 140;
    char** txt = get_lines_file("input.txt", HEIGHT, WIDTH);
    int cmt = 0;
    int j; // index of columns
    for (int i=0; i<HEIGHT; i++) {
        for (int j=0; j<WIDTH; j++) {
            if (txt[i][j] == 'X') {
                if (j<WIDTH-4) { // horinzontal search
                    
                }
            }
        }
    }
    return 0;
}
