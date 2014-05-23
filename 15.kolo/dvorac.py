#! /usr/bin/python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Neven Sajko

from turtle import degrees, forward, circle, left, pen

(n, d, r) = input().split()
(n, d, r) = (int(n), int(d), int(r))

degrees(n)  # 'n' is the full circle.

for unused_count in range(n):
    forward(d-4*r)
    pen(pendown=False)
    forward(2*r)
    pen(pendown=True)
    left(n/4)
    circle(r, 2*n-1)
    left(-n/4)
