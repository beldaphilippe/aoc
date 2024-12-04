#%% PART ONE

from aoc_structures import *

text = load_file('aoc_10_23_input.txt')

def find(l, text):
    for i,line in enumerate(text):
        for j,letter in enumerate(line):
            if letter == l:
                return (i,j)
    return (-1,-1)

def next_step(coord, coming_from): 
    (p,(i,j)) = coord
    if p=='S':
        if j!=0 and text[i][j-1] in ['-','L','F']:
            return text[i][j-1],(i,j-1)
        elif j!=n-1 and text[i][j+1] in ['-','7','J']:
            return text[i][j+1],(i,j+1)
        elif i!=0 and text[i-1][j] in ['|','7','F']:
            return text[i-1][j],(i-1,j)
        elif i!=n-1 and text[i+1][j] in ['|','L','J']:
            return text[i+1][j],(i+1,j)
    elif p=='|':
        if coming_from=='N':
            return text[i+1][j],(i+1,j)
        elif coming_from=='S':
            return text[i-1][j],(i-1,j)
    elif p=='-':
        if coming_from=='W':
            return text[i][j+1],(i,j+1)
        elif coming_from=='E':
            return text[i][j-1],(i,j-1)
    elif p=='L':
        if coming_from=='N':
            return text[i][j+1],(i,j+1)
        elif coming_from=='E':
            return text[i-1][j],(i-1,j)
    elif p=='J':
        if coming_from=='N':
            return text[i][j-1],(i,j-1)
        elif coming_from=='W':
            return text[i-1][j],(i-1,j)
    elif p=='7':
        if coming_from=='W':
            return text[i+1][j],(i+1,j)
        elif coming_from=='S':
            return text[i][j-1],(i,j-1)
    elif p=='F':
        if coming_from=='E':
            return text[i+1][j],(i+1,j)
        elif coming_from=='S':
            return text[i][j+1],(i,j+1)

direction = {(1,0,):'N', (0,-1):'E', (-1,0):'S', (0,1):'W',}

n, pipe = 0, ('S', find('S', text))
coming_from = ''
while n==0 or pipe[0] != 'S':
    pipe_next = next_step(pipe, coming_from)
    coming_from = direction[(pipe_next[1][0]-pipe[1][0],pipe_next[1][1]-pipe[1][1])]
    pipe = pipe_next
    n += 1

print(int(n/2))

#%% PART TWO

from aoc_structures import *

text = load_file('aoc_10_23_input.txt')

def find(l, text):
    for i,line in enumerate(text):
        for j,letter in enumerate(line):
            if letter == l:
                return (i,j)
    return (-1,-1)

def next_step(coord, coming_from): 
    (p,(i,j)) = coord
    if p=='S':
        if j!=0 and text[i][j-1] in ['-','L','F']:
            return text[i][j-1],(i,j-1)
        elif j!=n-1 and text[i][j+1] in ['-','7','J']:
            return text[i][j+1],(i,j+1)
        elif i!=0 and text[i-1][j] in ['|','7','F']:
            return text[i-1][j],(i-1,j)
        elif i!=n-1 and text[i+1][j] in ['|','L','J']:
            return text[i+1][j],(i+1,j)
    elif p=='|':
        if coming_from=='N':
            return text[i+1][j],(i+1,j)
        elif coming_from=='S':
            return text[i-1][j],(i-1,j)
    elif p=='-':
        if coming_from=='W':
            return text[i][j+1],(i,j+1)
        elif coming_from=='E':
            return text[i][j-1],(i,j-1)
    elif p=='L':
        if coming_from=='N':
            return text[i][j+1],(i,j+1)
        elif coming_from=='E':
            return text[i-1][j],(i-1,j)
    elif p=='J':
        if coming_from=='N':
            return text[i][j-1],(i,j-1)
        elif coming_from=='W':
            return text[i-1][j],(i-1,j)
    elif p=='7':
        if coming_from=='W':
            return text[i+1][j],(i+1,j)
        elif coming_from=='S':
            return text[i][j-1],(i,j-1)
    elif p=='F':
        if coming_from=='E':
            return text[i+1][j],(i+1,j)
        elif coming_from=='S':
            return text[i][j+1],(i,j+1)

direction = {(1,0,):'N', (0,-1):'E', (-1,0):'S', (0,1):'W',}

n, pipe = 0, ('S', find('S', text))
coming_from = ''
while n==0 or pipe[0] != 'S':
    pipe_next = next_step(pipe, coming_from)
    coming_from = direction[(pipe_next[1][0]-pipe[1][0],pipe_next[1][1]-pipe[1][1])]
    pipe = pipe_next
    n += 1

print(int(n/2))
