#! /usr/bin/python3
# Neven Sajko
from turtle import degrees, left, forward

broj_krakova = int(input())
velki_krak = int(input())
mali_krak = velki_krak - int(input())
degrees(broj_krakova)
# Sets the perigon to broj_krakova degrees, in other words:
# broj_krakova/2 is the straight angle.


def izdanak_pahuljice():
    i = broj_krakova
    while i > 1:
        forward(mali_krak)
        forward(-mali_krak)
        left(1)
        i -= 1

i = broj_krakova
while i > 0:
    forward(velki_krak)
    left(broj_krakova/2 + 1)
    izdanak_pahuljice()
    forward(velki_krak)
    left(broj_krakova/2 + 1)
    i -= 1
