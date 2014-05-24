#! /usr/bin/python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Neven Sajko

from turtle import forward, left, degrees


def to_and_fro(length, angle):
    left(angle)
    forward(length)
    forward(-length)
    left(-angle)


def larger_to_and_fro(length, angle):
    forward(b)
    left(3)
    forward(2*a)
    to_and_fro(length, angle)
    forward(-a)
    to_and_fro(length, angle)
    forward(-a)
    to_and_fro(length, angle)
    left(-3)
    forward(-b)

(a, b, c) = input().split()
(a, b, c) = (int(a), int(b), int(c))

# Smaller supplementary angles between a, b, c:
# <(c, b) = pi/3 = 60 degrees = 2 degrees
# <(a, b) = pi/2 = 90 degrees = 3 degrees
# <(a, c) = pi/6 = 30 degrees = 1 degree
degrees(12)  # The full angle is 360/30 degrees.

left(3)  # Rotate turtle to face "up".

for unused_count in (1, 2):
    larger_to_and_fro(c, 1)
    left(4)
    forward(c)
    left(-4)
larger_to_and_fro(b, 3)
left(3)
forward(2*a)
