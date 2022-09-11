"""
Day 13: Transparent Origami,Part Two
https://adventofcode.com/2021/day/13#part2
"""
import numpy as np


def code_to_camera(data_path):
    with open(data_path, 'r') as f:
        lines = f.readlines()
    # print(lines)
    a = [line.strip() for line in lines if line != '\n']
    # print(a)
    coords = [(int(s.split(',')[0]), int(s.split(',')[1])) for s in a if 'fold' not in s]
    # print(coords)
    b = [s.split()[2] for s in a if 'fold' in s]
    fold_along = [(s.split('=')[0], int(s.split('=')[1])) for s in b]
    # print(fold_along)

    max_x = 0
    max_y = 0
    for x, y in coords:
        max_x = x if max_x <= x else max_x
        max_y = y if max_y <= y else max_y

    arr = np.zeros((max_y+1, max_x+1))
    # print(arr)

    for x, y in coords:
        arr[y, x] = 1

    for t in fold_along:
        if t[0] == 'y':
            arr1, arr2 = np.split(arr, [t[1]], axis=0)
            for i in range(arr2.shape[0]):
                for j in range(arr2.shape[1]):
                    if arr2[i, j] == 1:
                        arr1[t[1]-i, j] = 1
            arr = arr1
        elif t[0] == 'x':
            arr1, arr2 = np.split(arr, [t[1]], axis=1)
            for i in range(arr2.shape[0]):
                for j in range(arr2.shape[1]):
                    if arr2[i, j] == 1:
                        arr1[i, t[1]-j] = 1
            arr = arr1
    np.savetxt('code', arr, fmt='%d')
    # print(arr)


if __name__ == '__main__':
    # code_to_camera('test')
    code_to_camera('data_day13')  # ZKAUCFUC

