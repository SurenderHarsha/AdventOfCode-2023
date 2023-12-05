with open('inputD4.txt') as f:
    c = f.read()

l = c.split('\n')
winning = [i.split(':')[1].split('|')[0] for i in l]
holding = [i.split(':')[1].split('|')[1] for i in l]


#PART 1
total = 0
for i, _ in enumerate(l):
    w = [k for k in winning[i].strip().split(' ') if k!='']
    h = [k for k in holding[i].strip().split(' ') if k!='']
    count = 0
    for win in w:
        if win in h:
            count += 1
    if count != 0:
        total += 2 ** (count-1)
print(total)

#PART 2
# with open('inputD4Sample.txt') as f:
#     c = f.read()
#
# l = c.split('\n')
# winning = [i.split(':')[1].split('|')[0] for i in l]
# holding = [i.split(':')[1].split('|')[1] for i in l]
totals = []
repeat = {}


# NOT USED TOO SLOW!
def recursive_count(id):
    if len(repeat[id]) == 0:
        return 1
    else:
        s = 0
        for j in repeat[id]:
            s += recursive_count(j)
        return s + 1


for i, _ in enumerate(l):
    w = [k for k in winning[i].strip().split(' ') if k!='']
    h = [k for k in holding[i].strip().split(' ') if k!='']
    count = 0
    for win in w:
        if win in h:
            count += 1
    totals.append(count)
for i, _ in enumerate(l):
    n = totals[i]
    last = min(i + n + 1, len(l) + 1)
    repeat[i+1] = list(range(i+2, last + 1))
    pass
t = 0
copy_r = {}
marks =  []
for k, v in repeat.items():
    copy_r[k] = [0 for j in v]
while True:
    if all(not isinstance(p, list) for k,p in repeat.items()):
        break
    for k,v in repeat.items():
        if isinstance(v, list) and len(v) == 0:
            repeat[k] = 1
        if isinstance(repeat[k], list) and all((k,c) in marks for c,_ in enumerate(repeat[k])):
            repeat[k] = sum(repeat[k]) + 1
        if isinstance(repeat[k], list):
            for j,_ in enumerate(repeat[k]):
                if (k, j) not in marks:
                    if not isinstance(repeat[repeat[k][j]], list):
                        repeat[k][j] = repeat[repeat[k][j]]
                        marks.append((k, j))

    #for j in repeat[k]:
    #    if not isinstance(repeat[j], list):
    #        pass


print(sum(repeat.values()))
pass