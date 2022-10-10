"""
Day 15: Chiton
https://adventofcode.com/2021/day/15
"""
import numpy as np


def get_total_risk(data_path):
    data = []
    for line in open(data_path):
        data.append([int(sn) for sn in list(line.strip())])
    # print(data)
    arr = np.array(data)
    # print(arr)
    i, j = 0, 0
    risk = []
    while True:
        temp1 = []
        temp2 = []
        r1 = [[0, 0, 0], [0, 0, 1], [0, 1, 2], [0, 1, 1]]
        c1 = [[1, 2, 3], [1, 2, 2], [1, 1, 1], [1, 1, 2]]
        r2 = [[r[0]+1, r[1]+1, r[2]+1] for r in r1]
        c2 = [[c[0]-1, c[1]-1, c[2]-1] for c in c1]
        # print(r2)
        # print(c2)
        for m in range(4):
            sum1, sum2 = 0, 0
            d1, d2 = 0, 0
            for n in range(3):
                a = i + r1[m][n]
                b = j + c1[m][n]
                if 0 <= a < arr.shape[0] and 0 <= b < arr.shape[1]:
                    d1 += 1
                    sum1 += arr[a, b]
            # print(d1)
            if d1 >= 2:
                temp1.append(sum1)
            for n in range(3):
                a = i + r2[m][n]
                b = j + c2[m][n]
                if 0 <= a < arr.shape[0] and 0 <= b < arr.shape[1]:
                    d2 += 1
                    sum2 += arr[a, b]
            if d2 >= 2:
                temp2.append(sum2)
        # print(temp1)
        # print(temp2)
        i, j = (i, j+1) if len(temp1) and len(temp2) and min(temp1) <= min(temp2) else (i+1, j)
        if i > arr.shape[0] - 1 or j > arr.shape[1] - 1:
            break
        risk.append(arr[i, j])
        # print((i, j))
    print(risk)
    print(sum(risk))


if __name__ == '__main__':
    get_total_risk('test')  # 40
    # get_total_risk('data_day15')  # 422
