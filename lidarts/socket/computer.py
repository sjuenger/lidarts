from lidarts.models import Game
from collections import deque
import numpy as np

#checkout table contains the next field to aim at
checkout_table = {'170': 'T20', '167': 'T20', '164': 'T20', '161': 'T20', '160': 'T20', '158': 'T20',
                  '157': 'T20', '156': 'T20', '155': 'T20', '154': 'T20', '153': 'T20', '152': 'T20',
                  '151': 'T20', '150': 'T20', '149': 'T20', '148': 'T20', '147': 'T20', '146': 'T20',
                  '145': 'T20', '144': 'T20', '143': 'T20', '142': 'T20', '141': 'T20', '140': 'T20',
                  '139': 'T20', '138': 'T20', '137': 'T20', '136': 'T20', '135': 'T20', '134': 'T20',
                  '133': 'T20', '132': 'T20', '131': 'T19', '130': 'T20', '129': 'T19', '128': 'T18',
                  '127': 'T20', '126': 'T19', '125': 'T18', '124': 'T20', '123': 'T19', '122': 'T18',
                  '121': 'T20', '120': 'T20', '119': 'T19', '118': 'T20', '117': 'T19', '116': 'T19',
                  '115': 'T20', '114': 'T19', '113': 'T19', '112': 'T20', '111': 'T19', '110': 'T20',
                  '107': 'T19', '106': 'T20', '105': 'T20', '104': 'T19', '103': 'T19', '102': 'T20',
                  '101': 'T20', '100': 'T20', '99': 'T19', '98': 'T20', '97': 'T19', '96': 'T20', '95':
                      'T19', '94': 'T18', '93': 'T19', '92': 'T20', '91': 'T17', '90': 'T20', '89': 'T19',
                  '88': 'T20', '87': 'T17', '86': 'T18', '85': 'T15', '84': 'T20', '83': 'T17', '82': 'DB',
                  '81': 'T19', '80': 'T20', '79': 'T19', '78': 'T18', '77': 'T19', '76': 'T20', '75': 'T17',
                  '74': 'T14', '73': 'T19', '72': 'T16', '71': 'T13', '70': 'T18', '69': 'T19', '68': 'T16',
                  '67': 'T9', '66': 'T10', '65': 'T11', '64': 'T16', '63': 'T13', '62': 'T10', '61': 'T15',
                  '60': 'S20', '59': 'S19', '58': 'S18', '57': 'S17', '56': 'T16', '55': 'S15', '54': 'S14',
                  '53': 'S13', '52': 'S12', '51': 'S11', '50': 'S10', '49': 'S9', '48': 'S16', '47': 'S7',
                  '46': 'S6', '45': 'S13', '44': 'S12', '43': 'S3', '42': 'S10', '41': 'S9'}


def get_target(remaining_score, out_mode):
    # valid for the naive checkout table
    if remaining_score > 131:
        return 'T20'

    # master's out currently does not try to check on trebles
    if out_mode == 'do' or 'mo':
        # computer currently always try to checkout 50 instead of going 18-D16 if appropiate
        if remaining_score == 50:
            return 'D25'
        if remaining_score <= 40:
            if remaining_score % 2 == 0:
                return 'D' + str(int(remaining_score/2))
            else:
                # computer currently always sets up the next highest double (not ideal)
                return 'S' + str(1)
        else:
            return checkout_table[str(remaining_score)]

    # Single Out - just naive checkout attempts
    else:
        if remaining_score > 60:
            return 'T20'
        # always try to checkout on singles if possible
        elif remaining_score < 20 or remaining_score == 25:
            return 'S' + str(remaining_score)
        # try to checkout on doubles if possible
        elif remaining_score % 2 == 0:
            return 'D' + str(int(remaining_score/2))
        # try to checkout on trebles if possible
        elif remaining_score % 3 == 0:
            return 'T' + str(int(remaining_score/3))
        # set up 40 if score between 41 and 59
        elif remaining_score > 40:
            return 'S' + str(remaining_score-40)
        # set up 20 if score between 21 and 39
        else:
            return 'S' + str(remaining_score-20)


def throw_dart(target):
    possible_hits = {}

    # cyclic data structure to simulate the dartboard
    dartboard = deque([20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5])

    field_type = target[0]  # 'S', 'D' or 'T'

    # probabilities to hit: 0 / single / double / triple
    if field_type == 'S':
        hit_chance = [0, 0.8, 0.1, 0.1]
    elif field_type == 'D':
        hit_chance = [0.4, 0.3, 0.3, 0]
    else:
        hit_chance = [0, 0.8, 0, 0.2]

    if target == 'D25':
        # probabilities for double bull
        possible_hits['D25'] = 0.25
        possible_hits['S25'] = 0.35
        # all numbers have a basic chance to be hit
        for number in range(1, 21):
            field = 'S' + str(number)
            possible_hits[field] = 0.02
    elif target == 'S25':
        # probabilities for single bull
        possible_hits['D25'] = 0.15
        possible_hits['S25'] = 0.45
        # all numbers have a basic chance to be hit
        for number in range(1, 21):
            field = 'S' + str(number)
            possible_hits[field] = 0.02
    else:
        # target number
        target_numbers = [int(target[1:])]
        index = dartboard.index(int(target[1:]))

        # get numbers next to target
        dartboard.rotate(-index)
        target_numbers.append(dartboard[-1])
        target_numbers.append(dartboard[1])

        # probability to hit: target / number left / number right
        number_hit = str(np.random.choice(target_numbers, p=[0.7, 0.15, 0.15]))

        possible_hits['0'] = hit_chance[0]
        possible_hits['S' + number_hit] = hit_chance[1]
        possible_hits['D' + number_hit] = hit_chance[2]
        possible_hits['T' + number_hit] = hit_chance[3]

    hit = np.random.choice(list(possible_hits), p=list(possible_hits.values()))

    if hit == '0':
        return 0
    elif hit[0] == 'S':
        factor = 1
    elif hit[0] == 'D':
        factor = 2
    else:
        factor = 3

    number = int(hit[1:])
    return number*factor


def get_computer_score(hashid):
    game = Game.query.filter_by(hashid=hashid).first_or_404()

    # handling bullout

    # get current remaining score
    remaining_score = game.p2_score
    thrown_score_total = 0

    for dart in range(3):
        # acquire target depending on remaining score
        if game.closest_to_bull:
            return throw_dart('D25')
        else:
            target = get_target(remaining_score, game.out_mode)
        # simulate dart throw
        thrown_score = throw_dart(target)
        thrown_score_total += thrown_score
        remaining_score -= thrown_score
        # don't keep throwing if leg won or busted
        if remaining_score <= 0:
            break

    return thrown_score_total