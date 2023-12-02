import math
#PART 1

game_dict = {}
total_colors = {
    'red': 12,
    'green': 13,
    'blue': 14
}
total = 0
with open("inputD2.txt") as f:
    all_inp = f.read()
games = all_inp.split('\n')
for g in games:
    id, obj = g.split(':')
    actual_id = id.split(' ')[1]
    add_id = True
    for sets in obj.split(';'):
        if len(sets.split(',')) <=1:
            pass
        for item in sets.split(','):
            _, val, key = item.split(' ')
            try:
                if total_colors[key] < int(val):
                    add_id = False
                    break
            except:
                pass
    if add_id:
        total += int(actual_id)
print(total)

#PART 2
sm = 0
for g in games:
    id, obj = g.split(':')
    total = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    actual_id = id.split(' ')[1]
    for sets in obj.split(';'):
        for item in sets.split(','):
            _, val, key = item.split(' ')
            try:
                if total[key] < int(val):
                    total[key] = int(val)
            except:
                pass
    sm += math.prod(total.values())
print(sm)
pass