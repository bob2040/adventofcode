"""
Day 16: Packet Decoder,Part Two
https://adventofcode.com/2021/day/16#part2
"""


def get_result(data_path):
    s_data = open(data_path).read()
    # print(s_data)
    hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                  '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                  '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                  'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    bin_to_dec = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
    bin4_to_dec = {'0000': 0, '0001': 1, '0010': 2, '0011': 3,
                   '0100': 4, '0101': 5, '0110': 6, '0111': 7,
                   '1000': 8, '1001': 9, '1010': 10, '1011': 11,
                   '1100': 12, '1101': 13, '1110': 14, '1111': 15}
    s_bin_data = ''
    for s in s_data:
        s_bin_data += hex_to_bin[s]
    # print(s_bin_data)
    i = 0
    # version = 0
    op_list = []
    while True:
        if i > len(s_bin_data) - 1 or i+3 > len(s_bin_data) - 1 \
                or i+6 > len(s_bin_data) - 1 or s_bin_data[i:i+3] not in bin_to_dec.keys():
            break
        # print(s_bin_data[i:i+3])
        # version += bin_to_dec[s_bin_data[i:i+3]]
        # print(version)
        type_id = s_bin_data[i+3:i+6]
        # print(type_id)
        if type_id != '100':
            # +
            if type_id == '000':
                op_list.append('+')
            # *
            if type_id == '001':
                op_list.append('*')
            # min
            if type_id == '010':
                op_list.append('min')
            # max
            if type_id == '011':
                op_list.append('max')
            # >
            if type_id == '101':
                op_list.append('>')
            # <
            if type_id == '110':
                op_list.append('<')
            # ==
            if type_id == '111':
                op_list.append('==')

            if s_bin_data[i+6] == '0':
                i += 3+3+1+15
            elif s_bin_data[i+6] == '1':
                i += 3+3+1+11
        elif type_id == '100':
            if s_bin_data[i + 6] == '0':
                op_list.append(bin4_to_dec[s_bin_data[i+7:i+11]])
                i += 3+3+1+4
            else:
                j = 0
                while s_bin_data[i+6+j] == '1':
                    op_list.append(bin4_to_dec[s_bin_data[i + 7+j:i + 11+j]])
                    j += 5
                op_list.append(bin4_to_dec[s_bin_data[i + 7 + j:i + 11 + j]])
                i += 6+j+5
                # print('i', i)
    # print(op_list)
    while True:
        i = 0
        if len(op_list) == 1:
            break
        while True:
            if i > len(op_list) - 1 or i+1 > len(op_list) - 1:
                break
            if isinstance(op_list[i], str) and isinstance(op_list[i+1], int):
                if op_list[i] == '+':
                    sum = 0
                    while True:
                        if i+1 > len(op_list)-1 or isinstance(op_list[i+1], str):
                            break
                        sum += op_list.pop(i+1)
                    op_list[i] = sum
                    # print(sum)
                    # print(op_list)
                if op_list[i] == '*':
                    mul = 1
                    while True:
                        if i+1 > len(op_list)-1 or isinstance(op_list[i+1], str):
                            break
                        mul *= op_list.pop(i+1)
                    op_list[i] = mul
                if op_list[i] == 'min':
                    temp = []
                    while True:
                        if i+1 > len(op_list)-1 or isinstance(op_list[i+1], str):
                            break
                        temp.append(op_list.pop(i+1))
                    op_list[i] = min(temp)
                if op_list[i] == 'max':
                    temp = []
                    while True:
                        if i+1 > len(op_list)-1 or isinstance(op_list[i+1], str):
                            break
                        temp.append(op_list.pop(i+1))
                    op_list[i] = max(temp)
                if op_list[i] == '<':
                    temp = []
                    k = 0
                    while k < 2:
                        if i+1 > len(op_list)-1 or isinstance(op_list[i+1], str):
                            break
                        temp.append(op_list.pop(i+1))
                        k += 1
                    op_list[i] = 1 if temp[0] < temp[1] else 0
                if op_list[i] == '>':
                    temp = []
                    k = 0
                    while k < 2:
                        if i+1 > len(op_list)-1 or isinstance(op_list[i+1], str):
                            break
                        temp.append(op_list.pop(i+1))
                        k += 1
                    op_list[i] = 1 if temp[0] > temp[1] else 0
                if op_list[i] == '==':
                    temp = []
                    k = 0
                    while k < 2:
                        if i+1 > len(op_list)-1 or isinstance(op_list[i+1], str):
                            break
                        temp.append(op_list.pop(i+1))
                        k += 1
                    op_list[i] = 1 if temp[0] == temp[1] else 0
                print(op_list)
            i += 1


if __name__ == '__main__':
    # get_result('test2_3')  # 110 000 1 00000000010 110 100 00001 010 100 00010 1+2=3
    # get_result('test2_54')  # 000 001 0 000000000010110 101 100 00110 011 100 01001 0000 6*9=54
    # get_result('test2_7')  # 100 010 0 000000000100001 101 100 00111 110 100 01000 000 100 01001 0 7,8,9 min=7
    # get_result('test2_9')  # 110 011 1 00000000011 000 100 00111 101 100 01000 000 100 01001 00000 7,8,9 max=9
    # get_result('test2_1_less_than')  # 110 110 0 000000000010110 101 100 00101 010 100 01111 0000 5,15 5<15,1
    # get_result('test2_0_greater_than')  # 111 101 1 00000000010 111 100 00101 101 100 01111 5,15 5<15,0
    # get_result('test2_0_equal_to')  # 100 111 0 000000000010110 101 100 00101 111 100 01111 0000 5,15 5 != 15,0
    # get_result('test2_1_1+3_2x2')  # 100 111 0 000000001010000 010 000 1 00000000010 010 100 00001 100 100 00011 110 001 1 00000000010 000 100 00010 010 100 00010 00 1,3,2,2 1+3=2+2
    get_result('data_day16')  #
