"""
Day 3: Binary Diagnostic,Part Two
https://adventofcode.com/2021/day/3#part2
"""
import day3_binary_diagnostic as d3bd


def oxygen_rate(bin_l):
    ind = 12
    for i in range(ind):
        ret = [b[i] for b in bin_l for i in range(len(b))]
        if ret[i::ind].count('1') >= ret[i::ind].count('0'):
            bin_l = [s for s in bin_l if s[i] == '1']
            # print(f'{i}过滤：', bin_l)
            if len(bin_l) == 1:
                break
        else:
            bin_l = [s for s in bin_l if s[i] == '0']
            # print(f'{i}过滤：', bin_l)
            if len(bin_l) == 1:
                break
    return bin_l[0]


def co2_rate(bin_l):
    ind = 12
    for i in range(ind):
        ret = [b[i] for b in bin_l for i in range(len(b))]
        if ret[i::ind].count('1') >= ret[i::ind].count('0'):
            bin_l = [s for s in bin_l if s[i] == '0']
            # print(f'{i}co2过滤：', bin_l)
            if len(bin_l) == 1:
                break
        else:
            bin_l = [s for s in bin_l if s[i] == '1']
            # print(f'{i}co2过滤：', bin_l)
            if len(bin_l) == 1:
                break
    return bin_l[0]


def life_support_rate(bin_o_r, bin_c_r):
    return int(bin_o_r, 2) * int(bin_c_r, 2)


if __name__ == '__main__':
    # bin_l = d3bd.data_list('data_day3_binary_diagnostic')
    bin_l = d3bd.data_list('data_day3_binary_diagnostic')
    # print(bin_l)
    # oc_l = oxygen_co2_rate(bin_l)
    bin_o_r = oxygen_rate(bin_l)
    bin_c_r =co2_rate(bin_l)
    print(life_support_rate(bin_o_r, bin_c_r))

