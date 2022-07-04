"""
Day 6: Lanternfish,Part Two
https://adventofcode.com/2021/day/6#part2
"""
import time


def get_data(data_path):
    with open(data_path, 'r') as f:
        con = f.readlines()
    # print(con)
    data_list = [int(i) for i in con[0].split(',')]
    return data_list


def cal_lanternfish(d_l, days):
    # for i in range(days):
    #     for n in d_l[:]:
    #         if n != 0:
    #             d_l[d_l.index(n)] = n - 1
    #         else:
    #             d_l[d_l.index(n)] = 6
    #             d_l.append(8)
    # return len(d_l)
    d = {}
    for i in range(9):
        d[i] = d_l.count(i)
    # print(f)  # {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0}
    for i in range(days):
        d[(i+7)%9] += d[i%9]
    return sum(d.values())
            

if __name__ == '__main__':
    # get_data('test')
    # d_l = get_data('test')
    # start = time.time()
    d_l = get_data('data_day6')
    # print(d_l)
    # cal_lanternfish(d_l, 18)
    # print(cal_lanternfish(d_l, 18))
    # print(cal_lanternfish(d_l, 80))  # 391888
    print(cal_lanternfish(d_l, 256))  # 1754597645339
    # end = time.time()
    # print(end - start)
