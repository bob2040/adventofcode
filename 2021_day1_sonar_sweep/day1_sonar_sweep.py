"""
Day 1: Sonar Sweep
https://adventofcode.com/2021/day/1
"""


# put data into a data list and return the list
def list_data(data_file_path):
    data_list = []
    with open(data_file_path, 'r') as f:
        while True:
            num = f.readline()
            data_list.append(num)
            if num == '':
                break
    return [int(i.strip()) for i in data_list if i]


# to calculate how many measurements are larger than the previous measurement
def larger_than_previous(d_l):
    a = d_l[:len(d_l)-1]
    b = d_l[1:]
    return sum([1 for m, n in zip(a, b) if m - n < 0])


if __name__ == '__main__':
    d_l = list_data('data')
    print(larger_than_previous(d_l))  # 1832
