"""
Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7
"""


def get_data(data_path):
    with open(data_path, 'r') as f:
        return [int(i) for i in f.readline().strip().split(',')]


def fuel_spent(d_l):
    suma = {}
    m = min(d_l)
    n = max(d_l)
    for k in range(m, n+1):
        a = []
        for g in d_l:
            diff = abs(g - k)
            b = [i for i in range(1, diff+1)]
            a.append(sum(b))
            if g == d_l[len(d_l)-1]:
                suma[k] = sum(a)
    # print(suma)
    # print(min(suma.values()))
    return min(suma.values())


if __name__ == '__main__':
    # d_l = get_data('test')
    # print(d_l)  # [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    # fuel_spent(d_l)
    d_l = get_data('data_day7')
    print(fuel_spent(d_l))  # 91257582
