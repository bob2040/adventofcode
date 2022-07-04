"""
Day 6: Lanternfish
https://adventofcode.com/2021/day/6
"""
import time


def get_data(data_path):
    with open(data_path, 'r') as f:
        con = f.readlines()
    # print(con)
    data_list = [int(i) for i in con[0].split(',')]
    return data_list


def cal_lanternfish(d_l, days):
    for i in range(days):
        for n in d_l[:]:
            if n != 0:
                d_l[d_l.index(n)] = n - 1
            else:
                d_l[d_l.index(n)] = 6
                d_l.append(8)
    return len(d_l)
            

if __name__ == '__main__':
    # d_l = get_data('test')
    start = time.time()
    d_l = get_data('data_day6')
    # print(d_l)
    # print(cal_lanternfish(d_l, 18))
    print(cal_lanternfish(d_l, 80))  # 391888
    # print(cal_lanternfish(d_l, 256))  #
    end = time.time()
    print(end - start)
