"""
Day 9: Smoke Basin,Part Two
https://adventofcode.com/2021/day/9#part2
"""
import numpy as np


def get_result(data_path):
    with open(data_path, 'r') as f:
        lines = f.read().splitlines()
    # print(con)
    arr = np.array([list(line) for line in lines], dtype=int)
    # print(arr)
    risk_levels = []
    row_n = arr.shape[0]
    col_n = arr.shape[1]
    # top left
    size_list = []
    if arr[0, 0] < arr[0, 1] and arr[0, 0] < arr[1, 0]:
        # risk_levels.append(arr[0, 0] + 1)
        temp = []
        temp.append((0, 0))
        size = 1
        r = 0
        c = 0
        while c < col_n-1:
            if arr[r, c] + 1 == arr[r, c+1] and arr[r, c+1] != 9 and arr[r, c] + 1 == arr[r+1, c] and arr[r+1, c] != 9:
                if (r, c+1) not in temp:
                    temp.append((r, c+1))
                    size += 1
                a = r
                # print('size1:', size)
                while r < row_n-1:
                    if arr[r, c] + 1 == arr[r+1, c] and arr[r+1, c] != 9:
                        if (r+1, c) not in temp:
                            temp.append((r+1, c))
                            size += 1
                        # print('size2:', size)
                        r += 1
                    else:
                        r = a
                        break
                c += 1
            elif arr[r, c] + 1 == arr[r, c+1] and arr[r, c+1] != 9 and arr[r, c] + 1 != arr[r+1, c]:
                if (r, c + 1) not in temp:
                    temp.append((r, c + 1))
                    size += 1
                a = r
                c += 1
                # print('size1:', size)
                while r < row_n - 1:
                    if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                        if (r + 1, c) not in temp:
                            temp.append((r + 1, c))
                            size += 1
                        # print('size2:', size)
                        r += 1
                    else:
                        r = a
                        break
                # c += 1
            else:
                break
        size_list.append(size)
    # print('size_list:', size_list)

    # top right
    if arr[0, col_n-1] < arr[0, col_n-2] and arr[0, col_n-1] < arr[1, col_n-1]:
        # risk_levels.append(arr[0, col_n - 1] + 1)
        temp = []
        temp.append((0, col_n-1))
        size = 1
        r = 0
        c = col_n - 1
        while c > 0:
            if arr[r, c] + 1 == arr[r, c-1] and arr[r, c-1] != 9 and arr[r, c] + 1 == arr[r+1, c] and arr[r+1, c] != 9:
                if (r, c-1) not in temp:
                    temp.append((r, c-1))
                    size += 1
                a = r
                # print('size1:', size)
                while r < row_n - 1:
                    if arr[r, c] + 1 == arr[r+1, c] and arr[r+1, c] != 9:
                        if (r+1, c) not in temp:
                            temp.append((r+1, c))
                            size += 1
                        # print('size2:', size)
                        r += 1
                    else:
                        r = a
                        break
                c -= 1
            elif arr[r, c] + 1 == arr[r, c-1] and arr[r, c-1] != 9 and arr[r, c] + 1 != arr[r+1, c]:
                if (r, c-1) not in temp:
                    temp.append((r, c-1))
                    size += 1
                a = r
                c -= 1
                # print('size1:', size)
                while r < row_n - 1:
                    if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                        if (r+1, c) not in temp:
                            temp.append((r+1, c))
                            size += 1
                        # print('size2:', size)
                        r += 1
                    else:
                        r = a
                        break
                # c -= 1
            else:
                break
        size_list.append(size)
    # print('size_list:', size_list)

    # bottom right
    if arr[row_n - 1, col_n - 1] < arr[row_n - 2, col_n - 1] and arr[row_n - 1, col_n - 1] < arr[row_n - 1, col_n - 2]:
        # risk_levels.append(arr[row_n - 1, col_n - 1] + 1)
        temp = []
        temp.append((row_n - 1, col_n - 1))
        size = 1
        r = row_n - 1
        c = col_n - 1
        while c > 0:
            if arr[r, c] + 1 == arr[r, c-1] and arr[r, c-1] != 9 and arr[r, c] + 1 == arr[r-1, c] and arr[r-1, c] != 9:
                if (r, c - 1) not in temp:
                    temp.append((r, c - 1))
                    size += 1
                a = r
                # print('size1:', size)
                while r > 0:
                    if arr[r, c] + 1 == arr[r-1, c] and arr[r-1, c] != 9:
                        if (r-1, c) not in temp:
                            temp.append((r-1, c))
                            size += 1
                        # print('size2:', size)
                        r -= 1
                    else:
                        r = a
                        break
                c -= 1
            elif arr[r, c] + 1 == arr[r, c-1] and arr[r, c-1] != 9 and arr[r, c] + 1 != arr[r-1, c]:
                if (r, c - 1) not in temp:
                    temp.append((r, c - 1))
                    size += 1
                a = r
                c -= 1
                # print('size1:', size)
                while r > 0:
                    if arr[r, c] + 1 == arr[r-1, c] and arr[r-1, c] != 9:
                        if (r-1, c) not in temp:
                            temp.append((r-1, c))
                            size += 1
                        # print('size2:', size)
                        r -= 1
                    else:
                        r = a
                        break
                # c -= 1
            else:
                break
        size_list.append(size)
    # print('size_list:', size_list)

    # bottom left
    if arr[row_n - 1, 0] < arr[row_n - 2, 0] and arr[row_n - 1, 0] < arr[row_n - 1, 1]:
        # risk_levels.append(arr[row_n - 1, 0] + 1)
        temp = []
        temp.append((row_n - 1, 0))
        size = 1
        r = row_n - 1
        c = 0
        while c < col_n-1:
            if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9 and arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                if (r, c+1) not in temp:
                    temp.append((r, c+1))
                    size += 1
                a = r
                # print('size1:', size)
                while r > 0:
                    if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                        if (r - 1, c) not in temp:
                            temp.append((r - 1, c))
                            size += 1
                        # print('size2:', size)
                        r -= 1
                    else:
                        r = a
                        break
                c += 1
            elif arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9 and arr[r, c] + 1 != arr[r - 1, c]:
                if (r, c+1) not in temp:
                    temp.append((r, c+1))
                    size += 1
                a = r
                c += 1
                # print('size1:', size)
                while r > 0:
                    if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                        if (r - 1, c) not in temp:
                            temp.append((r - 1, c))
                            size += 1
                        # print('size2:', size)
                        r -= 1
                    else:
                        r = a
                        break
                # c += 1
            else:
                break
        size_list.append(size)
    # print('size_list:', size_list)

    for i in range(row_n):
        for j in range(col_n):
            # top row
            if (j > 0 and j < col_n-1) and (i == 0):
                if arr[0, j] < arr[0, j-1] and arr[0, j] < arr[0, j+1] and arr[0, j] < arr[1, j]:
                    # risk_levels.append(arr[0, j] + 1)
                    temp = []
                    temp.append((0, j))
                    size = 1
                    r = 0
                    c = j
                    while c > 0 and c < col_n - 1:
                        if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c] + 1 == arr[r + 1, c] and arr[r, c + 1] != 9 and arr[r + 1, c] != 9:
                            if (r, c + 1) not in temp:
                                temp.append((r, c + 1))
                                size += 1
                            a = r
                            # c += 1
                            # print('size11:', size)
                            while r < row_n - 1:
                                if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                                    if (r+1, c) not in temp:
                                        temp.append((r+1, c))
                                        size += 1
                                    # print('size21:', size)
                                    r += 1
                                else:
                                    r = a
                                    break
                            c += 1
                        elif arr[r, c] + 1 == arr[r, c + 1] and arr[r, c] + 1 != arr[r + 1, c] and arr[r, c + 1] != 9:
                            if (r, c + 1) not in temp:
                                temp.append((r, c + 1))
                                size += 1
                            a = r
                            c += 1
                            # print('size11:', size)
                            while r < row_n - 1:
                                if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                                    if (r+1, c) not in temp:
                                        temp.append((r+1, c))
                                        size += 1
                                    # print('size21:', size)
                                    r += 1
                                else:
                                    r = a
                                    break
                            # c += 1
                        else:
                            break

                    r = 0
                    c = j
                    while c >= 0 and c < col_n - 1:
                        if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c] + 1 == arr[r + 1, c] and arr[r, c - 1] != 9 and arr[r + 1, c] != 9:
                            if (r, c-1) not in temp:
                                temp.append((r, c-1))
                                size += 1
                            a = r
                            # c -= 1
                            # print('size12:', size)
                            # print('r,c', r, c)
                            while r < row_n - 1:
                                if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                                    if (r+1, c) not in temp:
                                        temp.append((r+1, c))
                                        size += 1
                                    # print('size22:', size)
                                    r += 1
                                else:
                                    r = a
                                    break
                            c -= 1
                        elif arr[r, c] + 1 == arr[r, c - 1] and arr[r, c] + 1 != arr[r + 1, c] and arr[r, c - 1] != 9:
                            if (r, c - 1) not in temp:
                                temp.append((r, c - 1))
                                size += 1
                            a = r
                            c -= 1
                            # print('size12:', size)
                            # print('r,c', r, c)
                            while r < row_n - 1:
                                if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                                    if (r + 1, c) not in temp:
                                        temp.append((r + 1, c))
                                        size += 1
                                    # print('size22:', size)
                                    r += 1
                                else:
                                    r = a
                                    break
                            # c -= 1
                        else:
                            break

                    size_list.append(size)
                print('size_list:', size_list)

            # bottom row
            if (j > 0 and j < col_n - 1) and (i == row_n - 1):
                if arr[row_n-1, j] < arr[row_n-1, j-1] and arr[row_n-1, j] < arr[row_n-2, j] and arr[row_n-1, j] < arr[row_n-1, j+1]:
                    # risk_levels.append(arr[row_n-1, j] + 1)
                    temp = []
                    temp.append((row_n-1, j))
                    size = 1
                    r = row_n-1
                    c = j
                    while c > 0 and c < col_n - 1:
                        if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9 and arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                            if (r, c+1) not in temp:
                                temp.append((r, c+1))
                                size += 1
                            a = r
                            # print('size1:', size)
                            while r > 0:
                                if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                                    if (r - 1, c) not in temp:
                                        temp.append((r - 1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r -= 1
                                else:
                                    r = a
                                    break
                            c += 1
                        elif arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9 and arr[r, c] + 1 != arr[r - 1, c]:
                            if (r, c+1) not in temp:
                                temp.append((r, c+1))
                                size += 1
                            a = r
                            c += 1
                            # print('size1:', size)
                            while r > 0:
                                if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                                    if (r - 1, c) not in temp:
                                        temp.append((r - 1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r -= 1
                                else:
                                    r = a
                                    break
                            # c += 1
                        else:
                            break

                    r = row_n - 1
                    c = j
                    while c > 0 and c < col_n - 1:
                        if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9 and arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                            if (r, c - 1) not in temp:
                                temp.append((r, c - 1))
                                size += 1
                            a = r
                            # print('size1:', size)
                            while r > 0:
                                if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                                    if (r-1, c) not in temp:
                                        temp.append((r-1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r -= 1
                                else:
                                    r = a
                                    break
                            c -= 1
                        elif arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9 and arr[r, c] + 1 != arr[r - 1, c]:
                            if (r, c - 1) not in temp:
                                temp.append((r, c - 1))
                                size += 1
                            a = r
                            c -= 1
                            # print('size1:', size)
                            while r > 0:
                                if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                                    if (r-1, c) not in temp:
                                        temp.append((r-1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r -= 1
                                else:
                                    r = a
                                    break
                            # c -= 1
                        else:
                            break
                    size_list.append(size)
                print('size_list:', size_list)

            # left column
            if (i > 0 and i < row_n - 1) and (j == 0):
                if arr[i, 0] < arr[i-1, 0] and arr[i, 0] < arr[i, 1] and arr[i, 0] < arr[i+1, 0]:
                    # risk_levels.append(arr[i, 0] + 1)
                    temp = []
                    temp.append((i, 0))
                    size = 1
                    r = i
                    c = 0
                    while r > 0 and r < row_n - 1:
                        if arr[r, c] + 1 == arr[r+1, c] and arr[r+1, c] != 9 and arr[r, c] + 1 == arr[r, c+1] and arr[r, c+1] != 9:
                            if (r+1, c) not in temp:
                                temp.append((r+1, c))
                                size += 1
                            a = c
                            while c < col_n-1:
                                if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                                    if (r, c + 1) not in temp:
                                        temp.append((r, c + 1))
                                        size += 1
                                    c += 1
                                else:
                                    c = a
                                    break
                            r += 1
                        elif arr[r, c] +1 == arr[r+1, c] and arr[r+1, c] != 9 and arr[r, c] + 1 != arr[r, c+1]:
                            if (r+1, c) not in temp:
                                temp.append((r+1, c))
                                size += 1
                            a = c
                            r += 1
                            while c < col_n-1:
                                if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                                    if (r, c + 1) not in temp:
                                        temp.append((r, c + 1))
                                        size += 1
                                    c += 1
                                else:
                                    c = a
                                    break
                            # r += 1
                        else:
                            break

                    r = i
                    c = 0
                    while r > 0 and r < row_n - 1:
                        if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9 and arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                            if (r - 1, c) not in temp:
                                temp.append((r - 1, c))
                                size += 1
                            a = c
                            while c < col_n - 1:
                                if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                                    if (r, c + 1) not in temp:
                                        temp.append((r, c + 1))
                                        size += 1
                                    c += 1
                                else:
                                    c = a
                                    break
                            r -= 1
                        elif arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9 and arr[r, c] + 1 != arr[r, c + 1]:
                            if (r - 1, c) not in temp:
                                temp.append((r - 1, c))
                                size += 1
                            a = c
                            r -= 1
                            while c < col_n - 1:
                                if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                                    if (r, c + 1) not in temp:
                                        temp.append((r, c + 1))
                                        size += 1
                                    c += 1
                                else:
                                    c = a
                                    break
                            # r += 1
                        else:
                            break
                    size_list.append(size)
                print('size_list:', size_list)

            # right column
            if (i > 0 and i < row_n - 1) and (j == col_n - 1):
                if arr[i, col_n-1] < arr[i-1, col_n-1] and arr[i, col_n-1] < arr[i, col_n-2] and arr[i, col_n-1] < arr[i+1, col_n-1]:
                    # risk_levels.append(arr[i, col_n-1]+1)
                    temp = []
                    temp.append((i, col_n-1))
                    size = 1
                    r = i
                    c = col_n-1
                    while r > 0 and r < row_n - 1:
                        if arr[r, c] + 1 == arr[r+1, c] and arr[r+1, c] != 9 and arr[r, c] + 1 == arr[r, c-1] and arr[r, c-1] != 9:
                            if (r+1, c) not in temp:
                                temp.append((r+1, c))
                                size += 1
                            a = c
                            while c > 0:
                                if arr[r, c] + 1 == arr[r, c-1] and arr[r, c-1] != 9:
                                    if (r, c-1) not in temp:
                                        temp.append((r, c-1))
                                        size += 1
                                    c -= 1
                                else:
                                    c = a
                                    break
                            r += 1
                        elif arr[r, c] + 1 == arr[r+1, c] and arr[r+1, c] != 9 and arr[r, c] + 1 != arr[r, c-1]:
                            if (r+1, c) not in temp:
                                temp.append((r+1, c))
                                size += 1
                            a = c
                            r += 1
                            while c > 0:
                                if arr[r, c] + 1 == arr[r, c-1] and arr[r, c-1] != 9:
                                    if (r, c-1) not in temp:
                                        temp.append((r, c-1))
                                        size += 1
                                    c -= 1
                                else:
                                    c = a
                                    break
                            # r += 1
                        else:
                            break
                    r = i
                    c = col_n - 1
                    while r > 0 and r < row_n - 1:
                        if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9 and arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                            if (r - 1, c) not in temp:
                                temp.append((r - 1, c))
                                size += 1
                            a = c
                            while c > 0:
                                if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                                    if (r, c - 1) not in temp:
                                        temp.append((r, c - 1))
                                        size += 1
                                    c -= 1
                                else:
                                    c = a
                                    break
                            r -= 1
                        elif arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9 and arr[r, c] + 1 != arr[r, c - 1]:
                            if (r - 1, c) not in temp:
                                temp.append((r - 1, c))
                                size += 1
                            a = c
                            r -= 1
                            while c > 0:
                                if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                                    if (r, c - 1) not in temp:
                                        temp.append((r, c - 1))
                                        size += 1
                                    c -= 1
                                else:
                                    c = a
                                    break
                            # r += 1
                        else:
                            break
                    size_list.append(size)
                print(size_list)

            # center
            if (i > 0 and i < row_n - 1) and (j > 0 and j < col_n-1):
                if arr[i, j] < arr[i, j-1] and arr[i, j] < arr[i, j+1] and arr[i, j] < arr[i-1, j] and arr[i, j] < arr[i+1, j]:
                    # risk_levels.append(arr[i, j] + 1)
                    temp = []
                    temp.append((i, j))
                    size = 1
                    r = i
                    c = j
                    while c >= 0 and c <= col_n - 1:
                        if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9 and arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                            if (r, c+1) not in temp:
                                temp.append((r, c+1))
                                size += 1
                            a = r
                            # print('size1:', size)
                            while r >= 0:
                                if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                                    if (r - 1, c) not in temp:
                                        temp.append((r - 1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r -= 1
                                else:
                                    r = a
                                    break
                            c += 1
                        elif arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9 and arr[r, c] + 1 != arr[r - 1, c]:
                            if (r, c+1) not in temp:
                                temp.append((r, c+1))
                                size += 1
                            a = r
                            c += 1
                            # print('size1:', size)
                            while r >= 0:
                                if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                                    if (r - 1, c) not in temp:
                                        temp.append((r - 1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r -= 1
                                else:
                                    r = a
                                    break
                            # c += 1
                        else:
                            break

                    r = i
                    c = j
                    while c >= 0 and c <= col_n - 1:
                        if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9 and arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                            if (r, c - 1) not in temp:
                                temp.append((r, c - 1))
                                size += 1
                            a = r
                            # print('size1:', size)
                            while r >= 0:
                                if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                                    if (r-1, c) not in temp:
                                        temp.append((r-1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r -= 1
                                else:
                                    r = a
                                    break
                            c -= 1
                        elif arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9 and arr[r, c] + 1 != arr[r - 1, c]:
                            if (r, c - 1) not in temp:
                                temp.append((r, c - 1))
                                size += 1
                            a = r
                            c -= 1
                            # print('size1:', size)
                            while r >= 0:
                                if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9:
                                    if (r-1, c) not in temp:
                                        temp.append((r-1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r -= 1
                                else:
                                    r = a
                                    break
                            # c -= 1
                        else:
                            break
                    # *********************************
                    r = i
                    c = j
                    while c >= 0 and c <= col_n - 1:
                        if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9 and arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                            if (r, c + 1) not in temp:
                                temp.append((r, c + 1))
                                size += 1
                            a = r
                            # print('size1:', size)
                            while r <= row_n-1:
                                if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                                    if (r + 1, c) not in temp:
                                        temp.append((r + 1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r += 1
                                else:
                                    r = a
                                    break
                            c += 1
                        elif arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9 and arr[r, c] + 1 != arr[r + 1, c]:
                            if (r, c + 1) not in temp:
                                temp.append((r, c + 1))
                                size += 1
                            a = r
                            c += 1
                            # print('size1:', size)
                            while r <= row_n-1:
                                if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                                    if (r + 1, c) not in temp:
                                        temp.append((r + 1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r += 1
                                else:
                                    r = a
                                    break
                            # c += 1
                        else:
                            break

                    r = i
                    c = j
                    while c >= 0 and c <= col_n - 1:
                        if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9 and arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                            if (r, c - 1) not in temp:
                                temp.append((r, c - 1))
                                size += 1
                            a = r
                            # print('size1:', size)
                            while r <= row_n-1:
                                if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                                    if (r + 1, c) not in temp:
                                        temp.append((r + 1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r += 1
                                else:
                                    r = a
                                    break
                            c -= 1
                        elif arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9 and arr[r, c] + 1 != arr[r + 1, c]:
                            if (r, c - 1) not in temp:
                                temp.append((r, c - 1))
                                size += 1
                            a = r
                            c -= 1
                            # print('size1:', size)
                            while r <= row_n-1:
                                if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9:
                                    if (r + 1, c) not in temp:
                                        temp.append((r + 1, c))
                                        size += 1
                                    # print('size2:', size)
                                    r += 1
                                else:
                                    r = a
                                    break
                            # c -= 1
                        else:
                            break
                    # -----------------------------------------------
                    r = i
                    c = j
                    while r >= 0 and r <= row_n - 1:
                        if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9 and arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                            if (r + 1, c) not in temp:
                                temp.append((r + 1, c))
                                size += 1
                            a = c
                            while c >= 0:
                                if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                                    if (r, c - 1) not in temp:
                                        temp.append((r, c - 1))
                                        size += 1
                                    c -= 1
                                else:
                                    c = a
                                    break
                            r += 1
                        elif arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9 and arr[r, c] + 1 != arr[r, c - 1]:
                            if (r + 1, c) not in temp:
                                temp.append((r + 1, c))
                                size += 1
                            a = c
                            r += 1
                            while c >= 0:
                                if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                                    if (r, c - 1) not in temp:
                                        temp.append((r, c - 1))
                                        size += 1
                                    c -= 1
                                else:
                                    c = a
                                    break
                            # r += 1
                        else:
                            break
                    r = i
                    c = j
                    while r >= 0 and r <= row_n - 1:
                        if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9 and arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                            if (r - 1, c) not in temp:
                                temp.append((r - 1, c))
                                size += 1
                            a = c
                            while c >= 0:
                                if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                                    if (r, c - 1) not in temp:
                                        temp.append((r, c - 1))
                                        size += 1
                                    c -= 1
                                else:
                                    c = a
                                    break
                            r -= 1
                        elif arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9 and arr[r, c] + 1 != arr[r, c - 1]:
                            if (r - 1, c) not in temp:
                                temp.append((r - 1, c))
                                size += 1
                            a = c
                            r -= 1
                            while c >= 0:
                                if arr[r, c] + 1 == arr[r, c - 1] and arr[r, c - 1] != 9:
                                    if (r, c - 1) not in temp:
                                        temp.append((r, c - 1))
                                        size += 1
                                    c -= 1
                                else:
                                    c = a
                                    break
                            # r += 1
                        else:
                            break
                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    r = i
                    c = j
                    while r >= 0 and r <= row_n - 1:
                        if arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9 and arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                            if (r + 1, c) not in temp:
                                temp.append((r + 1, c))
                                size += 1
                            a = c
                            while c <= col_n-1:
                                if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                                    if (r, c + 1) not in temp:
                                        temp.append((r, c + 1))
                                        size += 1
                                    c += 1
                                else:
                                    c = a
                                    break
                            r += 1
                        elif arr[r, c] + 1 == arr[r + 1, c] and arr[r + 1, c] != 9 and arr[r, c] + 1 != arr[r, c + 1]:
                            if (r + 1, c) not in temp:
                                temp.append((r + 1, c))
                                size += 1
                            a = c
                            r += 1
                            while c <= col_n-1:
                                if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                                    if (r, c + 1) not in temp:
                                        temp.append((r, c + 1))
                                        size += 1
                                    c += 1
                                else:
                                    c = a
                                    break
                            # r += 1
                        else:
                            break
                    r = i
                    c = j
                    while r >= 0 and r <= row_n - 1:
                        if arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9 and arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                            if (r - 1, c) not in temp:
                                temp.append((r - 1, c))
                                size += 1
                            a = c
                            while c <= col_n-1:
                                if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                                    if (r, c + 1) not in temp:
                                        temp.append((r, c + 1))
                                        size += 1
                                    c += 1
                                else:
                                    c = a
                                    break
                            r -= 1
                        elif arr[r, c] + 1 == arr[r - 1, c] and arr[r - 1, c] != 9 and arr[r, c] + 1 != arr[r, c + 1]:
                            if (r - 1, c) not in temp:
                                temp.append((r - 1, c))
                                size += 1
                            a = c
                            r -= 1
                            while c <= col_n-1:
                                if arr[r, c] + 1 == arr[r, c + 1] and arr[r, c + 1] != 9:
                                    if (r, c + 1) not in temp:
                                        temp.append((r, c + 1))
                                        size += 1
                                    c += 1
                                else:
                                    c = a
                                    break
                            # r += 1
                        else:
                            break
                    size_list.append(size)
                print(size_list)

    # print(risk_levels)
    # print(np.array([risk_levels]).sum())


if __name__ == '__main__':
    get_result('test')  #
    # get_result('data_day9')  #
