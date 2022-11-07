"""
Day 16: Packet Decoder,Part Two
https://adventofcode.com/2021/day/16#part2
"""


def get_result(data_path):
    data = open(data_path).read().strip()
    binary = bin(int(data, 16))[2:]
    while len(binary) < 4*len(data):
        binary = '0'+binary
    value, next_i = parse(binary, 0, 0)
    print(value)


def parse(bits, i, indent):
    type_ = int(bits[i+3:i+6], 2)
    if type_ == 4:
        i += 6
        v = 0
        while True:
            v = v*16 + int(bits[i+1:i+5], 2)
            i += 5
            if bits[i-5] == '0':
                return v, i
    else:
        len_id = int(bits[i+6], 2)
        vs = []
        if len_id == 0:
            len_bits = int(bits[i+7:i+7+15], 2)
            start_i = i+7+15
            i = start_i
            while True:
                v, next_i = parse(bits, i, indent+1)
                vs.append(v)
                i = next_i
                if next_i - start_i == len_bits:
                    break
        else:
            n_packets = int(bits[i+7:i+7+11], 2)
            i += 7+11
            for t in range(n_packets):
                v, next_i = parse(bits, i, indent+1)
                vs.append(v)
                i = next_i
        if type_ == 0:
            return sum(vs), i
        elif type_ == 1:
            ans = 1
            for v in vs:
                ans *= v
            return ans, i
        elif type_ == 2:
            return min(vs), i
        elif type_ == 3:
            return max(vs), i
        elif type_ == 5:
            return (1 if vs[0] > vs[1] else 0), i
        elif type_ == 6:
            return (1 if vs[0] < vs[1] else 0), i
        elif type_ == 7:
            return (1 if vs[0] == vs[1] else 0), i


if __name__ == '__main__':
    get_result('data_day16')  # 12301926782560
