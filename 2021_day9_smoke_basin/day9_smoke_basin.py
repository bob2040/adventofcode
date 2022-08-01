"""
Day 9: Smoke Basin
https://adventofcode.com/2021/day/9
"""
import numpy as np


def sum_of_risk_levels(data_path):
    with open(data_path, 'r') as f:
        lines = f.read().splitlines()
    # print(con)
    arr = np.array([list(line) for line in lines], dtype=int)
    # print(arr)
    risk_levels = []
    row_n = arr.shape[0]
    col_n = arr.shape[1]
    # top left
    if arr[0, 0] < arr[0, 1] and arr[0, 0] < arr[1, 0]:
        risk_levels.append(arr[0, 0] + 1)
    # top right
    if arr[0, col_n - 1] < arr[0, col_n - 2] and arr[0, col_n - 1] < arr[1, col_n - 1]:
        risk_levels.append(arr[0, col_n - 1] + 1)
    # bottom right
    if arr[row_n - 1, col_n - 1] < arr[row_n - 2, col_n - 1] and arr[row_n - 1, col_n - 1] < arr[row_n - 1, col_n - 2]:
        risk_levels.append(arr[row_n - 1, col_n - 1] + 1)
    # bottom left
    if arr[row_n - 1, 0] < arr[row_n - 2, 0] and arr[row_n - 1, 0] < arr[row_n - 1, 1]:
        risk_levels.append(arr[row_n - 1, 0] + 1)

    for i in range(row_n):
        for j in range(col_n):
            # top row
            if (j > 0 and j < col_n-1) and (i == 0):
                if arr[0, j] < arr[0, j-1] and arr[0, j] < arr[0, j+1] and arr[0, j] < arr[1, j]:
                    risk_levels.append(arr[0, j] + 1)
            # bottom row
            if (j > 0 and j < col_n - 1) and (i == row_n - 1):
                if arr[row_n-1, j] < arr[row_n-1, j-1] and arr[row_n-1, j] < arr[row_n-2, j] and arr[row_n-1, j] < arr[row_n-1, j+1]:
                    risk_levels.append(arr[row_n-1, j] + 1)
            # left column
            if (i > 0 and i < row_n - 1) and (j == 0):
                if arr[i, 0] < arr[i-1, 0] and arr[i, 0] < arr[i, 1] and arr[i, 0] < arr[i+1, 0]:
                    risk_levels.append(arr[i, 0] + 1)
            # right column
            if (i > 0 and i < row_n - 1) and (j == col_n - 1):
                if arr[i, col_n-1] < arr[i-1, col_n-1] and arr[i, col_n-1] < arr[i, col_n-2] and arr[i, col_n-1] < arr[i+1, col_n-1]:
                    risk_levels.append(arr[i, col_n-1]+1)
            # center
            if (i > 0 and i < row_n - 1) and (j > 0 and j < col_n-1):
                if arr[i, j] < arr[i, j-1] and arr[i, j] < arr[i, j+1] and arr[i, j] < arr[i-1, j] and arr[i, j] < arr[i+1, j]:
                    risk_levels.append(arr[i, j] + 1)
    # print(risk_levels)
    print(np.array([risk_levels]).sum())


if __name__ == '__main__':
    # sum_of_risk_levels('test')  # 15
    sum_of_risk_levels('data_day9')  # 566
