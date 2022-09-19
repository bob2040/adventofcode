"""
Day 14: Extended Polymerization
https://adventofcode.com/2021/day/14
"""
import time
from itertools import chain
from collections import Counter

def get_diff(data_path):
    with open(data_path, 'r') as f:
        con = [s.strip() for s in f.readlines() if s != '\n']
    # print(con)
    temp = con[0]
    # print(temp)
    rule = dict([s.split(' -> ') for s in con if '->' in s])
    # print(rule)
    n = 0
    while n < 40:
        new_t = []
        for i in range(len(temp)-1):
            te = tuple(temp[i:i + 2])
            r = rule[te[0]+te[1]]
            new_t.append(r)
        # print(new_t)
        last = temp[len(temp)-1]
        temp = list(chain.from_iterable(zip(temp, new_t)))
        temp.append(last)
        print(n)
        n += 1
    # print(temp)
    quantity = [temp.count(s) for s in set(temp)]
    print(max(quantity) - min(quantity))


if __name__ == '__main__':
    start = time.time()
    # get_diff('test')  #
    get_diff('data_day14')  #
    print(time.time()-start)
