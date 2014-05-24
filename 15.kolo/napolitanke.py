#! /usr/bin/python3
# Neven Sajko

napolitanki_u_otvorenoj_kutiji_1 = int(input())
neotvorenih_kutija_1 = int(input())
napolitanki_u_otvorenoj_kutiji_2 = int(input())
neotvorenih_kutija_2 = int(input())
n = 40  # broj napolitanki u neotvorenim kutijama

napolitanki_prije = napolitanki_u_otvorenoj_kutiji_1 + n*neotvorenih_kutija_1
napolitanki_poslije = napolitanki_u_otvorenoj_kutiji_2 + n*neotvorenih_kutija_2

print(-(-(napolitanki_prije - napolitanki_poslije) // 40))
