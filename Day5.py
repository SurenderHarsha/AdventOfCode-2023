import numpy as np
#PART 1
with open('inputD5Sample.txt') as f:
    c = f.read()

l = c.split('\n')
seeds = l[0].split(' ')[1:]
prev = 2
sets = []
for i,_ in enumerate(l):
    if i>1:
        if _ == '':
            sets.append(l[prev:i])
            prev = i + 1
sets.append(l[prev:])
locs = []
for s in seeds:
    s_num = int(s)
    source = s_num
    dest = None
    for k in sets:
        found_source = False
        for i, _ in enumerate(k):

            if i==0:
                continue
            r = _.split(' ')
            if source in range(int(r[1]), int(r[1])+int(r[2])):
                dest = source - int(r[1]) + int(r[0])
                found_source = True
                source = dest
                break
        if not found_source:
            dest = source
            source = dest
    locs.append(dest)
print(min(locs))


#PART 2
locs = []
for s in seeds:
    s_num = int(s)
    source = s_num
    dest = None
    for k in sets:
        found_source = False
        for i, _ in enumerate(k):

            if i==0:
                continue
            r = _.split(' ')
            if source in range(int(r[1]), int(r[1])+int(r[2])):
                dest = source - int(r[1]) + int(r[0])
                found_source = True
                source = dest
                break
        if not found_source:
            dest = source
            source = dest
    locs.append(dest)
print(min(locs))
pass