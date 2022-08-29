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
    print(pd)
    # {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'c': ['A'], 'd': ['b'], 'b': ['A', 'd', 'end']}

    total = []
    en = 'start'
    pl = [en]
    # while True:
    while True:
        en = pl[len(pl) - 1]
        for val_l in pd[en]:
            for val in val_l:
                pl.append(val)
                # if val == 'end':
                #     # pl.append(val)
                #     total.append(pl)
                #     continue
                # if val.islower() and pl.count(val) < 1:
                #     pl.append(val)
                #     # end = pl[len(pl) - 1]
        if en == 'end':
            break

        print(pl)

    # P = []
    # j = 0
    # k = 'start'
    # mypath = [k]
    # while True:
    #     for i in range(j, len(md[k])):
    #         print(i, j, len(md[k]))
    #         k = mypath[len(mypath) - 1]
    #         a = md[k][i]
    #
    #         if a.islower() and mypath.count(a) >= 1:
    #             if j < len(md[k]):
    #                 j += 1
    #                 break
    #         mypath.append(a)
    #         print(mypath)
    #         # print(i, j)
    #         break

    # if key == 'start':
    #     mypath.append(key)
    #     for i in range(len(value)):
    #         mypath.append(value[i])
    #         mypath.append(md[value[i]])

    # starts = [p for p in paths if 'start' in p]
    # others = [p for p in paths if 'start' not in p]
    # print(starts)
    # print(others)
    # v_p = []
    # for start in starts:
    #     temp = ['start']
    #     a = [s for s in start if s != 'start'][0]
    #     temp.append(a)
    #     # col_temp = []
    #     # row_temp = []
    #     # for other in others:
    #     i = 0
    #     while i < len(others):
    #         te = temp[len(temp)-1]
    #         if te in others[i]:
    #             b = [s for s in others[i] if s != te][0]
    #             if b == 'end':
    #                 temp.append(b)
    #         i += 1
    #
    #     # print(col_temp)
    #     # print(row_temp)
    #         #     for other1 in others:
    #         #         te1 = [b]
    #         #         if te1 in other1:
    #         #             b1 = [s1 for s1 in other1 if s1 != te1][0]
    #         #             if b1 == 'end':
    #         #                 temp.append(b1)
    #         #                 v_p.append(temp)
    #         #             elif b1.islower() and b1 != temp[len(temp)-2] and b1 != 'end' and temp.count(b1) < 1:
    #         #                 temp.append(b1)
    #         #             elif b1.isupper():
    #         #                 temp.append(b1)
    #
    #         # print(temp)
    # print(starts)
    # print(v_p)


if __name__ == '__main__':
    paths('test10')
    # paths('test19')
    # paths('test226')
    # paths('data_day12')
