"""
Day 10: Syntax Scoring,Part Two
https://adventofcode.com/2021/day/10#part2
"""
import numpy as np


def middle_score(data_path):
    ch_list = ['{}', '[]', '<>', '()']
    i_c_l = ['}', ']', '>', ')']
    score_list = []
    for li in open(data_path):
        line = li.strip()
        n = 0
        while n < 4:
            for s in ch_list:
                if line.find(s) >= 0:
                    line = line.replace(s, '')
                    n = 0
                else:
                    n += 1
        # print(line)
        is_ok = []
        for ss in line:
            if ss not in i_c_l:
                is_ok.append(True)
            else:
                is_ok.append(False)
        cs_d = {'(': 1, '[': 2, '{': 3, '<': 4}
        if all(is_ok):
            score = 0
            for ch in line[::-1]:
                score = score * 5 + cs_d[ch]
            score_list.append(score)
    # print(score_list)
    print(int(np.median(np.array(score_list))))


if __name__ == '__main__':
    # middle_score('test')  # 288957
    middle_score('data_day10')  # 1152088313
