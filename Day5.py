import numpy as np
#PART 1
with open('inputD5.txt') as f:
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

def find_loc_for_seed(s):
    s_num = int(s)
    source = s_num
    dest = None
    for k in sets:
        found_source = False
        for i, _ in enumerate(k):

            if i == 0:
                continue
            r = _.split(' ')
            if source in range(int(r[1]), int(r[1]) + int(r[2])):
                dest = source - int(r[1]) + int(r[0])
                found_source = True
                source = dest
                break
        if not found_source:
            dest = source
            source = dest
    return dest
#PART 2
def get_for_seed_range(start, end):
    locs = [i for i in map(find_loc_for_seed, [start, (start + end) // 2, end - 1])]
    return locs

g = 100000
seed_ranges = [(int(_), int(_) + int(seeds[i+1])) for i,_ in enumerate(seeds) if i%2==0]
nsr = []
for i in seed_ranges:
    q = list(range(i[0], i[1], g))
    q.append(i[1])
    if q==None:
        pass
    qs = [(q[j], q[j + 1]) for j, _ in enumerate(q) if j != len(q) - 1]
    for j in qs:
        nsr.append(j)
min_loc = 1000000000000000
prev_loc = min_loc + 1
c = 0
seed_ranges = nsr
while True:
    c += 1
    min_idx = -1

    for p,_ in enumerate(seed_ranges):
        locs = get_for_seed_range(_[0], _[1])
        if min(locs) < min_loc:
            min_idx = p
            min_loc = min(locs)
    a = seed_ranges[min_idx]
    seed_ranges = []
    if c > 25:
        break
    prev_loc = min_loc
    seed_ranges.append((a[0], (a[0] + a[1])//2))
    seed_ranges.append(((a[0] + a[1])//2 + 1, a[1]))

print(min(locs))
pass