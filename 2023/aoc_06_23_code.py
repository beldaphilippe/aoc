#%% PART ONE

from math import sqrt
from math import ceil

with open('aoc_06_23_input.txt') as f:
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
        if text[i] in digits:
            k,j = '', 0
            while i+j < len(text) and text[i+j] in digits:
                k += text[i+j]
                j += 1
            nbs.append(int(k))
            i = i+j+1
        else:
            i += 1
    return nbs

times = get_all_nbs(text[0][11:])
dists = get_all_nbs(text[1][11:])

result = 1
for t,r in zip(times,dists):
    x1 = ceil(t/2-sqrt(t**2/4-r))
    x2 = int(t/2+sqrt(t**2/4-r))
    result *= x2 - x1 + 1

print(result)


#%% PART TWO

from math import sqrt
from math import ceil

with open('aoc_06_23_input.txt') as f:
    text = f.readlines()
l = []
for line in text:
    l.append(line.strip())
text = l


def erase_spaces(text):
    res = ''
    for l in text:
        if l != ' ':
            res += l
    return res

t = int(erase_spaces(text[0][5:]))
r = int(erase_spaces(text[1][11:]))

x1 = ceil(t/2-sqrt(t**2/4-r))
x2 = int(t/2+sqrt(t**2/4-r))

print(x2 - x1 + 1)