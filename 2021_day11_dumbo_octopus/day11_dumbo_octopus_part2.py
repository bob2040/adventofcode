"""
Day 11: Dumbo Octopus,Part Two
https://adventofcode.com/2021/day/11#part2
"""
import numpy as np


def first_all_flash(data_path):
    with open(data_path) as f:
        arr = np.array([int(e) for line in f.readlines() for e in list(line.strip())])
        arr.shape = (10, 10)
    # print(arr)
    n = 0
    while True:
        arr += 1
        coods = np.argwhere(arr > 9)
        if coods.size:
            temp = []
            for g in range(coods.shape[0]):
                i = coods[g][0]
                j = coods[g][1]
                arr[i, j] = 0
                temp.append((i, j))
            while len(temp):
                # print(temp)
                (i, j) = temp.pop(0)
                rr = [-1, -1, -1, 0, 0, 1, 1, 1]
                cc = [-1, 0, 1, -1, 1, -1, 0, 1]
                for k in range(8):
                    r = i + rr[k]
                    c = j + cc[k]
                    if 0 <= r < 10 and 0 <= c < 10 and 0 < arr[r, c] < 9:
                        arr[r, c] += 1
                    elif 0 <= r < 10 and 0 <= c < 10 and arr[r, c] >= 9:
                        arr[r, c] = 0
                        temp.append((r, c))
        n += 1
        if np.sum(arr) == 0:
            break
    print(n)


if __name__ == '__main__':
    # first_all_flash('test')  # 195
    first_all_flash('data_day11')  # 244
