#%% PART ONE

with open('aoc_07_23_input.txt') as f:
    text = f.readlines()
l = []
for line in text:
    l.append(line.strip())
text = l

cards = ['A','K','Q','J','T']+[str(i) for i in range(9,1,-1)]
cards_value = {c:i for i,c in enumerate(cards[::-1])}

def comp_cards(c1, c2):
    if cards_value[c1] <= cards_value[c2]:
        return True
    else:
        return False

def same_cards(h):
    dico = {}
    for c in h:
        if c not in dico:
            dico[c] = 1
        else : dico[c] += 1
    return dico

def hand_type(h):
    dico = same_cards(h)
    n = len(dico)
    if n == 5:
        return 0
    elif n == 4:
        return 1
    elif n == 3 :
        for i in dico:
            if dico[i] == 2:
                return 2
        return 3
    elif n == 2:
        for i in dico:
            if dico[i] == 2:
                return 4
        return 5
    elif n == 1:
        return 6

def comp_hands(h1, h2):
    t1, t2 = hand_type(h1), hand_type(h2)
    if t1 == t2:
        for i in range(5):
            if h1[i] == h2[i]:
                pass
            elif comp_cards(h1[i], h2[i]):
                return True
            else:
                return False
        return True
    elif t1 < t2:
        return True
    else:
        return False
    
def erase_spaces(text):
    res = ''
    for l in text:
        if l != ' ':
            res += l
    return res

def fusion(l1, l2):
    l = []
    n1, n2 = len(l1), len(l2)
    i1, i2 = 0, 0
    while i1<n1 and i2<n2:
        if comp_hands(l1[i1][0], l2[i2][0]):
            l.append(l1[i1])
            i1 += 1
        else:
            l.append(l2[i2])
            i2 += 1
    return l+l1[i1:]+l2[i2:]

def sort_hands(l):
    if len(l)<=1:
        return l
    else:
        return fusion(sort_hands(l[:int(len(l)/2)]), sort_hands(l[int(len(l)/2):]))


cards_input = []
for line in text:
    cards_input.append((line[0:5], int(erase_spaces(line[6:]))))

l = sort_hands(cards_input)
s = 0
for i,(_,b) in enumerate(l):
    s += b*(i+1)

print(s) 

#%% PART TWO

from math import sqrt
from math import ceil

with open('aoc_07_23_input.txt') as f:
    text = f.readlines()
l = []
for line in text:
    l.append(line.strip())
text = l

cards = ['A','K','Q','T']+[str(i) for i in range(9,1,-1)]+['J']
cards_value = {c:i for i,c in enumerate(cards[::-1])}

def comp_cards(c1, c2):
    if cards_value[c1] <= cards_value[c2]:
        return True
    else:
        return False

def same_cards(h):
    dico = {}
    for c in h:
        if c not in dico:
            dico[c] = 1
        else : dico[c] += 1
    return dico

def hand_type(h):
    dico = same_cards(h)
    n = len(dico)
    if 'J' in dico:
        n_j = dico['J']
    else :
        n_j = 0

    pair = False
    for i in dico:
        if dico[i]==2 and i!='J':
            pair = True

    if n==5 and n_j==0: 
        return 0 #nothing
    elif (n==5 and n_j==1) or (n==4 and n_j==0):
        return 1 #one pair
    elif (n==3 and n_j==0 and pair):
        return 2 #two pairs
    elif (n==4 and n_j>0) or (n==3 and n_j==0 and not pair):
        return 3 #three of a kind
    elif (n==3 and n_j==1 and pair) or (n==2 and n_j==0 and pair):
        return 4 #full house
    elif (n==3 and n_j==1 and not pair) or (n==3 and n_j==2 and pair) or (n==3 and n_j==3) or (n==2 and n_j==0 and not pair):
        return 5 #square
    elif (n==2 and n_j>0) or (n==1):
        return 6
    print(h) #non-matching pattern

def comp_hands(h1, h2):
    t1, t2 = hand_type(h1), hand_type(h2)
    if t1 == t2:
        for i in range(5):
            if h1[i] == h2[i]:
                pass
            elif comp_cards(h1[i], h2[i]):
                return True
            else:
                return False
        return True
    elif t1 < t2:
        return True
    else:
        return False
    
def erase_spaces(text):
    res = ''
    for l in text:
        if l != ' ':
            res += l
    return res

def fusion(l1, l2):
    l = []
    n1, n2 = len(l1), len(l2)
    i1, i2 = 0, 0
    while i1<n1 and i2<n2:
        if comp_hands(l1[i1][0], l2[i2][0]):
            l.append(l1[i1])
            i1 += 1
        else:
            l.append(l2[i2])
            i2 += 1
    return l+l1[i1:]+l2[i2:]

def sort_hands(l):
    if len(l)<=1:
        return l
    else:
        return fusion(sort_hands(l[:int(len(l)/2)]), sort_hands(l[int(len(l)/2):]))


cards_input = []
for line in text:
    cards_input.append((line[0:5], int(erase_spaces(line[6:]))))

l = sort_hands(cards_input)
s = 0
for i,(_,b) in enumerate(l):
    s += b*(i+1)

print(s) 