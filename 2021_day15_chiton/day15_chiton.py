"""
Day 15: Chiton
https://adventofcode.com/2021/day/15
"""
import numpy as np
import heapq


def get_total_risk(data_path):
    data = []
    for line in open(data_path):
        data.append([int(sn) for sn in list(line.strip())])
    # print(data)
    arr = np.array(data)
    # print(arr)
    rows = arr.shape[0]
    cols = arr.shape[1]
    x = [-1, 0, 1, 0]
    y = [0, 1, 0, -1]

    temp_arr = np.zeros((rows, cols), dtype=int)
    # print(temp_arr)
    temp_ls = [(0, 0, 0)]
    while temp_ls:
        # print(temp_ls)
        (dist, r, c) = heapq.heappop(temp_ls)
        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue

        rc_cost = dist + arr[r, c]

        if temp_arr[r, c] == 0 or rc_cost < temp_arr[r, c]:
            temp_arr[r, c] = rc_cost
            # print(temp_arr)
        else:
            continue
        if r == rows - 1 and c == cols - 1:
            break

        for n in range(4):
            rr = r + x[n]
            cc = c + y[n]
            heapq.heappush(temp_ls, (temp_arr[r, c], rr, cc))
    # print(temp_arr)
    print(temp_arr[rows - 1, cols - 1] - arr[0, 0])


if __name__ == '__main__':
    # get_total_risk('test')
    get_total_risk('data_day15')  # 366
