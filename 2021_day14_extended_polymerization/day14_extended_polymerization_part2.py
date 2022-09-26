"""
Day 14: Extended Polymerization,Part Two
https://adventofcode.com/2021/day/14#part2
"""
import time
from collections import Counter

def get_diff(data_path):
    with open(data_path, 'r') as f:
        con = [s.strip() for s in f.readlines() if s != '\n']
    # print(con)
    temp = con[0]
    # print(temp)
    rule = dict([s.split(' -> ') for s in con if '->' in s])
    # print(rule)

    q = Counter()
    for i in range(len(temp)-1):
        q[temp[i]+temp[i+1]] += 1

    diff = 0
    for j in range(41):
        q0 = Counter()
        q1 = Counter()
        for k, v in q.items():
            q0[k[0]] += v
            q1[k[0] + rule[k]] += v
            q1[rule[k] + k[1]] += v
        q = q1
        q0[temp[-1]] += 1
        # print(q0)
        d = dict(q0).values()
        diff = max(d) - min(d)
    print(diff)


if __name__ == '__main__':
    start = time.time()
    # get_diff('test')  #
    get_diff('data_day14')  # 2875665202438
    print(time.time()-start)  # 0.0050008296966552734

