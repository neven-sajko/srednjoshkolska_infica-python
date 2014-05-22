#! /usr/bin/python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Neven Sajko

from turtle import degrees, forward, circle#, left, pen

(n, d, r) = input().split()
(n, d, r) = (int(n), int(d), int(r))

degrees(360/n)

for unused_count in range(n):
    forward(d-2*r)
    circle(r, 2*n-1)
