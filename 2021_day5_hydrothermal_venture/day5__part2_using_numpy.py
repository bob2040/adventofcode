"""
Day 5: Hydrothermal Venture,Part 2,re-programing it with numpy
https://adventofcode.com/2021/day/5#part2
"""
import numpy as np
import time


def pass_both_xys(data_path):
    with open(data_path, 'r') as f:
        con = f.read().splitlines()
    # print(con)
    for s in con:
        str_both_xys = s.split(' -> ')
        # print(str_both_xys)
        s_xy = list(map(int, str_both_xys[0].split(',')))
        e_xy = list(map(int, str_both_xys[1].split(',')))
        # print(s_xy, e_xy)
        if s_xy[0] <= e_xy[0] and s_xy[1] <= e_xy[1]:
            make_points(s_xy, e_xy)
        else:
            make_points(e_xy, s_xy)


def make_points(xy1, xy2):
    if not (xy1[0] == xy2[0]) and not (xy1[1] == xy2[1]):
        o_matrix[xy2[0]][xy2[1]] += 1
        if xy1[1] > xy2[1]:
            for i in range(xy2[0]-xy1[0]):
                o_matrix[xy1[0]+i][xy1[1]-i] += 1
            return
        if xy1[0] > xy2[0]:
            for i in range(xy1[0]-xy2[0]):
                o_matrix[xy1[0]-i][xy1[1]+i] += 1
            return
        # top left -> bottom right
        for i in range(xy2[0] - xy1[0]):
            o_matrix[xy1[0]+i][xy1[1]+i] += 1
        return
    # left -> right
    for i in range(xy1[0], xy2[0]):
        o_matrix[i][xy1[1]] += 1
    # top -> bottom
    for i in range(xy1[1], xy2[1]):
        o_matrix[xy1[0]][i] += 1
    o_matrix[xy2[0]][xy2[1]] += 1


if __name__ == '__main__':
    start = time.time()
    o_matrix = np.zeros((1000, 1000))
    # print('o_matrix', o_matrix)
    pass_both_xys('data_day5')
    print((o_matrix > 1).sum())  # 17741
    print(time.time() - start)  # 0.5342063903808594
