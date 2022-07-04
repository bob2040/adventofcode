"""
Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7
"""


def get_data(data_path):
    with open(data_path, 'r') as f:
        return [int(i) for i in f.readline().strip().split(',')]


def fuel_spent(d_l):
    suma = {}
    for i in range(len(d_l)):
        a = []
        for k in d_l:
            a.append(abs(k - d_l[i]))
            if k == d_l[len(d_l) - 1]:
                suma[d_l[i]] = sum(a)
    # print(a)
    # print(suma)
    # print(min(suma.values()))
    return min(suma.values())


if __name__ == '__main__':
    # d_l = get_data('test')
    # print(d_l)  # [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    # fuel_spent(d_l)
    d_l = get_data('data_day7')
    print(fuel_spent(d_l))  # 328187
