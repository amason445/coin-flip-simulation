import coin_flips
import matplotlib.pyplot as plt

success_rate = 0.5
trials = range(1, 10000)
outcome_list = []

#iterate through experiments
for i in range(0, len(trials)):
    outcome_list.append(coin_flips.trial_sequence(trials[i], success_rate))

#generate outcome plot
plt.scatter(*zip(*outcome_list))
plt.suptitle('Coin Flip Simlation Scatter Plot')
plt.title('Realized Distance from Expected Success Rate')
plt.xlabel('Number of Trials')
plt.ylabel('Delta as a Percentage')
plt.savefig('output_plot.png')


