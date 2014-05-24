#! /usr/bin/python3
# Neven Sajko


def sports(result):
    return -10*result[0] + result[1]
skakači = [(int(input()), i) for i in range(1, 9)]

skakači.sort(key=sports)
print('S', skakači[0][1], '\nS', skakači[1][1], sep='')
