"""
Day 16: Packet Decoder
https://adventofcode.com/2021/day/16
"""


def version_sum(data_path):
    s_data = open(data_path).read()
    # print(s_data)
    hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                  '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                  '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                  'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    bin_to_dec = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
    s_bin_data = ''
    for s in s_data:
        s_bin_data += hex_to_bin[s]
    # print(s_bin_data)
    i = 0
    version = 0
    while True:
        if i > len(s_bin_data) - 1 or i+3 > len(s_bin_data) - 1 \
                or i+6 > len(s_bin_data) - 1 or s_bin_data[i:i+3] not in bin_to_dec.keys():
            break
        # print(s_bin_data[i:i+3])
        version += bin_to_dec[s_bin_data[i:i+3]]
        # print(version)
        type_id = s_bin_data[i+3:i+6]
        # print(type_id)
        if type_id != '100':
            if s_bin_data[i+6] == '0':
                i += 3+3+1+15
            elif s_bin_data[i+6] == '1':
                i += 3+3+1+11
        elif type_id == '100':
            if s_bin_data[i + 6] == '0':
                i += 3+3+1+4
            else:
                j = 0
                while s_bin_data[i+6+j] == '1':
                    j += 5
                i += 6+j+5
                # print('i', i)
    print(version)


if __name__ == '__main__':
    # version_sum('test16')  # 16
    # version_sum('test12')  # 12
    # version_sum('test23')  # 23
    # version_sum('test31')  # 31
    version_sum('data_day16')  # 960
