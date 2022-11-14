"""
Day 17: Trick Shot
https://adventofcode.com/2021/day/17
"""


def highest_y():
    x = 0
    i = 0
    while True:
        i += 1
        x += i
        if x >= 207:  # 20 207
            print('vx', i)  # 20
            break
    print('x', x)  # 210
    y = 0
    j = 0
    while True:
        j += 1
        y += j
        if j == 114:  # 9 114
            print('highest_y', y)  # 6555
            break
    k = 0
    while True:
        k += 1
        y -= k
        if y == 0:
            print('vy', k)
            break


if __name__ == '__main__':
    highest_y()
