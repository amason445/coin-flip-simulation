import random

#returns trial results as byte object
def flip(success_rate):
    flip = random.uniform(0,1)
    if flip > success_rate:
        return 0b1
    else:
        return 0b0

#packages trial results into byte array for each expirement   
def trial_sequence(n_trials, success_rate):
    sequence = bytearray()
    for i in range(n_trials + 1):
        outcome = flip(success_rate)
        sequence.append(outcome)
    success_count = sequence.count(1)
    failure_count = sequence.count(0)
    return (n_trials, abs(success_rate - (success_count / n_trials)) * 100)
