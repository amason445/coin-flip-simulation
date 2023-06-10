import coin_flips
import matplotlib.pyplot as plt

success_rate = 0.5
trials = range(1, 10000)
outcome_list = []

#iterate through expirements
for i in range(0, len(trials)):
    outcome_list.append(coin_flips.trial_sequence(trials[i], success_rate))

#generate outcome
plt.scatter(*zip(*outcome_list))
plt.suptitle('Coin Flip Simlation Scatter Plot')
plt.title('Distance from Expected Probability and Realized Success Rate')
plt.xlabel('Number of Sequential Coin Flips')
plt.ylabel('Distance from Expected Success Rate in Percent')
plt.savefig('output_plot.png')


