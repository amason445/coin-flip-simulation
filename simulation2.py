import coin_flips
import matplotlib.pyplot as plt

def main():
    success_rate = 0.5
    expirements = range(1,100 + 1)
    trials = range(1, 20 + 1)
    outcome_list = []
    
    #iterate through experiments
    for i in range(0, len(expirements)):
        for j in range(0, len(trials)):
            trial_outcome = coin_flips.trial_sequence(trials[j], success_rate)
            outcome_list.append(trial_outcome)

    #filter function to isolate final head count from simulation
    outcome_filter = lambda x: True if x[0] == 20 else False
    outcome_list = list(filter(outcome_filter, outcome_list))

    outcome_counts = [i[1] for i in outcome_list]
  
    # generate outcome plot
    plt.hist(outcome_counts)
    plt.suptitle('Coin Flip Histogram')
    plt.title('Number of Heads Observed in 100 Sequences of 20 Coin Flips')
    plt.xlabel('Number of Heads')
    plt.ylabel('Frequency')
    plt.savefig('simulation2_plot.png')

if __name__ == '__main__':
    main()
