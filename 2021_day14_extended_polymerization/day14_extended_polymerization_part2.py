"""
Day 14: Extended Polymerization,Part Two
https://adventofcode.com/2021/day/14#part2
"""
import numpy as np
import time


def get_diff(data_path):
    with open(data_path, 'r') as f:
        con = [s.strip() for s in f.readlines() if s != '\n']
    # print(con)
    temp = np.array(list(con[0]))
    # print(temp)
    rule = dict([s.split(' -> ') for s in con if '->' in s])
    # print(rule)
    n = 0
    while n < 40:
        print(n)
        for i in range(temp.size - 1):
            temp = np.insert(temp, i*2+1, rule[temp[i*2]+temp[i*2+1]])
        n += 1
    # print(temp)
    e = np.unique(temp)
    t = []
    for v in e:
        t.append(np.sum(temp == v))
    # print(quantity)
    print(max(t) - min(t))


if __name__ == '__main__':
    start = time.time()
    # get_diff('test')  #
    get_diff('data_day14')
    print(time.time() - start)

