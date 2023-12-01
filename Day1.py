#PART 1

import re
with open('inputD1.txt') as f:
    txt = f.read()

codes = txt.split('\n')
nums = [''.join(re.findall('\d+', i)) for i in codes]
cal_vals = [int(i[0] + i[-1]) for i in nums]
print(sum(cal_vals))

#PART2
def positioner(s):
    idxs = {}
    for k, v in mapping.items():
        idx = [m.start() for m in re.finditer('('+k+')', s)]
        if len(idx)>1:
            pass
            #print("EXTRA")
        if len(idx):
            idxs[v] = idx
    for k,v in idxs.items():
        for j in v:
            s = s[:j] + k + s[j+1:]
    return s
    pass
mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for i in range(len(codes)):
    codes[i] = positioner(codes[i])
nums = [''.join(re.findall('\d+', i)) for i in codes]
cal_vals = [int(i[0] + i[-1]) for i in nums]
print(sum(cal_vals))
pass

