"""
Day2 Dive! Part Two
https://adventofcode.com/2021/day/2#part2
"""


def final_position(data_day2_dive):
    data_list = []
    with open(data_day2_dive, 'r') as f:
        while True:
            con = f.readline()
            if con == '':
                break
            con = con.strip()
            data_list.append(con)
    down_total = 0
    up_total = 0
    forward_total = 0
    depth = 0
    for i in range(len(data_list)):
        if data_list[i].startswith('forward'):
            forward = int(data_list[i][8:])
            forward_total += int(data_list[i][8:])
            aim = down_total - up_total
            depth += aim * forward
        if data_list[i].startswith('down'):
            down_total += int(data_list[i][5:])
        if data_list[i].startswith('up'):
            up_total += int(data_list[i][3:])
    return [forward_total, depth]


def horizontal_multiply_depth(fp_list):
    return fp_list[0] * fp_list[1]


if __name__ == '__main__':
    fp_list = final_position('data_day2_dive')
    print(horizontal_multiply_depth(fp_list))  # 1840311528
