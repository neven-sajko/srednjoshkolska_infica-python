#! /usr/bin/python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Neven Sajko

debug = False


def kolika_rupa(polje, koraka=1):
    '''Provjerava kolika je rupa prije danog polja koristeći
    skup polja-rupa 'rupe', te vraća broj [1-6] koraka dovoljan za
    preskakanje te rupe.
    '''
    if polje in rupe:
        return(kolika_rupa(polje - 1, koraka + 1))
    else:
        return(koraka)

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
        koraci = kolika_rupa(polje)
        potezi += 1
        continue
    koraci += 1

print(potezi)
