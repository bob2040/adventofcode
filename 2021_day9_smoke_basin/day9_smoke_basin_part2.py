"""
Day 9: Smoke Basin,Part Two
https://adventofcode.com/2021/day/9#part2
"""
import numpy as np


def get_result(data_path):
    with open(data_path, 'r') as f:
        lines = f.read().splitlines()
    arr = np.array([list(line) for line in lines], dtype=int)
    row_n = arr.shape[0]
    col_n = arr.shape[1]

    size_list = []
    temp = []
    for i in range(row_n):
        for j in range(col_n):
            if arr[i, j] != 9 and ((i, j) not in temp):
                te = []
                te.append((i, j))
                size = 0
                while len(te):
                    (i, j) = te.pop(0)
                    if (i, j) in temp:
                        continue
                    temp.append((i, j))
                    size += 1

                    for c in range(j, col_n):
                        r = i
                        if arr[r, c] != 9:
                            te.append((r, c))
                        else:
                            break
                    for c in range(j, -1, -1):
                        r = i
                        if arr[r, c] != 9:
                            te.append((r, c))
                        else:
                            break
                    for r in range(i, row_n):
                        c = j
                        if arr[r, c] != 9:
                            te.append((r, c))
                        else:
                            break
                    for r in range(i, -1, -1):
                        c = j
                        if arr[r, c] != 9:
                            te.append((r, c))
                        else:
                            break
                size_list.append(size)
    # print(size_list)
    basins = np.array(size_list)
    print(np.sort(basins)[::-1][0:3].prod())


if __name__ == '__main__':
    # get_result('test')  # 1134
    get_result('data_day9')  # 891684
