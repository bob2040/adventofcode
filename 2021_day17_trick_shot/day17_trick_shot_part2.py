"""
Day 17: Trick Shot,Part Two
https://adventofcode.com/2021/day/17#part2
"""


def how_many():
    total = 0
    for x in range(1, 263 + 1):
        for y in range(-115, 115):
            vx, vy = x, y
            x_p = y_p = 0
            for _ in range(2 * 115 + 1):
                x_p += vx
                y_p += vy
                vx = max(vx - 1, 0)
                vy -= 1

                if -115 <= y_p <= -63 and 207 <= x_p <= 263:
                    total += 1
                    break
                elif y_p < -115 or x_p > 263:
                    break

    print(total)  # 4973


if __name__ == '__main__':
    how_many()
