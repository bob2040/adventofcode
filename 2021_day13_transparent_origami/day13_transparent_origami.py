"""
Day 13: Transparent Origami
https://adventofcode.com/2021/day/13
"""
import numpy as np


def first_fold_visible_dots(data_path):
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
    # print(max_x, max_y)

    arr = np.zeros((max_y+1, max_x+1))
    # print(arr)

    for x, y in coords:
        arr[y, x] = 1
        if fold_along[0][0] == 'y' and y > fold_along[0][1]:
            arr[y - (y - fold_along[0][1]) * 2, x] = 1
            arr[y, x] = 0
        elif fold_along[0][0] == 'x' and x > fold_along[0][1]:
            arr[y, x - (x - fold_along[0][1]) * 2] = 1
            arr[y, x] = 0

    print(int(np.sum(arr)))


if __name__ == '__main__':
    # first_fold_visible_dots('test')
    first_fold_visible_dots('data_day13')  # 731

