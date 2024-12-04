#%% PART ONE

from types import UnionType
from typing import Any


with open('aoc_05_23_input.txt') as f:
    text = f.readlines()
l = []
for line in text:
    l.append(line.strip())
text = l


def get_all_nbs(text):
    digits = [str(i) for i in range(10)]
    nbs = []
    i = 0
    while i < len(text):
        k,j = '', 0
        while i+j < len(text) and text[i+j] in digits:
            k += text[i+j]
            j += 1
        nbs.append(int(k))
        i = i+j+1
    return nbs


seeds = get_all_nbs(text[0][7:])

i = 3
while i < len(text):
    #print(seeds)
    seeds_next = []
    j = 0
    while i+j < len(text) and text[i+j] != '':
        [d_s, s_s, r] = get_all_nbs(text[i+j])
        #print(d_s, s_s, r)
        for n,k in enumerate(seeds):
            if s_s <= k < s_s+r:
                seeds_next.append(d_s + (k-s_s))
                seeds[n] = -1
        j += 1
    for k in seeds:
        if k != -1:
            seeds_next.append(k)
    seeds = seeds_next
    i = i+j+2

print(min(seeds))

#%% PART TWO

from aoc_structures import Interv

with open('aoc_05_23_input.txt') as f:
    text = f.readlines()
l = []
for line in text:
    l.append(line.strip())
text = l


def get_all_nbs(text):
    digits = [str(i) for i in range(10)]
    nbs = []
    i = 0
    while i < len(text):
        k,j = '', 0
        while i+j < len(text) and text[i+j] in digits:
            k += text[i+j]
            j += 1
        nbs.append(int(k))
        i = i+j+1
    return nbs


nbs = get_all_nbs(text[0][7:])
I = []
for i in range(int(len(nbs)/2)):
    I += [[nbs[2*i], nbs[2*i+1]]]
seeds = Interv(I)

i = 3
while i < len(text): # parcours de la carte de conversion donnée
    seeds_next = Interv([])
    seeds_taken = Interv([])
    j = 0
    while i+j < len(text) and text[i+j] != '':
        [d_s, s_s, r] = get_all_nbs(text[i+j])
        Is = Interv([[s_s,r]])
        It = seeds*Is
        seeds_taken += It
        It.move_from(d_s-s_s)
        seeds_next += It
        j += 1
    seeds_next += seeds-seeds_taken
    seeds = seeds_next.copy()
    i = i+j+2

print(seeds.I[0][0])