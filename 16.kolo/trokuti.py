#! /usr/bin/python3
# Neven Sajko
from turtle import degrees, forward, left
degrees(6)


def trokut(duljina_strane):
    forward(duljina_strane)
    left(2)
    forward(duljina_strane)
    left(2)
    forward(duljina_strane)
    left(2)
    forward(duljina_strane/2)
    left(1)

i = int(input())

while (i > 1):
    trokut(i)
    i /= 2
