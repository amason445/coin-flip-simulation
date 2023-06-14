import coin_flips
import matplotlib.pyplot as plt

def main():
    success_rate = 0.5
    trials = range(1, 10000)
    outcome_list = []

    #iterate through experiments
    for i in range(0, len(trials)):
        outcome_list.append(coin_flips.trial_sequence(trials[i], success_rate))
                            
    #mapping function and transformation to transform outcome list to deltas
    outcome_map = lambda x: (x[0], abs(success_rate - (x[1]/ x[0])) * 100)     
    outcome_list = map(outcome_map, outcome_list)

    #generate outcome plot
    plt.scatter(*zip(*outcome_list))
    plt.suptitle('Coin Flip Simlation Scatter Plot')
    plt.title('Realized Distance from Expected Success Rate')
    plt.xlabel('Number of Trials')
    plt.ylabel('Delta as a Percentage')
    plt.savefig('simulation1_plot.png')

if __name__ == '__main__':
    main()
