#! /usr/bin/python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Neven Sajko

debug = True


def pazi_rupe(polje):
    '''Provjerava kolika je rupa prije danog polja koristeći
    skup polja-rupa 'rupe', te postavlja 'koraci' na broj dovoljan za
    preskakanje te rupe.
    '''
rupe = {int(input()) for rupa in range(int(input()))}
if debug:
    print(rupe)

potezi = 1
koraci = 1  # ili možda 0, ovisi jel se računa prvo polje?
for polje in range(1, 101):
    if debug and polje in rupe:
        print('Polje', polje, 'je rupa.')
    if debug:
        print(polje, koraci, potezi)
    if koraci == 6:
        if polje in rupe:
            if polje - 1 in rupe:
                if polje - 2 in rupe:
                    if polje - 3 in rupe:
                        if polje - 4 in rupe:
                            koraci = 6
                        else:
                            koraci = 5
                    else:
                        koraci = 4
                else:
                    koraci = 3
            else:
                koraci = 2
        else:
            koraci = 1
        potezi += 1
        continue
    koraci += 1

print(potezi)
