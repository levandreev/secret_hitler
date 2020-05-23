L = 6
F = 11


def calc_prob(fascist_cards, liberal_cards):
    # FFF prob
    fff_prob = fascist_cards/(fascist_cards+liberal_cards) * (fascist_cards-1)/(fascist_cards+liberal_cards-1) * (fascist_cards-2)/(fascist_cards+liberal_cards-2)
    print('FFF -> ' + str(round(fff_prob, 2)))
    # FFL prob

    # FLL prob

    # LLL prob

    lll_prob = liberal_cards/(liberal_cards+fascist_cards)*(liberal_cards-1)/(fascist_cards+liberal_cards-1)*(liberal_cards-2)/(fascist_cards+liberal_cards-2)
    print(lll_prob)
calc_prob(11,6)


