"""
Day2 Dive!
https://adventofcode.com/2021/day/2
"""


def final_position(data_day2_dive):
    forward_l = []
    down_l = []
    up_l = []
    with open(data_day2_dive, 'r') as f:
        while True:
            con = f.readline()
            if con == '':
                break
            con = con.strip()
            if con.startswith('forward'):
                forward_l.append(int(con[8:]))
            elif con.startswith('down'):
                down_l.append(int(con[5:]))
            else:
                up_l.append(int(con[3:]))
    return [sum(forward_l), sum(down_l)-sum(up_l)]


def horizontal_multiply_depth(fp_list):
    return fp_list[0] * fp_list[1]


if __name__ == '__main__':
    fp_list = final_position('data_day2_dive')
    print(horizontal_multiply_depth(fp_list))  # 2073315
