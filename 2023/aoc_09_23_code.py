#%% PART ONE

from aoc_structures import *

text = load_file('aoc_09_23_input.txt')

def all_0(l):
    test = True
    for i in l:
        if i!=0:
            test = False
    return test

s = 0
for line in text:
    seq = get_all_nbs(line)
    diff = [seq]
    while not all_0(diff[-1]):
        l = []
        for i in range(len(diff[-1])-1):
            l.append(diff[-1][i+1]-diff[-1][i])
        diff.append(l)
    diff[-1].append(0)
    n = len(diff)
    for i in range(n-2,-1,-1):
        diff[i].append(diff[i][-1]+diff[i+1][-1])
    s += diff[0][-1]
print(s)

#%% PART TWO

from aoc_structures import *

text = load_file('aoc_09_23_input.txt')

def all_0(l):
    test = True
    for i in l:
        if i!=0:
            test = False
    return test

s = 0
for line in text:
    seq = get_all_nbs(line)
    diff = [seq]
    while not all_0(diff[-1]):
        l = []
        for i in range(len(diff[-1])-1):
            l.append(diff[-1][i+1]-diff[-1][i])
        diff.append(l)
    diff[-1].insert(0,0)
    n = len(diff)
    for i in range(n-2,-1,-1):
        diff[i].insert(0,diff[i][0]-diff[i+1][0])
    s += diff[0][0]
print(s)
