
order = 'AKQJT98765432'
def check_type(hand):
    h, bet = hand.split(' ')
    s = list(set(h))
    counts = {}
    #Five of a kind
    if len(s) == 1:
        return 0
    for j in s:
        counts[j] = h.count(j)

    if 4 in counts.values():
        return 1
    if 3 in counts.values() and 2 in counts.values():
        return 2
    if 3 in counts.values():
        return 3
    if list(counts.values()).count(2) == 2:
        return 4
    if 2 in counts.values():
        return 5
    return 6


with open('inputD7.txt') as f:
    c =  f.read()

l = c.split('\n')
ranks = {i: [] for i in range(7)}
final_ranks = []
for i in l:
    ranks[check_type(i)].append(i.split(' '))
for i in ranks:
    a = sorted(ranks[i], key=lambda hand: [order.index(c) for c in hand[0]])
    for j in a:
        final_ranks.append(j)
sm = 0
for i, _ in enumerate(final_ranks):
    sm += int(_[1]) * (len(final_ranks) - i)
print(sm)

#PART 2
order2 = 'AKQT98765432J'
def check_type2(hand):
    h, bet = hand.split(' ')
    s = list(set(h))
    counts = {}
    #Five of a kind
    if len(s) == 1:
        return 0

    for j in s:
        counts[j] = h.count(j)
    if 'J' in counts.keys():
        repeat = counts['J']
        counts["J"] = 0
        counts[max(counts, key=counts.get)] += repeat

    if 5 in counts.values():
        return 0
    if 4 in counts.values():
        return 1
    if 3 in counts.values() and 2 in counts.values():
        return 2
    if 3 in counts.values():
        return 3
    if list(counts.values()).count(2) == 2:
        return 4
    if 2 in counts.values():
        return 5
    return 6
ranks = {i: [] for i in range(7)}
final_ranks = []
for i in l:
    ranks[check_type2(i)].append(i.split(' '))
for i in ranks:
    a = sorted(ranks[i], key=lambda hand: [order2.index(c) for c in hand[0]])
    for j in a:
        final_ranks.append(j)
sm = 0
for i, _ in enumerate(final_ranks):
    sm += int(_[1]) * (len(final_ranks) - i)
print(sm)
pass