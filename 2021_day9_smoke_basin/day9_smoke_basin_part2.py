"""
Day 9: Smoke Basin
https://adventofcode.com/2021/day/9
"""
import numpy as np


def get_result(data_path):
    with open(data_path, 'r') as f:
        lines = f.read().splitlines()
    # print(con)
    arr = np.array([list(line) for line in lines], dtype=int)
    # print(arr)
    risk_level_coordinates = []
    row_n = arr.shape[0]
    col_n = arr.shape[1]

    for i in range(row_n):
        for j in range(col_n):
            mylist = []
            # top left
            if i == 0 and j == 0:
                mylist = [arr[i, j], arr[i + 1, j], arr[i, j + 1]]
            # top right
            elif i == 0 and j == col_n - 1:
                mylist = [arr[i, j], arr[i + 1, j], arr[i, j - 1]]
            # bottom right
            elif i == row_n - 1 and j == col_n - 1:
                mylist = [arr[i, j], arr[i - 1, j], arr[i, j - 1]]
            # bottom left
            elif i == row_n - 1 and j == 0:
                mylist = [arr[i, j], arr[i - 1, j], arr[i, j + 1]]
            # top row
            elif i == 0 and (j > 0 and j < col_n - 1):
                mylist = [arr[i, j], arr[i + 1, j], arr[i, j - 1], arr[i, j + 1]]
            # bottom row
            elif i == row_n - 1 and (j > 0 and j < col_n - 1):
                mylist = [arr[i, j], arr[i - 1, j], arr[i, j - 1], arr[i, j + 1]]
            # left column
            elif (i > 0 and i < row_n - 1) and j == 0:
                mylist = [arr[i, j], arr[i - 1, j], arr[i + 1, j], arr[i, j + 1]]
            # right column
            elif (i > 0 and i < row_n - 1) and j == col_n - 1:
                mylist = [arr[i, j], arr[i - 1, j], arr[i + 1, j], arr[i, j - 1]]
            # middle
            elif (i > 0 and i < row_n - 1) and (j > 0 and j < col_n - 1):
                mylist = [arr[i, j], arr[i - 1, j], arr[i + 1, j], arr[i, j - 1], arr[i, j + 1]]

            if len(mylist) > 0:
                if arr[i, j] == min(mylist) and arr[i, j] != 9 and ((i, j) not in risk_level_coordinates):
                    risk_level_coordinates.append((i, j))

    # print('coordinates:', risk_level_coordinates)
    # print('len:', len(risk_level_coordinates))
    size_list = []
    for e in risk_level_coordinates:
        temp = []
        temp.append(e)
        size = 1
        # print(temp)
        for ir, jc in temp:
            # print('sss:', ir, jc)
            for c in range(jc, col_n - 1):
                r = ir
                if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                    if (r, c + 1) not in temp:
                        temp.append((r, c + 1))
                        size += 1
                else:
                    break

            for c in range(jc, 0, -1):
                r = ir
                if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                    if (r, c - 1) not in temp:
                        temp.append((r, c - 1))
                        size += 1
                else:
                    break

            for r in range(ir, row_n - 1):
                c = jc
                if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                    if (r + 1, c) not in temp:
                        temp.append((r + 1, c))
                        size += 1
                else:
                    break

            for r in range(ir, 0, -1):
                c = jc
                if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                    if (r - 1, c) not in temp:
                        temp.append((r - 1, c))
                        size += 1
                else:
                    break
            # print('temp:', temp)
            # print('len_temp:', len(temp))
            # if len(temp) == 6:
            #     return
        size_list.append(size)
    # print(size_list)
    basins = np.array(size_list)
    # print(np.sort(basins)[::-1])
    # print(np.sort(basins)[::-1][0:3])
    print(np.sort(basins)[::-1][0:3].prod())


if __name__ == '__main__':
    get_result('test')  # 1134
    # get_result('data_day9')  # 351900, 522750, too low
