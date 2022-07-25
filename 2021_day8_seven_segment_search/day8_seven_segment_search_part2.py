"""
Day 8: Seven Segment Search,Part Two
https://adventofcode.com/2021/day/8#part2
"""
import numpy as np


def get_sum(data_path):
    with open(data_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    ret0 = [s.split('|')[0].strip() for s in lines]
    ret1 = [s.split('|')[1].strip() for s in lines]
    ten_arra = np.array([e0.split() for e0 in ret0])
    
    four_arra = np.array([e1.split() for e1 in ret1])
   
    ten_ordered = []
    for i in range(ten_arra.shape[0]):
        
        zero, one, two, three, four, five, six, seven, eight, nine = [], [], [], [], [], [], [], [], [], []
        for j in range(ten_arra.shape[1]):
            el = list(ten_arra[i, j])
            if len(el) == 2:
                one = el
            if len(el) == 3:
                seven = el
            if len(el) == 4:
                four = el
            if len(el) == 7:
                eight = el

        zero_six_nine = np.array([list(s6) for s6 in ten_arra[i] if len(s6) == 6])
        
        for k in range(zero_six_nine.shape[0]):
            if set(four).issubset(set(zero_six_nine[k])):
                nine = zero_six_nine[k].tolist()      
            elif set(seven).issubset(set(zero_six_nine[k])) and (not set(four).issubset(set(zero_six_nine[k]))):
                zero = zero_six_nine[k].tolist()
            else:
                six = zero_six_nine[k].tolist()

        two_three_five = np.array([list(s5) for s5 in ten_arra[i] if len(s5) == 5])
        for g in range(two_three_five.shape[0]):
            if set(seven).issubset(set(two_three_five[g])):
                three = two_three_five[g].tolist()
            elif set(two_three_five[g]).issubset(set(six)):
                five = two_three_five[g].tolist()
            else:
                two = two_three_five[g].tolist()

        # print('zero:', zero)
        # print('one:', one)
        # print('two:', two)
        # print('three:', three)
        # print('four:', four)
        # print('five:', five)
        # print('six:', six)
        # print('seven:', seven)
        # print('eight:', eight)
        # print('nine:', nine)

        ten_ordered.append([''.join(zero), ''.join(one), ''.join(two), ''.join(three), ''.join(four),
                            ''.join(five), ''.join(six), ''.join(seven), ''.join(eight), ''.join(nine)])
        
    ten_ordered_arra = np.array(ten_ordered)

    for i in range(four_arra.shape[0]):
        for j in range(four_arra.shape[1]):
            for k in range(ten_ordered_arra.shape[1]):
                if set(four_arra[i, j]) == set(ten_ordered_arra[i, k]):
                    four_arra[i, j] = str(k)

    nums = []
    for o in range(four_arra.shape[0]):
        nums.append(int(''.join(four_arra[o].tolist())))

    print(sum(nums))


if __name__ == '__main__':
    # get_sum('test')  # 61229
    get_sum('data_day8')  # 1027483
