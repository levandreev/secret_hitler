L = 6
F = 11


def calc_prob(fascist_cards, liberal_cards):
    remaining_cards = fascist_cards+liberal_cards
    # FFF prob
    fff_prob = fascist_cards/remaining_cards * (fascist_cards-1)/(remaining_cards-1) * (fascist_cards-2)/(remaining_cards-2)
    print('FFF -> ' + str(round(fff_prob, 2)))
    #LLL prob
    lll_prob = liberal_cards/remaining_cards * (liberal_cards-1)/(remaining_cards-1) *(liberal_cards-2)/(remaining_cards-2)
    print('LLL -> ' + str(round(lll_prob,2)))
    #FFL prob
    ffl_prob = fascist_cards/remaining_cards * (fascist_cards-1)/(remaining_cards-1)* liberal_cards/(remaining_cards-2)
    print('FFL ->' + str(round(ffl_prob,2)))
    #FLL prob
    fll_prob = fascist_cards/remaining_cards * (liberal_cards-1)/(remaining_cards-1) *(liberal_cards-2)/(remaining_cards-2)
    print('FLL ->' + str(round(fll_prob,2)))
calc_prob(11,6)


