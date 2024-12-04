colors = {'blue':2,
          'red':0,
          'green':1}

with open('aoc_02_23_input.txt') as f:
    text = f.readlines()

r = 0

for line in text:
    line = line.strip("\n")
    is_possible = True
    col_set = [0,0,0] # red green blue
    mem = ""
    i = 8
    n = len(line)
    while i<n:
        c=line[i]
        #print(c)
        if c==';':
            if col_set[0]>12 or col_set[1]>13 or col_set[2]>14 :
                is_possible = False
            #print(col_set)
            col_set = [0,0,0]
            i+=1
        elif c in [str(i) for i in range(10)]:
            if line[i+1] in [str(i) for i in range(10)]:
                i+=1
                v=int(c+line[i])
            else:
                v=int(c)
            j=i+2
            while j<n and line[j] not in [',',';']:
                j+=1
            col_set[colors[line[i+2:j]]] = v
            i=j
        else:
            i+=1 
    if col_set[0]>13 or col_set[1]>14 or col_set[2]>12 :
        is_possible = False
    #print(col_set)    
    if is_possible:
        if line[7] in [str(i) for i in range(10)]:
            print(line[5:8])
            r += int(line[5:8])
        elif line[6] in [str(i) for i in range(10)]:
            print(line[5:7])
            r += int(line[5:7])
        else:
            print(line[5])
            r += int(line[5])
print(r)