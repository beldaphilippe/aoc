def load_file(path):
    with open(path) as f:
        text = f.readlines()
    l = []
    for line in text:
        l.append(line.strip())
    return l

def get_all_nbs(text):
    digits = ['-']+[str(i) for i in range(10)]
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

class Interv:
    """
    Pour représenter des ensembles d'entiers naturels sous forme d'intervalles.
    self.I est un tableau de deux lignes, la première pour le début de l'intervalle,
    la deuxième pour sa longueur.

    Conv :
        I1+I2 : union
        I1*I2 : intersection
        I1-I2 : privation
    """
    def __init__(self, I):
        I.sort(key=lambda x:x[0]) # on trie la liste par début d'intervalles croissants
        changes = True
        while changes:
            I_fixed = []
            n = 0
            changes = False
            while n < len(I):
                if I[n][1] == 0: # cas où on veut se débarrasser d'un intervalle vide
                    changes = True
                    n += 1
                elif n < len(I)-1 and I[n][0]+I[n][1] >= I[n+1][0]: # on peut simplifier I[n] U I[n+1]
                    I_fixed.append([I[n][0], max(I[n+1][0]-I[n][0]+I[n+1][1], I[n][1])])
                    n += 2
                    changes = True
                else:
                    I_fixed.append(I[n])
                    n += 1
            I = I_fixed
        self.I = I

    def __str__(self):
        s = ''
        if len(self.I)>0:
            s = ''
            for i in self.I[:-1]:
                s += f'[|{i[0]};{i[0]+i[1]-1}|] U '
            i = self.I[-1]
            s += f'[|{i[0]};{i[0]+i[1]-1}|]'
        else:
            s = 'ø'
        return s

    def __mul__(self, interv2): # Intersection
        I = []
        for i1 in self.I:
            for i2 in interv2.I:
                a = max(i1[0], i2[0])
                b = min(i1[0]+i1[1]-1, i2[0]+i2[1]-1)
                if a<=b:
                    I.append([a,b-a+1])
        return Interv(I)
    
    def __add__(self, interv2): # Union
        return Interv(self.I + interv2.I)

    def __sub__(self, interv2): # Privation (I1\I2)
        I2 = interv2.I
        if len(I2)>0:
            Ic = [[0,I2[0][0]]] # Ic complémentaire de I2
            for n in range(len(I2)-1):
                Ic.append([I2[n][0]+I2[n][1], I2[n+1][0]-(I2[n][0]+I2[n][1])])
            a = self.I[-1][0]+self.I[-1][1]
            b = I2[-1][0]+I2[-1][1]
            if a > b:
                Ic.append([b, a-b])
        else:
            Ic = self.I
        return self*Interv(Ic)

    def copy(self):
        return Interv(self.I)
    
    def move_from(self, r): # décale les intervalles de r
        for k in range(len(self.I)):
            self.I[k] = [self.I[k][0]+r, self.I[k][1]]
        
""" TESTS
a = Interv([[1,4],[10,6]])
b = Interv([[2,3],[6,3]])
print(a,'___',b)
print(a*b)
print(a+b)
print(b+a)
print(a-b)
print(b-a)
a.move_from(2)
print(a)
"""