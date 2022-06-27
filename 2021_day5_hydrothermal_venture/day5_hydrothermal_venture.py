"""
Day 5: Hydrothermal Venture
https://adventofcode.com/2021/day/5
"""
import re
import time


def get_data(data_path):
    with open(data_path, 'r') as f:
        con = f.readlines()
    xy_points = [re.split(',| -> ', i.strip()) for i in con]
    xy_all_int = []
    for i in xy_points:
        xy_all_int.append([int(i[0]), int(i[1]), int(i[2]), int(i[3])])
    return xy_all_int


def points(xy_all_int):
    '''
    horizontal and vertical:
                   .(x,y-1)

        .(x-1,y)   .(x,y)   .(x+1,y)

                   .(x,y+1)

    '''
    a = []
    for i in xy_all_int:
        # vertical
        if i[0] == i[2]:
            for y in range(min([i[1], i[3]]), max([i[1], i[3]])+1):
                a.append(str([i[0], y]))
        # horizontal
        elif i[1] == i[3]:
            for x in range(min([i[0], i[2]]), max([i[0], i[2]])+1):
                a.append(str([x, i[1]]))
    b = set(a)
    count_list = [a.count(i) for i in b]
    # print(count_list)
    return sum([1 for i in count_list if i > 1])


if __name__ == '__main__':
    # xy_all_int = get_data('test')
    start = time.time()
    xy_all_int = get_data('data_day5')
    print(points(xy_all_int))  # 5690
    end = time.time()
    print(end - start)  # 334seconds
