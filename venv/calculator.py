L = 6
F = 11

11/17 * 10/16 * 9/15

def calc_prob(fascist_cards, liberal_cards):
    # FFF prob
    fff_prob = fascist_cards/(fascist_cards+liberal_cards) * (fascist_cards-1)/(fascist_cards+liberal_cards-1) * (fascist_cards-2)/(fascist_cards+liberal_cards-2)
    print('FFF -> ' + str(round(fff_prob, 2)))
    # FFL prob

    # FLL prob

    # LLL prob

calc_prob(11,6)