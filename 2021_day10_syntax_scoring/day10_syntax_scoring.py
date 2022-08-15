"""
Day 10: Syntax Scoring
https://adventofcode.com/2021/day/10
"""


def total_scores(data_path):
    ch_list = ['{}', '[]', '<>', '()']
    i_c_l = ['}', ']', '>', ')']
    i_c_t = []
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
        for ss in line:
            if ss in i_c_l:
                i_c_t.append(ss)
                break
    # print(i_c_t)
    print(i_c_t.count(')') * 3 + i_c_t.count(']') * 57 + i_c_t.count('}') * 1197 + i_c_t.count('>') * 25137)


if __name__ == '__main__':
    # total_scores('test')  # 26397
    total_scores('data_day10')  # 166191
