import numpy as np
import math
#PART 1

include = '0123456789'
exclude = '0123456789.'


def check_indices_symbol(arr, row, cols):
    for i in cols:
        start_row = row - 1
        start_col = i - 1
        end_row = row + 1
        end_col = i + 1
        if i == 0:
            start_col = i
        if row == 0:
            start_row = row
        if row >= arr.shape[0]:
            end_row = row
        if i >= arr.shape[1]:
            end_col = col
        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                try:
                    if arr[r][c] not in exclude:
                        return True
                except Exception as e:
                    print(e)
    return False




with open('inputD3.txt') as f:
    c = f.read()

l = c.split('\n')
semi = np.array([list(i) for i in l])

total = 0
for row in range(semi.shape[0]):
    indexes = []
    col = 0
    while col < semi.shape[1]:
        if semi[row][col] in include:
            indexes.append(col)
            for i in range(col + 1, semi.shape[1]):
                if semi[row][i] not in include:
                    break
                else:
                    indexes.append(i)
        if len(indexes) > 0:

            if check_indices_symbol(semi, row, indexes):
                total += int(''.join(semi[row][indexes]))
                col = indexes[-1] + 1
                indexes = []
            else:
                #indexes = []
                col = indexes[-1] + 1
                indexes = []
        else:
            indexes = []
            col +=1
print(total)

#PART 2
gear = "*"
def check_gear_symbol(arr, row, cols):
    for i in cols:
        start_row = row - 1
        start_col = i - 1
        end_row = row + 1
        end_col = i + 1
        if i == 0:
            start_col = i
        if row == 0:
            start_row = row
        if row >= arr.shape[0]:
            end_row = row
        if i >= arr.shape[1]:
            end_col = col
        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                try:
                    if arr[r][c] in gear:
                        return True, i
                except Exception as e:
                    print(e)
    return False, -1

semi = np.array([list(i) for i in l])
gear_locations = []
number_locs = []
total = 0
for row in range(semi.shape[0]):
    indexes = []
    col = 0
    while col < semi.shape[1]:
        if semi[row][col] == '*':
            gear_locations.append((row, col))
        if semi[row][col] in include:
            indexes.append(col)
            for i in range(col + 1, semi.shape[1]):
                if semi[row][i] not in include:
                    break
                else:
                    indexes.append(i)
        if len(indexes) > 0:
            yes, c = check_gear_symbol(semi, row, indexes)
            if yes:
                num = int(''.join(semi[row][indexes]))
                number_locs.append([num, (row, c)])
                col = indexes[-1] + 1
                indexes = []
            else:
                #indexes = []
                col = indexes[-1] + 1
                indexes = []
        else:
            indexes = []
            col +=1
def find_around_gears(num_locs, loc):
    if loc == (124,25):
        pass
    row_range = list(range(loc[0] - 1, loc[0] + 2))
    col_range = list(range(loc[1] - 1, loc[1] + 2))
    n = []
    for k, v in num_locs:
        if v[0] in row_range and v[1] in col_range:
            n.append(k)
    if len(n) != 2:
        return 0
    else:
        return math.prod(n)

total = 0
for i in gear_locations:
    total += find_around_gears(number_locs, i)
print(total)
pass