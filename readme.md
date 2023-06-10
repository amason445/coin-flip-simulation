# Coin Flip Simulation
## Summary
I wrote a simple script that simulates a fair coin being fliped and compared the expected success rate to the realized success rate. The expirements were packaged into bytearrays containing the trial outcomes.

## Methodolgy
- Each expirement follows a binomial distribution since a coin toss can be measured as a discrete outcome. Additionally, each coin toss is independent from one another and generated from a uniform distribution. Tosses above the success rate are considered a success.
- I encoded each sequence trial outcomes into bytearray objects and then counted the success rate for each expirement.
- Since the expected number of successes is equal to the number of trials multiplied by the theoretical success rate, the realized success rate is therefore equal to the number of observed success divided by the total number of trials.
- Once this was completed, I packaged this information into the below visualization.

## Formulas
$${Mean\ of\ the\ Binomial\ Distribution:\ }\mu = {Number\ of\ Trials}\cdot {Theoretical\ Success\ Rate}$$

$${Realized\ Success\ Rate:\ }{Realized\ Success\ Rate} = \frac{Number\  of\ Successes}{Number\ of\ Trials}$$

$${Distance\ between\ Theoretical\ and\ Realized\ Success\ Rate:\ }\Delta = \vert{\mu - Realized\ Success\ Rate}\vert$$

## Output
![alt text](output_plot.png)
