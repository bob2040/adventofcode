"""
Day 8: Seven Segment Search
https://adventofcode.com/2021/day/8
"""
import numpy as np


def get_times(data_path):
    with open(data_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    ret = [s.split('|')[1].strip() for s in lines]
    digits = np.array([e.split() for e in ret])
    n = 0
    for digit in digits.flat:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            n += 1
    print(n)


if __name__ == '__main__':
    get_times('data_day8')  # 519
