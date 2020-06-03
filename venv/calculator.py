import pandas as pd
import numpy as np

probs = []
L = 7
F = 13
def calc_prob():
    fascist_cards = F
    liberal_cards = L
    remaining_cards = fascist_cards+liberal_cards
    # FFF prob
    fff_prob = fascist_cards/remaining_cards * (fascist_cards-1)/(remaining_cards-1) * (fascist_cards-2)/(remaining_cards-2)
    print('FFF -> ' + str(round(fff_prob, 2)))
    probs.append(fff_prob)
    # LLL prob
    lll_prob = liberal_cards/remaining_cards * (liberal_cards-1)/(remaining_cards-1) * (liberal_cards-2)/(remaining_cards-2)
    print('LLL -> ' + str(round(lll_prob,2)))
    probs.append(lll_prob)
    # FFL prob
    # ffl
    ffl_prob = fascist_cards/remaining_cards * (fascist_cards-1)/(remaining_cards-1) * liberal_cards/(remaining_cards-2)
    # flf
    flf_prob = fascist_cards/remaining_cards * (liberal_cards)/(remaining_cards-1) * (fascist_cards-1)/(remaining_cards-2)
    # lff
    lff_prob = liberal_cards/remaining_cards * (fascist_cards)/(remaining_cards-1) * (fascist_cards-1)/(remaining_cards-2)
    # sum for FFL
    ffl_real = ffl_prob + flf_prob + lff_prob
    print('FFL -> ' + str(round(ffl_real,2)))
    probs.append(fff_prob)
    # FLL prob
    # fll
    fll_prob = fascist_cards/remaining_cards * (liberal_cards)/(remaining_cards-1) * (liberal_cards-1)/(remaining_cards-2)
    # lfl
    lfl_prob = liberal_cards/remaining_cards * (fascist_cards)/(remaining_cards-1) * (liberal_cards-1)/(remaining_cards-2)
    # llf
    llf_prob = liberal_cards/remaining_cards * (liberal_cards-1)/(remaining_cards-1) * (fascist_cards)/(remaining_cards-2)
    # sum for FLL
    fll_real = fll_prob + lfl_prob + llf_prob
    print('FLL -> ' + str(round(fll_real,2)))
    probs.append(ffl_real)


def claims_fff():
    print('TRURTH (FFF)')
    global F
    # global L
    F = F-3
    # calc_prob()
    # print('LIE')
    # print('CASE FFL: ')
    # L = L-1
    # print(F)
    calc_prob()


def claims_ffl():
    print('TRURTH (FFL)')
    global F
    global L
    F = F-2
    L = L-1
    calc_prob()
def claims_fll():
    print('TRURTH (FLL)')
    global F
    global L
    F -= 1
    L = L-2
    calc_prob()
def claims_lll():
    print('TRURTH (LLL)')
    global L
    L = L-3
    calc_prob()
def redo_fff():
    print('REDOf (FFF)')
    global F
    F = F+3
def redo_fll():
    print('REDOf (FLL)')
    global F
    global L
    F = F+1
    L += 2
def redo_ffl():
    print('REDOf (FFL)')
    global F
    global L
    F = F+2
    L += 1
def redo_lll():
    print('REDOf (LLL)')
    L += 3
