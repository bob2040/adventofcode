"""
Day 12: Passage Pathing
https://adventofcode.com/2021/day/12
"""


def paths(data_path):
    paths = []
    pd = {}
    for line in open(data_path):
        paths.append(line.strip().split('-'))
    # print(paths)
    m = list(set([e for p in paths for e in p if e != 'end']))
    # print(m)
    for key in m:
        temp = []
        for ls in paths:
            if key in ls:
                v = [s for s in ls if s != key][0]
                if v != 'start':
                    temp.append(v)
        pd[key] = temp
    # print(pd)
    # {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'c': ['A'], 'd': ['b'], 'b': ['A', 'd', 'end']}

    start = ('start', set(['start']), None)
    temp = [start]
    n = 0
    while temp:
        cp, sc, t2 = temp.pop(0)
        if cp == 'end':
            n += 1
            continue
        for cave in pd[cp]:
            if cave not in sc:
                nsc = set(sc)
                if cave.lower() == cave:
                    nsc.add(cave)
                temp.append((cave, nsc, t2))
    print(n)


if __name__ == '__main__':
    # paths('test10')
    # paths('test19')
    # paths('test226')
    paths('data_day12')  # 4885
