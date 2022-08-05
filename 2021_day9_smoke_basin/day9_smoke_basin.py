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
    risk_level_coordinates = []
    row_n = arr.shape[0]
    col_n = arr.shape[1]

    # Way 1:
    # # top left
    # if arr[0, 0] < arr[0, 1] and arr[0, 0] < arr[1, 0]:
    #     risk_levels.append(arr[0, 0] + 1)
    # # top right
    # if arr[0, col_n - 1] < arr[0, col_n - 2] and arr[0, col_n - 1] < arr[1, col_n - 1]:
    #     risk_levels.append(arr[0, col_n - 1] + 1)
    # # bottom right
    # if arr[row_n - 1, col_n - 1] < arr[row_n - 2, col_n - 1] and arr[row_n - 1, col_n - 1] < arr[row_n - 1, col_n - 2]:
    #     risk_levels.append(arr[row_n - 1, col_n - 1] + 1)
    # # bottom left
    # if arr[row_n - 1, 0] < arr[row_n - 2, 0] and arr[row_n - 1, 0] < arr[row_n - 1, 1]:
    #     risk_levels.append(arr[row_n - 1, 0] + 1)
    #
    # for i in range(row_n):
    #     for j in range(col_n):
    #         # top row
    #         if (j > 0 and j < col_n-1) and (i == 0):
    #             if arr[0, j] < arr[0, j-1] and arr[0, j] < arr[0, j+1] and arr[0, j] < arr[1, j]:
    #                 risk_levels.append(arr[0, j] + 1)
    #         # bottom row
    #         if (j > 0 and j < col_n - 1) and (i == row_n - 1):
    #             if arr[row_n-1, j] < arr[row_n-1, j-1] and arr[row_n-1, j] < arr[row_n-2, j] and arr[row_n-1, j] < arr[row_n-1, j+1]:
    #                 risk_levels.append(arr[row_n-1, j] + 1)
    #         # left column
    #         if (i > 0 and i < row_n - 1) and (j == 0):
    #             if arr[i, 0] < arr[i-1, 0] and arr[i, 0] < arr[i, 1] and arr[i, 0] < arr[i+1, 0]:
    #                 risk_levels.append(arr[i, 0] + 1)
    #         # right column
    #         if (i > 0 and i < row_n - 1) and (j == col_n - 1):
    #             if arr[i, col_n-1] < arr[i-1, col_n-1] and arr[i, col_n-1] < arr[i, col_n-2] and arr[i, col_n-1] < arr[i+1, col_n-1]:
    #                 risk_levels.append(arr[i, col_n-1]+1)
    #         # center
    #         if (i > 0 and i < row_n - 1) and (j > 0 and j < col_n-1):
    #             if arr[i, j] < arr[i, j-1] and arr[i, j] < arr[i, j+1] and arr[i, j] < arr[i-1, j] and arr[i, j] < arr[i+1, j]:
    #                 risk_levels.append(arr[i, j] + 1)
    # print(np.array(risk_levels)-1)
    # # [1 0 0 4 0 1 0 4 1 0 1 0 2 1 2 0 2 3 4 0 1 1 1 0 3 2 1 3 0 3 0 1 1 1 0 0 2
    # #  5 1 0 0 2 0 0 1 0 2 1 1 4 2 2 0 4 4 3 0 1 6 2 1 2 3 2 0 2 1 0 0 2 0 0 4 3
    # #  1 0 0 1 4 0 0 0 1 1 3 2 1 0 0 0 3 2 0 0 2 2 0 4 0 5 1 3 1 1 1 0 4 4 0 4 0
    # #  0 0 0 0 0 0 1 0 1 0 0 3 0 0 0 0 0 2 0 2 0 3 1 5 2 6 0 0 0 0 2 0 0 0 1 2 2
    # #  3 4 0 0 3 0 0 0 0 0 0 1 1 0 2 0 5 2 0 1 0 1 0 2 2 0 6 0 1 1 2 3 1 1 2 1 0
    # #  2 2 0 0 0 0 1 0 5 0 1 0 2 4 1 0 0 4 1 1 0 0 3 0 0 5 1 5 2 1 0 5 1 1 3 3 1
    # #  0 5 1 0 5 0 0 4 1 0 0 0 0 1 6 4 3 0 3 0]
    # # print(len(risk_levels))  # 242
    # print(np.array(risk_levels).sum())

    # Way 2:
    for i in range(row_n):
        for j in range(col_n):
            mylist = []
            # top left
            if i == 0 and j == 0:
                mylist = [arr[i, j], arr[i+1, j], arr[i, j+1]]
            # top right
            elif i == 0 and j == col_n-1:
                mylist = [arr[i, j], arr[i + 1, j], arr[i, j - 1]]
            # bottom right
            elif i == row_n-1 and j == col_n-1:
                mylist = [arr[i, j], arr[i - 1, j], arr[i, j - 1]]
            # bottom left
            elif i == row_n-1 and j == 0:
                mylist = [arr[i, j], arr[i - 1, j], arr[i, j + 1]]
            # top row
            elif i == 0 and (j > 0 and j < col_n-1):
                mylist = [arr[i, j], arr[i + 1, j], arr[i, j - 1], arr[i, j + 1]]
            # bottom row
            elif i == row_n-1 and (j > 0 and j < col_n-1):
                mylist = [arr[i, j], arr[i - 1, j], arr[i, j - 1], arr[i, j + 1]]
            # left column
            elif (i > 0 and i < row_n-1) and j == 0:
                mylist = [arr[i, j], arr[i - 1, j], arr[i + 1, j], arr[i, j + 1]]
            # right column
            elif (i > 0 and i < row_n - 1) and j == col_n-1:
                mylist = [arr[i, j], arr[i - 1, j], arr[i + 1, j], arr[i, j - 1]]
            # middle
            elif (i > 0 and i < row_n - 1) and (j > 0 and j < col_n-1):
                mylist = [arr[i, j], arr[i - 1, j], arr[i + 1, j], arr[i, j - 1], arr[i, j + 1]]

            if len(mylist) > 0:
                if arr[i, j] == min(mylist) and arr[i, j] != 9 and ((i, j) not in risk_level_coordinates):
                    risk_level_coordinates.append((i, j))
                    risk_levels.append(arr[i, j])
    print((np.array(risk_levels)+1).sum())


if __name__ == '__main__':
    # sum_of_risk_levels('test')  # 15
    sum_of_risk_levels('data_day9')  # 566
