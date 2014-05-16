#! /usr/bin/python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Neven Sajko

formula = input()
upit = input()

count = 0
# broj ponavljanja elementa danog u upitu u formuli, rezultat
preskok = 0
# za preskočiti neke znakove formule prilikom iteracije kroz formulu

if len(upit) == 1:
    for i in range(len(formula)):
        i += preskok
        if i > len(formula) - 1:
            break
        if formula[i] == upit:
            if i == len(formula) - 1 or not formula[i+1].isdecimal():
                count += 1
            else:
                count += int(formula[i+1])
                preskok += 1
elif len(upit) == 2:
    for i in range(len(formula)):
        i += preskok
        if i > len(formula) - 1:
            break
        if formula[i] == upit[0] and formula[i+1] == upit[1]:
            if i == len(formula) - 1 or not formula[i+2].isdecimal():
                count += 1
                preskok += 1
            else:
                count += int(formula[i+2])
                preskok += 2

print(count)
