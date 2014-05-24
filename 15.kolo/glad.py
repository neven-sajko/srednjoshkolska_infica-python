#! /usr/bin/python3
# Neven Sajko

debug = False

sat = int(input())
mali = int(input())
# 'mali' = trajanje malog odmora = vrijeme kupovanja sandwicha
veliki = int(input())
vrijeme = 60*int(input()) + int(input())

raspored_sati = (8*60,)
for i in range(1, 12):
    if i in (3, 9):  # sati velikih odmora
        raspored_sati += (raspored_sati[len(raspored_sati)-1] + sat + veliki,)
    else:
        raspored_sati += (raspored_sati[len(raspored_sati)-1] + sat + mali,)
if debug:
    print(raspored_sati, vrijeme)


def main(time, schedule):
    for event in range(len(schedule)):
        if event == len(schedule)-1:
            if debug:
                print('Kraj ¹kole.')
            return schedule[event] + sat
        if schedule[event] + sat < time <= schedule[event+1] - mali:
            if debug:
                print('Odmor je i stigne¹ po sandwich.')
            return time
        elif time <= schedule[event] + sat:
            if debug:
                print('Sat je.')
            return schedule[event] + sat

vrijeme_za_sandwich = main(vrijeme, raspored_sati)

if vrijeme_za_sandwich == vrijeme:
    print('Kreni odmah')
else:
    print('Kreni za', vrijeme_za_sandwich-vrijeme)
