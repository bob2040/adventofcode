"""
Day 4: Giant Squid
https://adventofcode.com/2021/day/4
"""
import numpy as np


def input_boards_list(in_l):
    with open(in_l, 'r') as f:
        con = f.readlines()
    input_list = [int(i) for i in con[0].strip().split(',')]
    boards_rows = [[int(j) for j in con[i].split()] for i in range(2, len(con)) if con[i] != '\n']
    for g in range(5, len(input_list)):
        for i in range(0, len(boards_rows), 5):
            for j in range(5):
                for k in range(5):
                    a = np.matrix(boards_rows[i:i+5])
                    b = a.T
                    c = [input_list[o] for o in range(g)]
                    if all([True if d in c else False for d in a[j].tolist()[0]]):
                        return a, c
                    elif all([True if d in c else False for d in b[j].tolist()[0]]):
                        return b, c


 
def final_score(winning_board, input_number_list):
    w_b_l = winning_board.reshape(-1).tolist()[0]
    m_n_l = [i for i in input_number_list if i in w_b_l]
    num = input_number_list[::-1][0]
    return (sum(w_b_l) - sum(m_n_l)) * num


if __name__ == '__main__':
    w_b, i_n_l = input_boards_list('data_day4_giant_squid')
    print(final_score(w_b, i_n_l))  # 39902
    


