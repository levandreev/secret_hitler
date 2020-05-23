L = 6
F = 11



def calc_prob(fascist_cards, liberal_cards):
    remaining_cards = fascist_cards+liberal_cards
    # FFF prob
    fff_prob = fascist_cards/remaining_cards * (fascist_cards-1)/(remaining_cards-1) * (fascist_cards-2)/(remaining_cards-2)
    print('FFF -> ' + str(round(fff_prob, 2)))
    # LLL prob
    lll_prob = liberal_cards/remaining_cards * (liberal_cards-1)/(remaining_cards-1) * (liberal_cards-2)/(remaining_cards-2)
    print('LLL -> ' + str(round(lll_prob,2)))
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
calc_prob(11,6)


