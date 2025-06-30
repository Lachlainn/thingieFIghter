konstant = 5

def expected_score(player_elo, opponent_elo): #done separetely because this is also % chance of victory)
    return 1 / ((10 ** ((opponent_elo - player_elo) / 400)) + 1)

def calc_elo(player_elo, opponent_elo, player_score): #this is just straight up the chess elo system off some website
    new_elo = player_elo + (konstant * (player_score - expected_score(player_elo, opponent_elo)))
    if new_elo < 0:
        return 0
    else:
        return new_elo

#calc_elo(100, 100, 1)
#print(calc_elo(-100, 0, 1))
#calc_elo(2000, 20, 0.5)
#print(victory_chance(100, 500))

#expected = 1 / (10^[(B - A) / 400] + 1)