"""
Day 14: Extended Polymerization
https://adventofcode.com/2021/day/14
"""


def get_diff(data_path):
    with open(data_path, 'r') as f:
        con = [s.strip() for s in f.readlines() if s != '\n']
    # print(con)
    temp = con[0]
    # print(temp)
    rule = dict([s.split(' -> ') for s in con if '->' in s])
    # print(rule)
    n = 0
    while n < 10:
        new_t = ''
        for i in range(len(temp)-1):
            new_t += rule[temp[i:i+2]].join(list(temp[i:i+2]))[0:2]
        new_t += temp[len(temp)-1]
        temp = new_t
        n += 1
    quantity = [temp.count(s) for s in set(temp)]
    # print(quantity)
    print(max(quantity) - min(quantity))


if __name__ == '__main__':
    # get_diff('test')  # 1588
    get_diff('data_day14')  # 2590
