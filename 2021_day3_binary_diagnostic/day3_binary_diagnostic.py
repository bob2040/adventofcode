"""
Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3
"""


def data_list(d_l):
    bin_l = []
    with open(d_l, 'r') as f:
        while True:
            con = f.readline()
            con = con.strip()
            if con == '':
                break
            bin_l.append(con)
    return bin_l


def gamma_epsilon_rate(bin_l):
    bin_g_r = ''
    ret = [b[i] for b in bin_l for i in range(len(b))]
    for i in range(12):
        if ret[i::12].count('1') > ret[i::12].count('0'):
            bin_g_r += '1'
        else:
            bin_g_r += '0'
    g_r = int(bin_g_r, 2)
    e_r = int(''.join(['0' if s == '1' else '1' for s in bin_g_r]), 2)
    return [g_r, e_r]


def power_consumption(ge_l):
    return ge_l[0] * ge_l[1]


if __name__ == '__main__':
    bin_l = data_list('data_day3_binary_diagnostic')
    # print(bin_l)
    ge_l = gamma_epsilon_rate(bin_l)
    print(power_consumption(ge_l))

