"""
Day 1: Sonar Sweep, part two
https://adventofcode.com/2021/day/1#part2
"""
import day1_sonar_sweep as d1ss


# put data into a data list,generate a new list and return it
def list_data_part2(data_file_path):
    i_d_l = d1ss.list_data(data_file_path)
    a = i_d_l[:len(i_d_l)-2]
    b = i_d_l[1:len(i_d_l)-1]
    c = i_d_l[2:len(i_d_l)]
    return [m + n + o for m, n, o in zip(a, b, c)]


if __name__ == '__main__':
    d_l = list_data_part2('data_for_part2')
    # How many sums are larger than the previous sum?
    print(d1ss.larger_than_previous(d_l))  # 1858
