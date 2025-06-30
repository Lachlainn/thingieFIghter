import ELO
import random

cheese_wins = 0
love_wins = 0
max_elo = 0
exaggeration_factor = 1

thingies = [
    'Cheese',
    'Manchester United',
    'No New Ideas',
    'The Concept of Love',
    'Coffee',
]
elo_list = [0,0,0,0,0,0,0,0]

def update_max_elo():
    global max_elo
    for i in elo_list:
        if i > max_elo:
            max_elo = i


def get_player_index(player):
    return thingies.index(player)

def get_elo(player):  #returns the elo
    index = get_player_index(player)
    return elo_list[index]

def win_decider(player1, player2):
    random.seed()
    player_1_wins = ((((ELO.expected_score(get_elo(player1), get_elo(player2)) * 100))-50)*exaggeration_factor)+50
    roll = random.randrange(0, 99)
    print("Cheese wins if roll is over:", round(player_1_wins), "and roll is: ", roll)
    if roll == round(player_1_wins):
        return 0.5
    elif roll > player_1_wins:
        return 1
    else:
        return 0

def update_elo(player1, player2, score):
    elo_p_1 = get_elo(player1)
    elo_p_2 = get_elo(player2)
    index_1 = get_player_index(player1)
    index_2 = get_player_index(player2)
    new_elo_p_1 = ELO.calc_elo(elo_p_1, elo_p_2, score)
    new_elo_p_2 = ELO.calc_elo(elo_p_2, elo_p_1, 1 - score)
    elo_list[index_1] = new_elo_p_1
    elo_list[index_2] = new_elo_p_2

for i in range (1, 50):
    score = (win_decider('Cheese', 'The Concept of Love'))
    update_elo('Cheese', 'The Concept of Love', score)
    if score == 1:
        result = "~~ Cheese win!!!"
        cheese_wins += 1
    elif score == 0:
        result = "<3 The concept of love win!!!"
        love_wins += 1
    else:
        result = "It's a draw probably??"
    print(result," Cheese ELO: ", round(get_elo('Cheese')), "The Concept of Love ELO: ",round(get_elo('The Concept of Love')))
    print("---------next game----------")
    update_max_elo()

print('Cheese total wins:', cheese_wins, '  love total wins: ',  love_wins, "maximum elo: ",max_elo)