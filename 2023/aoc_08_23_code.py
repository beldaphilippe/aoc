#%% PART ONE

with open('aoc_08_23_input.txt') as f:
    text = f.readlines()
l = []
for line in text:
    l.append(line.strip())
text = l

path = text[0]
map_d = {}
for line in text[2:]:
    map_d[line[:3]] = (line[7:10], line[12:15]) #(L,R)

rl = {'L':0, 'R':1}

node, n = 'AAA', 0


while node != 'ZZZ':
    node = map_d[node][rl[path[n%len(path)]]]
    n += 1

print(n)

#%% PART TWO

from functools import reduce
from math import lcm

with open('aoc_08_23_input.txt') as f:
    text = f.readlines()
l = []
for line in text:
    l.append(line.strip())
text = l

path = text[0]
map_d = {}
for line in text[2:]:
    map_d[line[:3]] = (line[7:10], line[12:15]) #(L,R)

rl = {'L':0, 'R':1}

n = 0
nodes = [i for i in map_d if i[2]=='A']


cycles = []
cache = []
for i in nodes:
    node = i
    count = 0
    while node[2]!='Z' or count==0 :
        node = map_d[node][rl[path[count%len(path)]]]
        count += 1
    cycles.append(count)

print(reduce(lcm,cycles))